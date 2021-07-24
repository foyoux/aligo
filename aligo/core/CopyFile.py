"""..."""

from aligo.config import *
from aligo.core import *
from aligo.request import *
from aligo.response import *


class CopyFile(BaseAligo):
    """..."""

    def copy_file(self, body: CopyFileRequest) -> CopyFileResponse:
        """..."""
        response = self._post(V2_FILE_COPY, body=body)
        return self._result(response, CopyFileResponse, [201, 202])

    # @overload
    # def copy_file(self, body: CopyFileRequest) -> CopyFileResponse:
    #     """..."""
    #     ...
    #
    # @overload
    # def copy_file(self, file_id: str,
    #               to_parent_file_id: str = 'root',
    #               drive_id: str = None,
    #               to_drive_id: str = None, ) -> CopyFileResponse:
    #     """..."""
    #     ...
    #
    # def copy_file(
    #         self,
    #         body: CopyFileRequest = None,
    #         file_id: str = None,
    #         to_parent_file_id: str = 'root',
    #         drive_id: str = None,
    #         to_drive_id: str = None,
    # ) -> CopyFileResponse:
    #     """..."""
    #     # CopyFileRequest的to_parent_file_id已具有'root'默认值
    #     # if body.to_parent_file_id is None:
    #     #     body.to_parent_file_id = 'root'
    #     if body is None:
    #         body = CopyFileRequest(
    #             file_id=file_id,
    #             to_parent_file_id=to_parent_file_id,
    #             drive_id=drive_id,
    #             to_drive_id=to_drive_id
    #         )
    #     if body.drive_id is None:
    #         body.drive_id = self.default_drive_id
    #     if body.to_drive_id is None:
    #         body.to_drive_id = self.default_drive_id
    #     response = self._post(V2_FILE_COPY, body=body)
    #     return self._result(response, CopyFileResponse, 202)
