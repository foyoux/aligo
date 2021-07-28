"""..."""
from typing import Iterator

import requests

from aligo.core import *
from aligo.request import *
from aligo.response import *


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

        for i in self.batch_request(BatchRequest(
                requests=[BatchSubRequest(
                    id=file_id,
                    url='/file/get_download_url',
                    body=GetDownloadUrlRequest(
                        drive_id=body.drive_id, file_id=file_id
                    )
                ) for file_id in body.file_id_list]
        ), GetDownloadUrlResponse):
            yield i

    @staticmethod
    def download_file(file_path: str, url: str):
        """..."""
        with requests.get(url, headers={
            'referer': 'https://www.aliyundrive.com/'
        }, stream=True) as resp:
            with open(file_path, 'wb') as f:
                for chunk in resp.iter_content(chunk_size=int(Download.CHUNK_SIZE)):
                    f.write(chunk)
        return file_path
