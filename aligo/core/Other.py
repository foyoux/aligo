"""..."""

from aligo.core import *
from aligo.request import *
from aligo.response import *


class Other(BaseAligo):
    """..."""

    def get_download_url(self, body: GetDownloadUrlRequest) -> GetDownloadUrlResponse:
        """..."""
        response = self._post(V2_FILE_GET_DOWNLOAD_URL, body=body)
        return self._result(response, GetDownloadUrlResponse)
