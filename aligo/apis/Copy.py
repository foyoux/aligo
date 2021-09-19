"""..."""
from typing import List

from aligo.core import *
from aligo.request import *
from aligo.response import *


class Copy(Core):
    """..."""

    def copy_file(self, file_id: str = None,
                  to_parent_file_id: str = 'root',
                  new_name: str = None,
                  drive_id: str = None,
                  to_drive_id: str = None,
                  body: CopyFileRequest = None,
                  **kwargs) -> CopyFileResponse:
        """复制文件"""
        if body is None:
            body = CopyFileRequest(
                file_id=file_id,
                drive_id=drive_id,
                to_drive_id=to_drive_id,
                to_parent_file_id=to_parent_file_id,
                new_name=new_name,
                **kwargs
            )
        return self._core_copy_file(body)

    def batch_copy_files(self,
                         file_id_list: List[str] = None,
                         to_parent_file_id: str = 'root',
                         drive_id: str = None,
                         body: BatchCopyFilesRequest = None,
                         **kwargs) -> List[BatchSubResponse]:
        """批量复制"""
        if body is None:
            body = BatchCopyFilesRequest(drive_id=drive_id,
                                         file_id_list=file_id_list,
                                         to_parent_file_id=to_parent_file_id,
                                         **kwargs)
        result = self._core_batch_copy_files(body)
        return [i for i in result]
