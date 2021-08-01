"""创建上传相关"""
import os
from typing import List

from aligo.core import *
from aligo.request import *
from aligo.response import *
from aligo.types import *
from aligo.types.Enum import *


class Create(Core):
    """..."""

    def create_folder(self,
                      name: str,
                      parent_file_id: str = 'root',
                      drive_id: str = None,
                      check_name_mode: CheckNameMode = 'auto_rename') -> CreateFileResponse:
        """创建文件夹"""
        body = CreateFolderRequest(
            name=name,
            parent_file_id=parent_file_id,
            drive_id=drive_id,
            check_name_mode=check_name_mode,
        )
        return super(Create, self).create_folder(body)

    def upload_files(self, file_paths: List[str], parent_file_id: str = 'root', drive_id: str = None,
                     check_name_mode: CheckNameMode = "auto_rename") -> List[BaseFile]:
        """..."""
        file_list = []
        for file_path in file_paths:
            file = self.upload_file(file_path=file_path, parent_file_id=parent_file_id, drive_id=drive_id,
                                    check_name_mode=check_name_mode)
            file_list.append(file)
        return file_list

    def upload_folder(self, folder_path: str, parent_file_id: str = 'root', drive_id: str = None,
                      check_name_mode: CheckNameMode = "auto_rename") -> List:
        """上传本地文件夹"""
        result = []
        # 1. 获取文件夹名
        folder_name = os.path.basename(folder_path)
        # 2. 在指定 parent_file_id 下创建 folder_name 文件夹, 并获取 folder BaseFile 对象
        folder = self.create_folder(folder_name, parent_file_id=parent_file_id, drive_id=drive_id,
                                    check_name_mode=check_name_mode)
        # 3. 开始扫描目标文件夹
        file: os.DirEntry
        for file in os.scandir(folder_path):
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
