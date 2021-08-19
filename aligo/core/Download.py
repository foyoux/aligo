"""..."""
import os
import re
from typing import Iterator, List

import requests
from tqdm import tqdm

from aligo.core import *
from aligo.core.Config import *
from aligo.request import *
from aligo.response import *
from aligo.types import *


class Download(BaseAligo):
    """..."""
    DOWNLOAD_CHUNK_SIZE = 8388608

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
        """下载文件

        :param file_path: 下载到哪里, 比如: 123.jpg, ./123.jpg, D:\123.jpg
        :param url: 下载地址
        :return: 下载完成保存文件的本地路径
        """
        file_dir, file_name = os.path.split(file_path)
        file_name = self._del_special_symbol(file_name)
        file_path = os.path.abspath(os.path.join(file_dir, file_name))

        # 递归创建目录
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        if os.path.exists(file_path):
            self._auth.log.warning(f'文件已存在,跳过下载 {file_path}')
            return file_path

        tmp_file = file_path + '.ali'

        self._auth.log.info(f'开始下载文件 {file_path}')

        with requests.get(url, headers={
            'referer': 'https://www.aliyundrive.com/'
        }, stream=True) as resp:
            llen = int(resp.headers.get('content-length', 0))
            progress_bar = tqdm(total=llen, unit='B', unit_scale=True, colour='#31a8ff')
            with open(tmp_file, 'wb') as f:
                for content in resp.iter_content(chunk_size=Download.DOWNLOAD_CHUNK_SIZE):
                    progress_bar.update(len(content))
                    f.write(content)

        os.renames(tmp_file, file_path)

        progress_bar.close()

        self._auth.log.info(f'文件下载完成 {file_path}')
        return file_path

    def download_files(self, files: List[BaseFile], local_folder: str = '.') -> List[str]:
        """批量下载文件

        :param files: BaseFile 对象列表, 或者包含 name 和  download_url 属性的对象
        :param local_folder: 目标文件夹, 表示要下载到哪个文件夹
        :return: 返回下载完成后的本地文件路径列表
        """
        rt = []
        for file in files:
            file_path = os.path.join(local_folder, file.name)
            file_path = self.download_file(file_path, file.download_url)
            rt.append(file_path)
        return rt
