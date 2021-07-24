"""..."""

from aligo.config import *
from aligo.core import *
from aligo.request import *
from aligo.response import *


class MoveFile(BaseAligo):
    """..."""

    def move_file(self, body: MoveFileRequest) -> MoveFileResponse:
        """..."""
        response = self._post(V2_FILE_MOVE, body=body)
        return self._result(response, MoveFileResponse)

    # @overload
    # def move_file(self, body: MoveFileRequest) -> MoveFileResponse:
    #     """..."""
    #     ...
    #
    # @overload
    # def move_file(self, src: BaseFile, dest: BaseFile = None) -> MoveFileResponse:
    #     """..."""
    #     ...
    #
    # @overload
    # def move_file(
    #         self,
    #         file_id: str,
    #         to_parent_file_id: str = 'root',
    #         drive_id: str = None,
    #         to_drive_id: str = None
    # ) -> MoveFileResponse:
    #     """..."""
    #     ...
    #
    # def move_file(
    #         self,
    #         body: MoveFileRequest = None,
    #         src: BaseFile = None,
    #         dest: BaseFile = None,
    #         file_id: str = None,
    #         to_parent_file_id: str = 'root',
    #         drive_id: str = None,
    #         to_drive_id: str = None
    # ) -> MoveFileResponse:
    #     """..."""
    #     if body is None:
    #         if src is None:
    #             body = MoveFileRequest(
    #                 file_id=file_id,
    #                 to_parent_file_id=to_parent_file_id,
    #                 drive_id=drive_id,
    #                 to_drive_id=to_drive_id
    #             )
    #         else:
    #             if dest is None:
    #                 dest = BaseFile(file_id='root', drive_id=self.default_drive_id)
    #             body = MoveFileRequest(
    #                 file_id=src.file_id,
    #                 drive_id=src.drive_id,
    #                 to_parent_file_id=dest.file_id,
    #                 to_drive_id=dest.drive_id
    #             )
    #
    #     if body.drive_id is None:
    #         body.drive_id = self.default_drive_id
    #     if body.to_drive_id is None:
    #         body.to_drive_id = self.default_drive_id
    #     response = self._post(V2_FILE_MOVE, body=body)
    #     return self._result(response, MoveFileResponse)
