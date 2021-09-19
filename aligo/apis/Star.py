"""收藏相关"""
from typing import List

from aligo.core import *
from aligo.request import *
from aligo.response import *
from aligo.types import *


class Star(Core):
    """..."""
    _MAX_STAR_COUNT: int = 500

    def starred_file(self,
                     file_id: str,
                     starred: bool = True,
                     drive_id: str = None) -> BaseFile:
        """收藏(或取消) 文件"""
        body = StarredFileRequest(
            file_id=file_id,
            starred=starred,
            drive_id=drive_id,
        )
        return self._core_starred_file(body)

    def batch_star_files(self,
                         file_id_list: List[str],
                         starred: bool = True,
                         drive_id: str = None) -> List[BatchSubResponse]:
        """批量收藏文件"""
        body = BatchStarFilesRequest(
            drive_id=drive_id,
            file_id_list=file_id_list,
            starred=starred,
        )
        result = self._core_batch_star_files(body)
        return [i for i in result]

    def get_starred_list(self, body: GetStarredListRequest = None, **kwargs) -> List[BaseFile]:
        """收藏(或取消) 文件列表"""
        if body is None:
            body = GetStarredListRequest(**kwargs)
        result = self._core_get_starred_list(body)
        return [i for i in result]
