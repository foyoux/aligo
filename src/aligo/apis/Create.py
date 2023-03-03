"""Create class"""
import os
from typing import List, Callable

from aligo.core import *
from aligo.request import *
from aligo.response import *
from aligo.types import *
from aligo.types.Enum import *


class Create(Core):
    """创建上传文件相关"""

    def create_folder(self,
                      name: str,
                      parent_file_id: str = 'root',
                      drive_id: str = None,
                      check_name_mode: CheckNameMode = 'auto_rename') -> CreateFileResponse:
        """
        创建文件夹
        :param name: [str] 文件夹名
        :param parent_file_id: Optional[str] 父文件夹id, 默认为 'root'
        :param drive_id: Optional[str] 指定网盘id, 默认为 None
        :param check_name_mode: Optional[CheckNameMode] 检查文件名模式, 默认为 'auto_rename'
        :return: [CreateFileResponse]

        用法示例:
        >>> from aligo import Aligo
        >>> ali = Aligo()
        >>> result = ali.create_folder(name='test')
        >>> print(result)
        """
        body = CreateFolderRequest(
            name=name,
            parent_file_id=parent_file_id,
            drive_id=drive_id,
            check_name_mode=check_name_mode,
        )
        return self._core_create_folder(body)

    def upload_files(self, file_paths: List[str], parent_file_id: str = 'root', drive_id: str = None,
                     check_name_mode: CheckNameMode = "auto_rename") -> List[BaseFile]:
        """
        批量上传文件
        :param file_paths: [List[str]] 文件路径列表
        :param parent_file_id: Optional[str] 父文件夹id, 默认为 'root'
        :param drive_id: Optional[str] 指定网盘id, 默认为 None
        :param check_name_mode: Optional[CheckNameMode] 检查文件名模式, 默认为 'auto_rename'
        :return: [List[BaseFile]]

        用法示例:
        >>> from aligo import Aligo
        >>> ali = Aligo()
        >>> result = ali.upload_files(file_paths=['/Users/aligo/Desktop/test1.txt', '/Users/aligo/Desktop/test2.txt'])
        >>> print(result)
        """
        file_list = []
        for file_path in file_paths:
            file = self.upload_file(file_path=file_path, parent_file_id=parent_file_id, drive_id=drive_id,
                                    check_name_mode=check_name_mode)
            file_list.append(file)
        return file_list

    def upload_folder(self, folder_path: str, parent_file_id: str = 'root', drive_id: str = None,
                      check_name_mode: CheckNameMode = "auto_rename", folder_check_name_mode: CheckNameMode = 'refuse',
                      file_filter: Callable[[os.DirEntry], bool] = lambda x: False) -> List:
        """
        上传文件夹
        :param folder_path: [str] 文件夹路径
        :param parent_file_id: Optional[str] 父文件夹id, 默认为 'root'
        :param drive_id: [str] 指定网盘id, 默认为 None, 如果为 None, 则使用默认网盘
        :param check_name_mode: [CheckNameMode] 检查文件名模式, 默认为 'auto_rename'
        :param folder_check_name_mode: [CheckNameMode] 检查文件夹名模式, 默认为 'refuse'
        :param file_filter: 文件过滤函数
        :return: [List]

        用法示例:
        >>> from aligo import Aligo
        >>> ali = Aligo()
        >>> # noinspection PyShadowingNames
        >>> result = ali.upload_folder('/Users/aligo/Desktop/test')
        >>> print(result)
        """
        result = []
        folder_path = os.path.abspath(folder_path)

        # 0. 判断是否为文件夹
        if not os.path.isdir(folder_path):
            raise NotADirectoryError('不是文件夹')

        # 1. 获取文件夹名
        # 防止文件夹末尾存在分隔符时, 返回为空 "" 的情况
        folder_name = os.path.basename(folder_path)
        # 2. 在指定 parent_file_id 下创建 folder_name 文件夹, 并获取 folder BaseFile 对象
        folder = self.create_folder(folder_name, parent_file_id=parent_file_id, drive_id=drive_id,
                                    check_name_mode=folder_check_name_mode)
        # 3. 开始扫描目标文件夹
        file: os.DirEntry
        for file in os.scandir(folder_path):
            if file_filter(file):
                continue
            if file.is_file():
                # 4. 如果是文件, 就上传, 并继续
                x = self.upload_file(file.path, parent_file_id=folder.file_id, name=file.name, drive_id=drive_id,
                                     check_name_mode=check_name_mode)
                result.append(x)
                continue
            # 5. 否则为文件夹, 递归
            x = self.upload_folder(folder_path=file.path, parent_file_id=folder.file_id, drive_id=drive_id,
                                   check_name_mode=check_name_mode)
            result.append({file.name: x})
        return result
