"""..."""
from typing import Iterator

from aligo.core import BaseAligo
from aligo.core.Config import V2_FILE_COPY
from aligo.request import BatchCopyFilesRequest, CopyFileRequest, BatchRequest, BatchSubRequest
from aligo.response import BatchSubResponse, CopyFileResponse


class Copy(BaseAligo):
    """..."""

    def _core_copy_file(self, body: CopyFileRequest) -> CopyFileResponse:
        """..."""
        response = self.post(V2_FILE_COPY, body=body)
        return self._result(response, CopyFileResponse, [201, 202])

    def _core_batch_copy_files(self, body: BatchCopyFilesRequest) -> Iterator[BatchSubResponse[CopyFileResponse]]:
        """..."""
        if body.drive_id is None:
            body.drive_id = self.default_drive_id

        yield from self.batch_request(BatchRequest(
            requests=[BatchSubRequest(
                id=file_id,
                url='/file/copy',
                body=CopyFileRequest(
                    drive_id=body.drive_id, file_id=file_id,
                    to_parent_file_id=body.to_parent_file_id,
                    overwrite=body.overwrite, auto_rename=body.auto_rename
                )
            ) for file_id in body.file_id_list]
        ), CopyFileResponse)
