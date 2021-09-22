"""Other"""

from aligo.core import *
from aligo.request import *
from aligo.response import *


class Other(Core):
    """Other"""

    def get_path(self, file_id: str, drive_id: str = None) -> GetFilePathResponse:
        """get_path: 获取文件的父级目录信息"""
        body = GetFilePathRequest(file_id=file_id, drive_id=drive_id)
        return self._core_get_path(body)
