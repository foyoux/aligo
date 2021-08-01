"""文件相关"""
from typing import List

from aligo.core import *
from aligo.request import *
from aligo.types import *


class File(Core):
    """..."""

    def get_file_list(self, parent_file_id: str = 'root', drive_id: str = None, body: GetFileListRequest = None,
                      **kwargs) -> List[BaseFile]:
        """获取文件列表"""
        if body is None:
            body = GetFileListRequest(drive_id=drive_id, parent_file_id=parent_file_id, **kwargs)
        result = super(File, self).get_file_list(body)
        return [i for i in result]
