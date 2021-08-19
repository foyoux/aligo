"""..."""
import os
from typing import List, overload

from aligo.core import *
from aligo.core.File import File
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
        return super(Download, self).get_download_url(body)

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
        result = super(Download, self).batch_download_url(body)
        return [i for i in result]

    def download_folder(self, folder_file_id: str, local_folder: str = '.', drive_id: str = None) -> str:
        """下载文件夹"""
        files = []
        for file in File.get_file_list(self, GetFileListRequest(parent_file_id=folder_file_id, drive_id=drive_id)):
            if file.type == 'folder':
                self.download_folder(folder_file_id=file.file_id,
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
            # file = self.get_download_url(file_id, drive_id)
            # url = file.url
            # file_name = parse.parse_qs(url).get('response-content-disposition')[0]
            # file_name = file_name.split("''")[1]
            # file_name = parse.unquote_plus(file_name)
            # file_path = os.path.join(local_folder, file_name)
            file = File.get_file(self, GetFileRequest(file_id=file_id, drive_id=drive_id))

        if file:
            file_path = os.path.join(local_folder, file.name)
            url = file.download_url

        return super(Download, self).download_file(file_path, url)
