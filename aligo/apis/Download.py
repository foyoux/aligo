"""..."""
import os
from typing import List, overload

from aligo.core import *
from aligo.request import *
from aligo.response import *
from aligo.types import *


class Download(Core):
    """..."""

    def get_download_url(self,
                         file_id: str,
                         file_name: str = None,
                         expire_sec: int = 14400,
                         drive_id: str = None,
                         ) -> GetDownloadUrlResponse:
        """获取下载链接"""
        body = GetDownloadUrlRequest(
            file_id=file_id,
            drive_id=drive_id,
            file_name=file_name,
            expire_sec=expire_sec,
        )
        return self._core_get_download_url(body)

    def batch_download_url(self,
                           file_id_list: List[str],
                           expire_sec: int = 14400,
                           drive_id=None) -> List[BatchDownloadUrlResponse]:
        """批量获取下载链接"""
        body = BatchDownloadUrlRequest(
            drive_id=drive_id,
            file_id_list=file_id_list,
            expire_sec=expire_sec
        )
        result = self._core_batch_download_url(body)
        return [i for i in result]

    def download_folder(self, folder_file_id: str, local_folder: str = '.', drive_id: str = None) -> str:
        """下载文件夹, 为解决先下载目标文件夹的问题"""
        if folder_file_id != 'root':
            folder = self._core_get_file(GetFileRequest(file_id=folder_file_id, drive_id=drive_id))
            local_folder = os.path.join(local_folder, self._del_special_symbol(folder.name))
        return self.__download_folder(folder_file_id, local_folder, drive_id)

    def __download_folder(self, folder_file_id: str, local_folder: str = '.', drive_id: str = None) -> str:
        """下载文件夹"""
        # 创建文件夹, 即使文件夹为空
        os.makedirs(local_folder, exist_ok=True)
        files = []
        for file in self._core_get_file_list(GetFileListRequest(parent_file_id=folder_file_id, drive_id=drive_id)):
            if file.type == 'folder':
                self.__download_folder(folder_file_id=file.file_id,
                                       local_folder=os.path.join(local_folder, self._del_special_symbol(file.name)))
                continue
            files.append(file)
        self.download_files(files, local_folder=local_folder)
        return os.path.abspath(local_folder)

    @overload
    def download_file(self, file_path: str, url: str) -> str:
        """..."""

    @overload
    def download_file(self, file_id: str, local_folder: str = '.') -> str:
        """..."""

    @overload
    def download_file(self, file: BaseFile, local_folder: str = '.') -> str:
        """..."""

    def download_file(self, file_path: str = None, url: str = None,
                      local_folder: str = '.', file_id: str = None, file: BaseFile = None, drive_id=None) -> str:
        """..."""
        if file_id:
            file = self._core_get_file(GetFileRequest(file_id=file_id, drive_id=drive_id))

        if file:
            file_path = os.path.join(local_folder, file.name)
            url = file.download_url

        return self._core_download_file(file_path, url)
