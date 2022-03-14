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
        """
        官方：收藏(或取消) 文件
        :param file_id: [必须] 文件ID
        :param starred: [必须] 是否收藏
        :param drive_id: [可选] 文件所在的网盘ID
        :return: [BaseFile] 文件信息

        用法示例：
        >>> from aligo import Aligo
        >>> ali = Aligo()
        >>> star_file = ali.starred_file('file_id')
        >>> print(star_file.name)
        """
        body = StarredFileRequest(
            file_id=file_id,
            starred=starred,
            drive_id=drive_id,
        )
        return self._core_starred_file(body)

    def batch_star_files(self,
                         file_id_list: List[str],
                         starred: bool = True,
                         drive_id: str = None) -> List[BatchSubResponse[BaseFile]]:
        """
        官方：批量收藏(或取消) 文件
        :param file_id_list: [必须] 文件ID列表
        :param starred: [必须] 是否收藏
        :param drive_id: [可选] 文件所在的网盘ID
        :return: [BatchSubResponse] 批量操作结果

        用法示例：
        >>> from aligo import Aligo
        >>> ali = Aligo()
        >>> star_files = ali.batch_star_files(['file_id1', 'file_id2'])
        >>> print(star_files[0].body.name)
        """
        body = BatchStarFilesRequest(
            drive_id=drive_id,
            file_id_list=file_id_list,
            starred=starred,
        )
        result = self._core_batch_star_files(body)
        return list(result)

    def get_starred_list(self, body: GetStarredListRequest = None, **kwargs) -> List[BaseFile]:
        """
        官方：获取收藏列表
        :param body: [可选] 请求体
        :param kwargs: [可选] 其他参数
        :return: [List[BaseFile]] 收藏列表

        用法示例：
        >>> from aligo import Aligo
        >>> ali = Aligo()
        >>> starred_list = ali.get_starred_list()
        >>> print(starred_list[0].name)
        """
        if body is None:
            body = GetStarredListRequest(**kwargs)
        result = self._core_get_starred_list(body)
        return list(result)
