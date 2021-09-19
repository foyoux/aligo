"""..."""
from typing import Iterator

from aligo.core import *
from aligo.core.Config import *
from aligo.request import *
from aligo.response import *
from aligo.types import *


class Recyclebin(BaseAligo):
    """删除文件太过危险, 只提供移动文件到回收站的功能"""

    def _core_move_file_to_trash(self, body: MoveFileToTrashRequest) -> MoveFileToTrashResponse:
        """移动文件到回收站"""
        response = self._post(V2_RECYCLEBIN_TRASH, body=body)
        return self._result(response, MoveFileToTrashResponse, [202, 204])

    def _core_batch_move_to_trash(self, body: BatchMoveToTrashRequest) -> Iterator[BatchSubResponse]:
        """..."""
        if body.drive_id is None:
            body.drive_id = self.default_drive_id

        yield from self.batch_request(BatchRequest(
            requests=[BatchSubRequest(
                id=file_id,
                url='/recyclebin/trash',
                body=MoveFileToTrashRequest(
                    drive_id=body.drive_id, file_id=file_id
                )
            ) for file_id in body.file_id_list]
        ), MoveFileToTrashResponse)

    def _core_restore_file(self, body: RestoreFileRequest) -> RestoreFileResponse:
        """恢复文件"""
        response = self._post(V2_RECYCLEBIN_RESTORE, body=body)
        return self._result(response, RestoreFileResponse, 204)

    def _core_batch_restore_files(self, body: BatchRestoreRequest) -> Iterator[BatchSubResponse]:
        """..."""
        if body.drive_id is None:
            body.drive_id = self.default_drive_id

        yield from self.batch_request(BatchRequest(
            requests=[BatchSubRequest(
                id=file_id,
                url='/recyclebin/restore',
                body=RestoreFileRequest(
                    drive_id=body.drive_id, file_id=file_id
                )
            ) for file_id in body.file_id_list]
        ), RestoreFileResponse)

    def _core_get_recyclebin_list(self, body: GetRecycleBinListRequest) -> Iterator[BaseFile]:
        """获取回收站文件列表"""
        yield from self._list_file(V2_RECYCLEBIN_LIST, body, GetRecycleBinListResponse)
