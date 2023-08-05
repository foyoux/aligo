"""..."""
from typing import Iterator

from aligo.core import BaseAligo
from aligo.core.Config import V2_FILE_MOVE
from aligo.request import BatchMoveFilesRequest, MoveFileRequest, BatchRequest, BatchSubRequest
from aligo.response import BatchSubResponse, MoveFileResponse


class Move(BaseAligo):
    """..."""

    def _core_move_file(self, body: MoveFileRequest) -> MoveFileResponse:
        """..."""
        response = self.post(V2_FILE_MOVE, body=body)
        return self._result(response, MoveFileResponse)

    def _core_batch_move_files(self, body: BatchMoveFilesRequest) -> Iterator[BatchSubResponse[MoveFileResponse]]:
        """..."""
        if body.drive_id is None:
            body.drive_id = self.default_drive_id

        yield from self.batch_request(BatchRequest(
            requests=[BatchSubRequest(
                id=file_id,
                url='/file/move',
                body=MoveFileRequest(
                    drive_id=body.drive_id, file_id=file_id,
                    to_parent_file_id=body.to_parent_file_id,
                    overwrite=body.overwrite, auto_rename=body.auto_rename
                )
            ) for file_id in body.file_id_list]
        ), MoveFileResponse)
