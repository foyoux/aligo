"""..."""
from typing import Iterator

import requests

from aligo.core import *
from aligo.request import *
from aligo.response import *
from aligo.types import *


class Download(BaseAligo):
    """..."""
    MAX_DOWNLOAD_URL = 100
    CHUNK_SIZE = 10485760

    def get_download_url(self, body: GetDownloadUrlRequest) -> GetDownloadUrlResponse:
        """..."""
        response = self._post(V2_FILE_GET_DOWNLOAD_URL, body=body)
        return self._result(response, GetDownloadUrlResponse)

    def batch_download_url(self, body: BatchDownloadUrlRequest) -> Iterator[BatchDownloadUrlResponse]:
        """..."""
        if body.drive_id is None:
            body.drive_id = self.default_drive_id

        for file_id_list in self._list_split(body.file_id_list, self.MAX_DOWNLOAD_URL):
            response = self._post(V2_BATCH, body={
                "requests": [
                    {
                        "body": {
                            "drive_id": body.drive_id,
                            "file_id": file_id,
                            "expire_sec": body.expire_sec
                        },
                        "headers": {"Content-Type": "application/json"},
                        "id": file_id,
                        "method": "POST",
                        "url": "/file/get_download_url"
                    } for file_id in file_id_list
                ],
                "resource": "file"
            })

            if response.status_code != 200:
                yield Null(response)
                return

            for batch in response.json()['responses']:
                yield BatchDownloadUrlResponse(**batch)

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
