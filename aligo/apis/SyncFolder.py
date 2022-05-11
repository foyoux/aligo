"""..."""
import hashlib
import os
import shutil
from datetime import datetime
from pathlib import Path
from typing import Callable
from typing import Dict
from typing import Optional

from aligo.core import *
from aligo.request import GetFileListRequest, MoveFileToTrashRequest, CreateFolderRequest, BatchMoveToTrashRequest
from aligo.types import BaseFile


def utc_str_to_timestamp(utc: str) -> int:
    """'2022-04-16T11:07:03.276Z' -> timestamp"""
    return int(datetime.fromisoformat(utc[:-1]).timestamp()) + 28800


class SyncFolder(Core):
    """sync folder"""

    def sync_folder(
            self,
            local_folder: str,
            remote_folder: str,
            flag: Optional[bool] = None,
            follow_delete: bool = False,
            file_filter: Callable[[str], bool] = lambda x: False,
            ignore_content: bool = False,
            drive_id: str = None):
        """
        sync folder
        :param local_folder: 本地文件夹路径
        :param remote_folder: 云端文件夹 file_id
        :param flag: 同步标志（类型），默认：None, 另外可选：True, False
            - 冲突是指，程序无法自动处理的情况，例如：两端具有同名文件，但一个是文件，另一个是文件夹
            - 保持文件最新是指，两端具有同名文件，则下载或上传最新(根据最后修改时间)的文件，不受哪端为主的约束，三种模式处理方式均相同
            - 以某端为主
                - 会影响程序解决冲突的方式：删除次端冲突，保持主端文件。
                - 主端存在的，会同步到次端，反之则不会，并且会根据 `follow_delete`(是否跟随删除) 参数决定是否删除次端文件 
            None：
                - 不自动解决冲突
                - 不存在主次端
                - 同步所有文件，本地有的就上传，远端有的就下载，都有的看是否冲突，不冲突则保持最新
                - 此时会忽略 `follow_delete` 参数
            True：以本地为主
            False：以云端为主
        :param follow_delete: 次端是否跟随主端删除
        :param file_filter: 文件过滤函数，参数文件名，返回值为True则过滤，可用于实现 只同步 特定文件 或 排除某些文件
        :param ignore_content: 是否忽略文件内容，默认：False. 来自 issues/19 的功能请求
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
        # 不管三七二十一，先创建一波
        Path(local_folder).mkdir(parents=True, exist_ok=True)
        self.__sync_folder(local_folder, remote_folder, flag, follow_delete, file_filter, ignore_content, drive_id)

    def __sync_folder(
            self,
            local_folder: str,
            remote_folder: str,
            flag: Optional[bool] = True,
            follow_delete: bool = False,
            file_filter: Callable[[str], bool] = lambda x: False,
            ignore_content: bool = False,
            drive_id: str = None):
        """..."""
        # 获取local_folder下的所有文件 # 转为 {文件名:文件路径} 字典模式
        local_files = {}
        for f in os.listdir(local_folder):
            local_file = os.path.join(local_folder, f)
            if os.path.isfile(local_file) and file_filter(f):
                self._auth.log.debug(f'过滤本地文件 {local_file}')
                continue
            local_files[f] = local_file
        # 获取remote_folder下的所有文件 # 转为 {文件名:BaseFile对象} 字典模式
        remote_files: Dict[str, BaseFile] = {}
        for f in self._core_get_file_list(
                GetFileListRequest(remote_folder, drive_id=drive_id)
        ):
            remote_file = f.name
            if f.type == 'file' and file_filter(remote_file):
                self._auth.log.debug(f'过滤云端文件 {remote_file}')
                continue
            remote_files[remote_file] = f

        if flag is None:
            self.__sync_all(drive_id, file_filter, flag, follow_delete, local_files,
                            local_folder, remote_files, remote_folder, ignore_content)
        elif flag:
            self.__sync_local(drive_id, follow_delete, local_files, remote_files,
                              remote_folder, flag, file_filter, local_folder, ignore_content)
        else:
            self.__sync_remote(drive_id, follow_delete, local_files, remote_files,
                               local_folder, flag, file_filter, ignore_content)

    def __sync_all(self, drive_id, file_filter, flag, follow_delete, local_files, local_folder, remote_files,
                   remote_folder, ignore_content):
        # 双端同步
        for f in local_files:
            local_file = local_files[f]
            # 文件夹则递归
            if os.path.isdir(local_file):
                # 判断云端是否存在
                if f in remote_files:
                    # 如果有，则判断是不是文件夹，不是就删除
                    remote_file = remote_files[f]
                    remote_files.pop(f)
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
                self.__sync_folder(local_file, remote_file.file_id, flag, follow_delete, file_filter, ignore_content,
                                   drive_id)
                continue

            # 如果本地文件存在，且在云端也存在，则依次比较 size，sha1，时间戳
            if f in remote_files:
                remote_file = remote_files[f]
                # 先判断文件类型
                if remote_file.type == 'folder':
                    # 没有主次端，不自动处理冲突
                    self._auth.log.warning(f'冲突：本地为文件，云端为文件夹，不处理 {f}')
                    remote_files.pop(f)
                    continue

                # 跳过对比文件内容
                if ignore_content:
                    self._auth.log.warning(f'忽略文件内容: 不处理 {f}')
                    remote_files.pop(f)
                    continue

                # 获取 f 文件大小
                local_size = os.path.getsize(local_file)
                # 比较大小
                if local_size == remote_file.size:
                    # 计算 f 文件 sha1
                    local_sha1 = self._core_sha1(local_file).lower()
                    # 如果sha1值相同，则跳过
                    if local_sha1 == remote_file.content_hash.lower():
                        self._auth.log.debug(f'文件 {f} 已存在，且sha1值相同，跳过')
                        remote_files.pop(f)
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
                # 在字典中删除remote_file
                remote_files.pop(f)
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

    def __sync_remote(self, drive_id, follow_delete, local_files, remote_files,
                      local_folder, flag, file_filter, ignore_content):
        # 以云端为主
        for f in remote_files:
            remote_file = remote_files[f]
            # 文件夹则递归
            if remote_file.type == 'folder':
                # 判断本地是否存在
                if f in local_files:
                    # 如果有，则判断是否是文件夹，不是就删除
                    local_file = local_files[f]
                    if os.path.isfile(local_file):
                        # 删除本地文件，创建本地文件夹
                        self._auth.log.debug(f'云端是文件夹，本地是文件，删除本地文件，并创建文件夹 {local_file}')
                        os.remove(local_file)
                        os.mkdir(local_file)
                    local_files.pop(f)
                else:
                    # 如果没有，则创建本地文件夹
                    local_file = os.path.join(local_folder, f)
                    self._auth.log.debug(f'云端是文件夹，本地没有，创建文件夹，并递归 {local_file}')
                    os.mkdir(local_file)
                self.__sync_folder(local_file, remote_file.file_id, flag, follow_delete, file_filter, ignore_content,
                                   drive_id)
                continue

            # 如果云端文件存在，且在本地也存在，则依次比较 size，sha1，时间戳
            if f in local_files:
                local_file = local_files[f]
                # 先判断文件类型
                if os.path.isdir(local_file):
                    # 云端为文件，本地却是文件夹，则递归删除文件夹，再下载文件
                    self._auth.log.debug('云端为文件，本地却是文件夹，则递归删除文件夹，再下载文件')
                    # 递归删除文件夹
                    shutil.rmtree(local_file)
                    # 下载文件
                    self.download_files([remote_file], local_folder)
                    local_files.pop(f)
                    continue

                # 跳过对比文件内容
                if ignore_content:
                    self._auth.log.warning(f'忽略文件内容: 不处理 {f}')
                    local_files.pop(f)
                    continue

                # 获取 f 文件大小
                remote_size = remote_file.size
                # 比较大小
                if remote_size == os.path.getsize(local_file):
                    # 计算 f 文件 sha1
                    local_sha1 = self._core_sha1(local_file).lower()
                    # 如果sha1值相同，则跳过
                    if local_sha1 == remote_file.content_hash.lower():
                        self._auth.log.debug(f'文件 {local_file} 已存在，且sha1值相同，跳过')
                        local_files.pop(f)
                        continue
                # 否则对比时间戳，删除较旧文件，同步最新文件
                # 获取 f 文件的最后修改时间
                remote_time = remote_file.updated_at
                # 将UTC时间字符串转换为时间戳
                remote_time = utc_str_to_timestamp(remote_time)
                # 获取本地文件的最后修改时间
                local_time = os.path.getmtime(local_file)
                local_time = int(local_time)
                # 比较时间戳，删除较旧文件，同步最新文件
                if local_time < remote_time:
                    # 先删除本地文件，再下载
                    self._auth.log.debug(f'云端文件较新，先删除本地文件，再下载云端文件 {local_file}')
                    os.remove(local_file)
                    self.download_files([remote_file], local_folder)
                elif local_time < remote_time:
                    # 云端较新，删除本地，下载云端文件
                    self._auth.log.debug(f'云端较新，删除本地，下载云端文件 {f}')
                    os.remove(local_file)
                    self.download_files([remote_file], local_folder)
                # 在字典中删除local_file
                local_files.pop(f)
            else:
                # 不存在直接下载
                local_file = os.path.join(local_folder, f)
                self._auth.log.debug(f'本地不存在，下载云端文件 {local_file}')
                self.download_files([remote_file], local_folder)

        # local_files剩下的就是多余的
        if follow_delete and len(local_files) != 0:
            self._auth.log.debug(f'删除本地文件 {len(local_files)} {list(local_files.values())}')
            for f in local_files:
                local_file = local_files[f]
                if os.path.isdir(local_file):
                    shutil.rmtree(local_file)
                else:
                    os.remove(local_file)

    def __sync_local(self, drive_id, follow_delete, local_files, remote_files,
                     remote_folder, flag, file_filter, local_folder, ignore_content):
        # 以本地为主
        for f in local_files:
            local_file = local_files[f]
            # 文件夹则递归
            if os.path.isdir(local_file):
                # 判断云端是否存在
                if f in remote_files:
                    # 如果有，则判断是不是文件夹，不是就删除
                    remote_file = remote_files[f]
                    if remote_file.type == 'file':
                        # 删除云端文件并创建文件夹
                        self._auth.log.debug(f'本地是文件夹，云端是文件，删除云端文件，并在云端创建文件夹 {f}')
                        self._core_move_file_to_trash(
                            MoveFileToTrashRequest(file_id=remote_file.file_id, drive_id=drive_id)
                        )
                        remote_file = self._core_create_folder(
                            CreateFolderRequest(name=f, parent_file_id=remote_folder, drive_id=drive_id,
                                                check_name_mode='overwrite')
                        )
                    remote_files.pop(f)
                else:
                    # 如果没有，则创建文件夹
                    self._auth.log.debug(f'本地是文件夹，云端不存在，创建云端文件夹，并递归 {f}')
                    remote_file = self._core_create_folder(
                        CreateFolderRequest(name=f, parent_file_id=remote_folder, drive_id=drive_id,
                                            check_name_mode='overwrite')
                    )
                self.__sync_folder(local_file, remote_file.file_id, flag, follow_delete, file_filter, ignore_content,
                                   drive_id)
                continue

            # 如果本地文件存在，且在云端也存在，则依次比较 size，sha1，时间戳
            if f in remote_files:
                remote_file = remote_files[f]
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
                    remote_files.pop(f)
                    continue

                # 跳过对比文件内容
                if ignore_content:
                    self._auth.log.warning(f'忽略文件内容: 不处理 {f}')
                    remote_files.pop(f)
                    continue

                # 获取 f 文件大小
                local_size = os.path.getsize(local_file)
                # 比较大小
                if local_size == remote_file.size:
                    # 计算 f 文件 sha1
                    local_sha1 = self._core_sha1(local_file).lower()
                    # 如果sha1值相同，则跳过
                    if local_sha1 == remote_file.content_hash.lower():
                        self._auth.log.debug(f'文件 {f} 已存在，且sha1值相同，跳过')
                        remote_files.pop(f)
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
                # 在字典中删除remote_file
                remote_files.pop(f)
            else:
                # 不存在则直接上传
                self._auth.log.debug(f'云端不存在，上传本地文件 {f}')
                self.upload_file(file_path=local_file, parent_file_id=remote_folder, name=f,
                                 drive_id=drive_id, check_name_mode='overwrite')
        # 判断是否删除云端文件
        if follow_delete and len(remote_files) != 0:
            self._auth.log.debug(f'删除云端文件 {len(remote_files)} {list(remote_files.keys())}')
            for _ in self._core_batch_move_to_trash(BatchMoveToTrashRequest(
                    drive_id=drive_id, file_id_list=[f.file_id for f in remote_files.values()]
            )):
                pass

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
