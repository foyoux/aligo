"""..."""
import hashlib
import os
import shutil
from datetime import datetime
from typing import Callable
from typing import Dict, Union
from typing import Optional

from aligo.core import *
from aligo.request import GetFileListRequest, MoveFileToTrashRequest, CreateFolderRequest
from aligo.types import BaseFile


def utc_str_to_timestamp(utc: str) -> int:
    """'2022-04-16T11:07:03.276Z' -> timestamp"""
    return int(datetime.fromisoformat(utc[:-1]).timestamp()) + 28800


class SyncFolder(Core):
    """sync folder

    冲突：本地和云端冲突，一端是文件，另一端是文件夹，此种情况跳过，统一不处理

    三种同步模式：
        1. 双端同步
            差异文件保持最新；独有文件上传和下载，保持共有。

        2. 本地为主
            差异文件，本地为主；本地独有文件，上传；云端独有文件，忽略。

        3. 云端为主
            差异文件，云端为主；云端独有文件，下载；本地独有文件，忽略。
    """

    def sync_folder(
            self,
            local_folder: str,
            remote_folder: str,
            flag: Optional[bool] = None,
            file_filter: Callable[[Union[str, BaseFile]], bool] = lambda x: False,
            ignore_content: bool = False,
            follow_delete: bool = False,
            drive_id: str = None
    ):
        """
        sync folder
        :param local_folder: 本地文件夹路径
        :param remote_folder: 云端文件夹 file_id
        :param flag: 同步标志（类型），默认：None, 另外可选：True, False
            None：双端同步
            True：以本地为主
            False：以云端为主
        :param file_filter: 文件过滤函数，参数为 本地文件绝对路径 / 云端文件 BaseFile，返回值为 `True` 则过滤，可用于实现 只同步 特定文件 或 排除某些文件
        :param ignore_content: 是否忽略文件内容，默认：False
        :param follow_delete: 是否跟随删除，默认：False
        :param drive_id: 云端文件夹 drive_id
        :return:

        :Example:
        >>> from aligo import Aligo
        >>> ali = Aligo()
        >>> ali.sync_folder('<本地路径>', '<云端文件夹 file_id>')
        """
        if flag is None:
            self._auth.log.info('sync_folder: 双端同步')
        elif flag:
            self._auth.log.info('sync_folder: 本地为主')
        else:
            self._auth.log.info('sync_folder: 云端为主')

        if not os.path.exists(local_folder):
            self._auth.log.warning('本地文件夹不存在，创建: %s', local_folder)
            os.makedirs(local_folder)
        self.__sync_folder(local_folder, remote_folder, flag, file_filter, ignore_content, follow_delete, drive_id)

    def __sync_folder(
            self,
            local_folder: str,
            remote_folder: str,
            flag: Optional[bool],
            file_filter: Callable[[Union[str, BaseFile]], bool],
            ignore_content: bool,
            follow_delete: bool,
            drive_id: str):
        """..."""
        # 获取local_folder下的所有文件 # 转为 {文件名:文件路径} 字典模式
        local_files = {}
        for f in os.listdir(local_folder):
            local_file = os.path.join(local_folder, f)
            # 过滤文件只处理文件，跳过 文件夹
            if os.path.isfile(local_file) and file_filter(local_file):
                self._auth.log.debug(f'过滤本地文件 {local_file}')
                continue
            local_files[f] = local_file
        # 获取remote_folder下的所有文件 # 转为 {文件名:BaseFile对象} 字典模式
        remote_files: Dict[str, BaseFile] = {}
        for f in self._core_get_file_list(
                GetFileListRequest(remote_folder, drive_id=drive_id)
        ):
            remote_file = f.name
            if f.type == 'file' and file_filter(f):
                self._auth.log.debug(f'过滤云端文件 {remote_file}')
                continue
            remote_files[remote_file] = f

        if flag is None:
            self.__sync_all(
                drive_id, file_filter, flag, local_files, local_folder, remote_files, remote_folder, ignore_content,
                follow_delete)
        elif flag:
            self.__sync_local(
                drive_id, local_files, remote_files, remote_folder, flag, file_filter, local_folder, ignore_content,
                follow_delete)
        else:
            self.__sync_remote(drive_id, local_files, remote_files, local_folder, flag, file_filter, ignore_content,
                               follow_delete)

    def __sync_all(
            self, drive_id, file_filter, flag, local_files, local_folder, remote_files, remote_folder, ignore_content,
            follow_delete
    ):
        # 双端同步
        for f in list(local_files):
            # 在字典中获取并删除 local_file
            local_file = local_files.pop(f)
            # 文件夹则递归
            if os.path.isdir(local_file):
                # 判断云端是否存在
                if f in remote_files:
                    # 如果有，则判断是不是文件夹，不是就跳过
                    remote_file = remote_files.pop(f)
                    if remote_file.type == 'file':
                        # 跳过冲突
                        self._auth.log.warning(f'冲突：本地是文件夹，云端是文件，不处理 {f}')
                        continue
                else:
                    # 如果没有，则创建文件夹
                    self._auth.log.debug(f'本地是文件夹，云端不存在，创建云端文件夹，并递归 {f}')
                    remote_file = self._core_create_folder(
                        CreateFolderRequest(name=f, parent_file_id=remote_folder, drive_id=drive_id,
                                            check_name_mode='overwrite')
                    )
                self.__sync_folder(local_file, remote_file.file_id, flag, file_filter, ignore_content, follow_delete,
                                   drive_id)
                continue

            # 如果本地文件存在，且在云端也存在，则依次比较 size，sha1，时间戳
            if f in remote_files:
                # 在字典中获取并删除 remote_file
                remote_file = remote_files.pop(f)
                # 先判断文件类型
                if remote_file.type == 'folder':
                    # 没有主次端，不自动处理冲突
                    self._auth.log.warning(f'冲突：本地为文件，云端为文件夹，不处理 {f}')
                    continue

                # 获取 f 文件大小
                local_size = os.path.getsize(local_file)
                # 比较大小
                if local_size == remote_file.size:
                    # 跳过对比文件内容
                    if ignore_content:
                        self._auth.log.warning(f'忽略文件内容: 不处理 {f}')
                        continue

                    # 计算 f 文件 sha1
                    local_sha1 = self._core_sha1(local_file).lower()
                    # 如果sha1值相同，则跳过
                    if local_sha1 == remote_file.content_hash.lower():
                        self._auth.log.debug(f'文件 {f} 已存在，且sha1值相同，跳过')
                        continue
                # 否则对比时间戳，删除较旧文件，同步最新文件
                # 获取 f 文件的最后修改时间
                local_time = os.path.getmtime(local_file)
                local_time = int(local_time)
                # 获取云端文件的最后修改时间
                remote_time = remote_file.updated_at
                # 将UTC时间字符串转换为时间戳
                remote_time = utc_str_to_timestamp(remote_time)
                # 比较时间戳，删除较旧文件，同步最新文件
                if local_time > remote_time:
                    # 覆盖方式上传文件
                    self._auth.log.debug(f'本地文件较新，上传本地文件 {f}')
                    self.upload_file(file_path=local_file, parent_file_id=remote_folder, name=f,
                                     drive_id=drive_id, check_name_mode='overwrite')
                elif local_time < remote_time:
                    # 云端较新，删除本地，下载云端文件
                    self._auth.log.debug(f'云端较新，删除本地，下载云端文件 {f}')
                    os.remove(local_file)
                    self.download_files([remote_file], local_folder)
            else:
                # 不存在则直接上传
                self._auth.log.debug(f'云端不存在，上传本地文件 {f}')
                self.upload_file(file_path=local_file, parent_file_id=remote_folder, name=f,
                                 drive_id=drive_id, check_name_mode='overwrite')
        # 剩下的就是云端文件夹中有，本地文件夹中没有的文件，下载到本地
        if len(remote_files) != 0:
            self._auth.log.debug(f'本地不存在，下载云端文件 {len(remote_files)} {list(remote_files.keys())}')
            for remote_file in remote_files.values():
                if remote_file.type == 'file':
                    self.download_files([remote_file], local_folder)
                else:
                    self.download_folder(remote_file.file_id, local_folder)  # type: ignore

    def __sync_remote(self, drive_id, local_files, remote_files,
                      local_folder, flag, file_filter, ignore_content, follow_delete):
        # 以云端为主
        for f in list(remote_files):
            remote_file = remote_files.pop(f)
            # 文件夹则递归
            if remote_file.type == 'folder':
                # 判断本地是否存在
                if f in local_files:
                    # 如果有，则判断是否是文件夹，不是就忽略
                    local_file = local_files.pop(f)
                    if os.path.isfile(local_file):
                        # 跳过冲突
                        self._auth.log.warning(f'冲突：本地是文件，云端是文件夹，不处理 {f}')
                else:
                    # 如果没有，则创建本地文件夹
                    local_file = os.path.join(local_folder, f)
                    self._auth.log.debug(f'云端是文件夹，本地没有，创建文件夹，并递归 {local_file}')
                    if not os.path.exists(local_file):
                        os.mkdir(local_file)
                self.__sync_folder(local_file, remote_file.file_id, flag, file_filter, ignore_content, follow_delete,
                                   drive_id)
                continue

            # 如果云端文件存在，且在本地也存在，则依次比较 size，sha1，时间戳
            if f in local_files:
                local_file = local_files.pop(f)
                # 先判断文件类型
                if os.path.isdir(local_file):
                    # 云端为文件，本地却是文件夹，则递归删除文件夹，再下载文件
                    self._auth.log.debug('云端为文件，本地却是文件夹，则递归删除文件夹，再下载文件')
                    # 递归删除文件夹
                    shutil.rmtree(local_file)
                    # 下载文件
                    self.download_files([remote_file], local_folder)
                    continue

                # 获取 f 文件大小
                remote_size = remote_file.size
                # 比较大小
                if remote_size == os.path.getsize(local_file):
                    # 跳过对比文件内容
                    if ignore_content:
                        self._auth.log.warning(f'忽略文件内容: 不处理 {f}')
                        continue

                    # 计算 f 文件 sha1
                    local_sha1 = self._core_sha1(local_file).lower()
                    # 如果sha1值相同，则跳过
                    if local_sha1 == remote_file.content_hash.lower():
                        self._auth.log.debug(f'文件 {local_file} 已存在，且sha1值相同，跳过')
                        continue
                os.remove(local_file)
                self.download_files([remote_file], local_folder)
            else:
                # 不存在直接下载
                local_file = os.path.join(local_folder, f)
                self._auth.log.debug(f'本地不存在，下载云端文件 {local_file}')
                self.download_files([remote_file], local_folder)

        # 剩下的就是云端文件夹中没有，本地文件夹中有的文件，删除
        if follow_delete and len(local_files) != 0:
            self._auth.log.debug(f'云端不存在，本地存在 删除 {len(local_files)} {list(local_files.keys())}')
            for local_file in local_files.values():
                if os.path.isfile(local_file):
                    os.remove(local_file)
                else:
                    shutil.rmtree(local_file)

    def __sync_local(self, drive_id, local_files, remote_files,
                     remote_folder, flag, file_filter, local_folder, ignore_content, follow_delete):
        # 以本地为主
        for f in list(local_files):
            local_file = local_files.pop(f)
            # 文件夹则递归
            if os.path.isdir(local_file):
                # 判断云端是否存在
                if f in remote_files:
                    # 如果有，则判断是不是文件夹，不是就删除
                    remote_file = remote_files.pop(f)
                    if remote_file.type == 'file':
                        # 删除云端文件并创建文件夹
                        self._auth.log.warning(f'冲突：本地是文件夹，云端是文件，不处理 {f}')
                else:
                    # 如果没有，则创建文件夹
                    self._auth.log.debug(f'本地是文件夹，云端不存在，创建云端文件夹，并递归 {f}')
                    remote_file = self._core_create_folder(
                        CreateFolderRequest(name=f, parent_file_id=remote_folder, drive_id=drive_id,
                                            check_name_mode='overwrite')
                    )
                self.__sync_folder(local_file, remote_file.file_id, flag, file_filter, ignore_content, follow_delete,
                                   drive_id)
                continue

            # 如果本地文件存在，且在云端也存在，则依次比较 size，sha1，时间戳
            if f in remote_files:
                # 在字典中删除remote_file
                remote_file = remote_files.pop(f)
                # 先判断文件类型
                if remote_file.type == 'folder':
                    # 以本地文件夹为主，那只有删除云端文件夹，再上传本地文件
                    self._auth.log.debug(f'本地为文件，云端为文件夹，删除云端文件夹，并上传本地文件 {f}')
                    self._core_move_file_to_trash(
                        MoveFileToTrashRequest(file_id=remote_file.file_id, drive_id=drive_id)
                    )
                    self._auth.log.debug(f'上传本地文件 {f}')
                    self.upload_file(file_path=local_file, parent_file_id=remote_folder, name=f,
                                     drive_id=drive_id, check_name_mode='overwrite')
                    continue

                # 获取 f 文件大小
                local_size = os.path.getsize(local_file)
                # 比较大小
                if local_size == remote_file.size:
                    # 跳过对比文件内容
                    if ignore_content:
                        self._auth.log.warning(f'忽略文件内容: 不处理 {f}')
                        continue

                    # 计算 f 文件 sha1
                    local_sha1 = self._core_sha1(local_file).lower()
                    # 如果sha1值相同，则跳过
                    if local_sha1 == remote_file.content_hash.lower():
                        self._auth.log.debug(f'文件 {f} 已存在，且sha1值相同，跳过')
                        continue
                    else:
                        self.upload_file(file_path=local_file, parent_file_id=remote_folder, name=f,
                                         drive_id=drive_id, check_name_mode='overwrite')
                else:
                    self.upload_file(file_path=local_file, parent_file_id=remote_folder, name=f,
                                     drive_id=drive_id, check_name_mode='overwrite')
            else:
                # 不存在则直接上传
                self._auth.log.debug(f'云端不存在，上传本地文件 {f}')
                self.upload_file(file_path=local_file, parent_file_id=remote_folder, name=f,
                                 drive_id=drive_id, check_name_mode='overwrite')

        # 剩下的就是本地文件夹中没有，云端文件夹中有的文件，删除
        if follow_delete and len(remote_files) != 0:
            self._auth.log.debug(f'本地不存在，云端存在 删除 {len(remote_files)} {list(remote_files.keys())}')
            self.batch_move_to_trash([remote_file.file_id for remote_file in remote_files.values()])  # type: ignore

    @staticmethod
    def _core_sha1(param):
        """计算文件sha1"""
        sha1 = hashlib.sha1()
        with open(param, 'rb') as f:
            while True:
                data = f.read(8192)
                if not data:
                    break
                sha1.update(data)
        return sha1.hexdigest()
