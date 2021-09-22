"""Other"""

from aligo.request import GetFilePathRequest
from aligo.response import GetFilePathResponse
from .BaseAligo import BaseAligo
from .Config import *


class Other(BaseAligo):
    """Other"""

    def _core_get_path(self, body: GetFilePathRequest) -> GetFilePathResponse:
        """get_path 获取当前文件的路径, 父级目录"""
        response = self._post(ADRIVE_V1_FILE_GET_PATH, body=body)
        return self._result(response, GetFilePathResponse)
