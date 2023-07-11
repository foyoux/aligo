"""..."""
import os
import re
from typing import Iterator, List

from tqdm import tqdm

from aligo.core import *
from aligo.core.Config import *
from aligo.request import *
from aligo.response import *
from aligo.types import *


class Download(BaseAligo):
    """..."""
    _DOWNLOAD_CHUNK_SIZE = 8388608  # 8 MB

    def _core_get_download_url(self, body: GetDownloadUrlRequest) -> GetDownloadUrlResponse:
        """..."""
        response = self._post(V2_FILE_GET_DOWNLOAD_URL, body=body)
        return self._result(response, GetDownloadUrlResponse)

    def _core_batch_download_url(self, body: BatchDownloadUrlRequest) -> Iterator[BatchDownloadUrlResponse]:
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

    def _core_download_file(self, file_path: str, url: str) -> str:
        """下载文件

        :param file_path: 下载到哪里, 比如: 123.jpg, ./123.jpg, D:\123.jpg
        :param url: 下载地址
        :return: 下载完成保存文件的本地路径
        """
        file_dir, file_name = os.path.split(os.path.abspath(file_path))
        file_name = self._del_special_symbol(file_name)
        file_path = os.path.join(file_dir, file_name)

        # url 为空判断
        if not url:
            self._auth.log.error(f'文件 {file_path} 下载失败: 获取的url为空, 文件可能被屏蔽导致无法下载')
            return file_path

        self._auth.log.info(f'开始下载文件 {file_path}')

        if os.path.exists(file_path) and not os.path.exists(f'{file_path}.aria2'):
            self._auth.log.warning(f'文件已存在,跳过下载 {file_path}')
            return file_path

        if self._has_aria2c:
            cmd = ' '.join([
                f'aria2c "{url}"',
                f'--referer=https://www.aliyundrive.com/',
                f'-d "{file_dir}"',
                f'-o "{file_name}"'
                f'-x 16',
                f'-s 8',
            ])
            # print(cmd)
            os.system(cmd)
            return file_path

        # 递归创建目录
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        tmp_file = file_path + '.ali'

        tmp_size = 0
        if os.path.exists(tmp_file):
            tmp_size = os.path.getsize(tmp_file)

        try:
            progress_bar = None
            # noinspection PyProtectedMember
            with self._session.get(url, headers={
                'Range': f'bytes={tmp_size}-',
                'Referer': 'https://www.aliyundrive.com/',
            }, stream=True) as resp:
                total_size = int(resp.headers.get('content-length', 0))
                accept_range = resp.headers.get('Accept-Ranges', None)
                if accept_range == 'bytes':
                    progress_bar = tqdm(total=total_size + tmp_size, unit='B', unit_scale=True, colour='#31a8ff')
                    progress_bar.update(tmp_size)
                    with open(tmp_file, 'ab') as f:
                        for content in resp.iter_content(chunk_size=Download._DOWNLOAD_CHUNK_SIZE):
                            progress_bar.update(len(content))
                            f.write(content)
                else:
                    self._auth.log.warning(f'不支持断点续传 {file_path}')
                    progress_bar = tqdm(total=total_size, unit='B', unit_scale=True, colour='#31a8ff')
                    with open(tmp_file, 'wb') as f:
                        for content in resp.iter_content(chunk_size=Download._DOWNLOAD_CHUNK_SIZE):
                            progress_bar.update(len(content))
                            f.write(content)
            os.renames(tmp_file, file_path)
        finally:
            if progress_bar:
                progress_bar.close()

        self._auth.log.info(f'文件下载完成 {file_path}')
        return file_path

    def download_files(self, files: List[BaseFile], local_folder: str = '.') -> List[str]:
        """批量下载文件

        :param files: BaseFile 对象列表, 或者包含 name 和  download_url 属性的对象
        :param local_folder: 目标文件夹, 表示要下载到哪个文件夹
        :return: 返回下载完成后的本地文件路径列表

        :Example:
        >>> from aligo import Aligo
        >>> ali = Aligo()
        >>> # noinspection PyShadowingNames
        >>> file_path = ali.download_files([ali.get_file_by_path('xxx.mp3')])
        >>> print(file_path)
        """
        rt = []
        for file in files:
            file_path = os.path.join(local_folder, file.name)
            file_path = self._core_download_file(file_path, file.download_url or file.url)
            rt.append(file_path)
        return rt
