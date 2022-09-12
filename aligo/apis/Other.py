"""Other"""

from aligo.core import *
from aligo.core.Config import *
from aligo.request import *
from aligo.response import *


class Other(Core):
    """Other"""

    def get_path(self, file_id: str, drive_id: str = None) -> GetFilePathResponse:
        """
        官方：获取文件（夹）目录信息
        :param file_id: 文件（夹）ID
        :param drive_id: 文件（夹）所在网盘ID
        :return: [GetFilePathResponse]

        用法示例：
        >>> from aligo import Aligo, BaseFile, GetFilePathResponse
        >>> aligo = Aligo()
        >>> file_path_info = aligo.get_path('60f927edf4c9f64d3a0c4704b80154cfa3d13c2a')
        >>> assert isinstance(file_path_info, GetFilePathResponse)
        >>> for item in file_path_info.items:
        >>>     assert isinstance(item, BaseFile)
        """
        body = GetFilePathRequest(file_id=file_id, drive_id=drive_id)
        return self._core_get_path(body)

    def get_office_preview_url(self, file_id: str, drive_id: str = None):
        response = self._post(V2_FILE_GET_OFFICE_PREVIEW_URL, body={
            'file_id': file_id,
            'drive_id': drive_id
        })
        return self._result(response, GetOfficePreviewUrlResponse)
