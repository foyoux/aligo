"""文件相关"""
import os
from typing import List, Union

from aligo.core import *
from aligo.request import *
from aligo.response import *
from aligo.types import *
from aligo.types.Enum import *


class File(Core):
    """..."""

    def get_file(self,
                 file_id: str,
                 drive_id: str = None,
                 body: GetFileRequest = None,
                 **kwargs) -> BaseFile:
        """获取文件信息, 其他类中可能会用到, 所以放到基类中"""
        if body is None:
            body = GetFileRequest(
                file_id=file_id, drive_id=drive_id,
                **kwargs
            )
        return self._core_get_file(body)

    def get_file_list(self, parent_file_id: str = 'root', drive_id: str = None, body: GetFileListRequest = None,
                      **kwargs) -> List[BaseFile]:
        """获取文件列表"""
        if body is None:
            body = GetFileListRequest(drive_id=drive_id, parent_file_id=parent_file_id, **kwargs)
        result = self._core_get_file_list(body)
        return [i for i in result]

    def batch_get_files(self, file_id_list: List[str], drive_id: str = None) -> List[BatchSubResponse]:
        """..."""
        body = BatchGetFileRequest(file_id_list=file_id_list, drive_id=drive_id)
        result = self._core_batch_get_files(body)
        return [i for i in result]

    def get_folder_by_path(self, path: str = '/', parent_file_id: str = 'root',
                           check_name_mode: CheckNameMode = 'refuse', drive_id: str = None
                           ) -> Union[BaseFile, CreateFileResponse]:
        """根据路径字符串获取或创建文件夹"""
        path = path.strip('/')
        if path == '':
            return self.get_file(file_id=parent_file_id, drive_id=drive_id)
        folder = None
        for name in path.split('/'):
            folder = self._core_create_folder(CreateFolderRequest(
                name=name, parent_file_id=parent_file_id, check_name_mode=check_name_mode, drive_id=drive_id
            ))
            parent_file_id = folder.file_id
        return folder

    def get_file_by_path(self, path: str = '/', parent_file_id: str = 'root',
                         check_name_mode: CheckNameMode = 'refuse',
                         drive_id: str = None) -> Union[BaseFile, CreateFileResponse]:
        """根据路径字符串获取文件或文件夹, 优先获取文件, 文件夹不存在则创建"""
        path = path.strip('/')
        folder_path, file_name = os.path.split(path)
        if folder_path != '':
            parent_file_id = self.get_folder_by_path(folder_path, parent_file_id=parent_file_id,
                                                     check_name_mode=check_name_mode, drive_id=drive_id).file_id
        if file_name == '':
            return self.get_file(file_id=parent_file_id, drive_id=drive_id)

        file_list = self._core_get_file_list(
            GetFileListRequest(parent_file_id=parent_file_id, drive_id=drive_id)
        )

        for file in file_list:
            if file_name == file.name:
                return file

        return self._core_create_folder(CreateFolderRequest(
            name=file_name, parent_file_id=parent_file_id, check_name_mode=check_name_mode, drive_id=drive_id
        ))
