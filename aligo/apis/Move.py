"""..."""
from typing import List

from aligo.core import *
from aligo.request import *
from aligo.response import *


class Move(Core):
    """..."""

    def move_file(self, file_id: str = None,
                  to_parent_file_id: str = 'root',
                  new_name: str = None,
                  drive_id: str = None,
                  to_drive_id: str = None,
                  body: MoveFileRequest = None,
                  **kwargs) -> MoveFileResponse:
        """移动文件"""
        if body is None:
            body = MoveFileRequest(
                file_id=file_id,
                drive_id=drive_id,
                to_drive_id=to_drive_id,
                to_parent_file_id=to_parent_file_id,
                new_name=new_name,
                **kwargs
            )
        return super(Move, self).move_file(body)

    def batch_move_files(self,
                         file_id_list: List[str] = None,
                         to_parent_file_id: str = 'root',
                         drive_id: str = None,
                         body: BatchMoveFilesRequest = None,
                         **kwargs) -> List[BatchSubResponse]:
        """批量移动"""
        if body is None:
            body = BatchMoveFilesRequest(drive_id=drive_id,
                                         file_id_list=file_id_list,
                                         to_parent_file_id=to_parent_file_id)
        result = super(Move, self).batch_move_files(body)
        return [i for i in result]
