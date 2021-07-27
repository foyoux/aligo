"""..."""
from typing import Iterator

from aligo.core import *
from aligo.request import *
from aligo.response import *
from aligo.types import *


class Move(BaseAligo):
    """..."""
    MAX_MOVE_COUNT = 100

    def move_file(self, body: MoveFileRequest) -> MoveFileResponse:
        """..."""
        response = self._post(V2_FILE_MOVE, body=body)
        return self._result(response, MoveFileResponse)

    def batch_move_files(self, body: BatchMoveFilesRequest) -> Iterator[BatchResponse]:
        """..."""

        if body.drive_id is None:
            body.drive_id = self.default_drive_id

        for file_id_list in self._list_split(body.file_id_list, self.MAX_MOVE_COUNT):
            response = self._post(V2_BATCH, body={
                "requests": [
                    {
                        "body": {
                            "drive_id": body.drive_id,
                            "file_id": file_id,
                            "to_parent_file_id": body.to_parent_file_id,
                            "overwrite": body.overwrite,
                            "auto_rename": body.auto_rename
                        },
                        "headers": {"Content-Type": "application/json"},
                        "id": file_id,
                        "method": "POST",
                        "url": "/file/move"
                    } for file_id in file_id_list
                ],
                "resource": "file"
            })

            if response.status_code != 200:
                yield Null(response)
                return

            for batch in response.json()['responses']:
                yield BatchResponse(**batch)

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
