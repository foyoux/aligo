"""..."""
import os
import re
from typing import Iterator, List

import requests

from aligo.core import *
from aligo.core.Config import *
from aligo.request import *
from aligo.response import *
from aligo.types import *


class Download(BaseAligo):
    """..."""
    CHUNK_SIZE = 10485760

    def get_download_url(self, body: GetDownloadUrlRequest) -> GetDownloadUrlResponse:
        """..."""
        response = self._post(V2_FILE_GET_DOWNLOAD_URL, body=body)
        return self._result(response, GetDownloadUrlResponse)

    def batch_download_url(self, body: BatchDownloadUrlRequest) -> Iterator[BatchDownloadUrlResponse]:
        """..."""
        if body.drive_id is None:
            body.drive_id = self.default_drive_id

        yield from self.batch_request(BatchRequest(
                requests=[BatchSubRequest(
                    id=file_id,
                    url='/file/get_download_url',
                    body=GetDownloadUrlRequest(
                        drive_id=body.drive_id, file_id=file_id
                    )
                ) for file_id in body.file_id_list]
        ), GetDownloadUrlResponse)

    @staticmethod
    def _del_special_symbol(s: str) -> str:
        """删除Windows文件名中不允许的字符"""
        return re.sub(r'[\\/:*?"<>|]', '_', s)

    def download_file(self, file_path: str, url: str) -> str:
        """下载文件"""
        file_path = os.path.abspath(file_path)
        # 递归创建目录
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        if os.path.exists(file_path):
            self._auth.log.warning(f'文件已存在,跳过下载 {file_path}')
            return file_path

        tmp_file = file_path + '.ali'

        with requests.get(url, headers={
            'referer': 'https://www.aliyundrive.com/'
        }, stream=True) as resp:
            with open(tmp_file, 'wb') as f:
                for chunk in resp.iter_content(chunk_size=int(Download.CHUNK_SIZE)):
                    f.write(chunk)

        os.renames(tmp_file, file_path)
        self._auth.log.info(f'文件下载完成 {file_path}')
        return file_path

    def download_files(self, files: List[BaseFile], local_folder: str = '.') -> List[str]:
        """批量下载文件"""
        rt = []
        for file in files:
            file_name = os.path.join(local_folder, self._del_special_symbol(file.name))
            file_path = self.download_file(file_name, file.download_url)
            rt.append(file_path)
        return rt
