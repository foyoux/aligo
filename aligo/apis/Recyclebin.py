"""..."""
from typing import List

from aligo.core import *
from aligo.request import *
from aligo.response import *
from aligo.types import *


class Recyclebin(Core):
    """删除文件太过危险, 只提供移动文件到回收站的功能"""

    def move_file_to_trash(self, file_id: str, drive_id: str = None) -> MoveFileToTrashResponse:
        """移动文件到回收站"""
        body = MoveFileToTrashRequest(file_id=file_id, drive_id=drive_id)
        return self._core_move_file_to_trash(body)

    def batch_move_to_trash(self, file_id_list: List[str], drive_id: str = None) -> List[BatchSubResponse]:
        """批量移动到回收站"""
        body = BatchMoveToTrashRequest(drive_id=drive_id, file_id_list=file_id_list)
        result = self._core_batch_move_to_trash(body)
        return [i for i in result]

    def restore_file(self, file_id: str, drive_id: str = None) -> RestoreFileResponse:
        """恢复文件"""
        body = RestoreFileRequest(drive_id=drive_id, file_id=file_id)
        return self._core_restore_file(body)

    def batch_restore_files(self, file_id_list: List[str], drive_id: str = None) -> List[BatchSubResponse]:
        """批量恢复文件"""
        body = BatchRestoreRequest(drive_id=drive_id, file_id_list=file_id_list)
        result = self._core_batch_restore_files(body)
        return [i for i in result]

    def get_recyclebin_list(self, body: GetRecycleBinListRequest = None, **kwargs) -> List[BaseFile]:
        """获取回收站文件列表"""
        if body is None:
            body = GetRecycleBinListRequest(**kwargs)
        result = self._core_get_recyclebin_list(body)
        return [i for i in result]
