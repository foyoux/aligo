"""..."""
from typing import List

from aligo.core import *
from aligo.request import *
from aligo.response import *


class Download(Core):
    """..."""

    def get_download_url(self,
                         file_id,
                         drive_id=None,
                         file_name=None,
                         expire_sec: int = 14400,
                         ) -> GetDownloadUrlResponse:
        """..."""
        body = GetDownloadUrlRequest(
            file_id=file_id,
            drive_id=drive_id,
            file_name=file_name,
            expire_sec=expire_sec,
        )
        return super(Download, self).get_download_url(body)

    def batch_download_url(self,
                           file_id_list: List[str],
                           drive_id=None,
                           expire_sec: int = 14400) -> List[BatchDownloadUrlResponse]:
        """..."""
        body = BatchDownloadUrlRequest(
            drive_id=drive_id,
            file_id_list=file_id_list,
            expire_sec=expire_sec
        )
        result = super(Download, self).batch_download_url(body)
        return [i for i in result]
