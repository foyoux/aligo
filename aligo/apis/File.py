"""文件相关"""
from typing import List

from aligo.core import *
from aligo.request import *
from aligo.response import *
from aligo.types import *


class File(Core):
    """..."""

    def get_file(self,
                 file_id: str,
                 drive_id: str = None,
                 body: GetFileRequest = None,
                 **kwargs) -> BaseFile:
        """获取文件信息, 其他类中可能会用到, 所以放到基类中"""
        if body is None:
            body = GetFileRequest(
                file_id=file_id, drive_id=drive_id,
                **kwargs
            )
        return super(File, self).get_file(body)

    def get_file_list(self, parent_file_id: str = 'root', drive_id: str = None, body: GetFileListRequest = None,
                      **kwargs) -> List[BaseFile]:
        """获取文件列表"""
        if body is None:
            body = GetFileListRequest(drive_id=drive_id, parent_file_id=parent_file_id, **kwargs)
        result = super(File, self).get_file_list(body)
        return [i for i in result]

    def batch_get_files(self, file_id_list: List[str], drive_id: str = None) -> List[BatchSubResponse]:
        """..."""
        body = BatchGetFileRequest(file_id_list=file_id_list, drive_id=drive_id)
        result = super(File, self).batch_get_files(body)
        return [i for i in result]
