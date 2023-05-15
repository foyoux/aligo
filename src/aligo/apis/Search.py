"""Search class"""
import warnings
from typing import List, overload

from aligo.core import *
from aligo.request import *
from aligo.types import *
from aligo.types.Enum import *


class Search(Core):
    """搜索相关"""

    def search_file(self, *args, **kwargs):
        """请使用 search_files """
        warnings.warn('此方法已更名为 `search_files`', DeprecationWarning, stacklevel=2)
        return self.search_files(*args, **kwargs)

    @overload
    def search_files(self, name: str = None, category: SearchCategory = None,
                     drive_id: str = None, **kwargs) -> List[BaseFile]:
        """
        搜索文件
        :param name: [必选] 搜索的文件名
        :param category: [可选] 搜索的文件类型
        :param drive_id: [可选] 搜索的文件所在的网盘
        :param kwargs: [可选] 其他参数
        :return: [List[BaseFile]]

        用法示例：
        >>> from aligo import Aligo
        >>> ali = Aligo()
        >>> files1 = ali.search_files('test')
        >>> files2 = ali.search_files('test', category='video')
        """

    @overload
    def search_files(self, body: SearchFileRequest) -> List[BaseFile]:
        """
        搜索文件
        :param body: [必选] 搜索文件请求对象
        :return: [List[BaseFile]]

        用法示例：
        >>> from aligo import Aligo, SearchFileRequest
        >>> ali = Aligo()
        >>> files = ali.search_files(body=SearchFileRequest(query='name match "test"'))
        >>> print(files)
        """

    def search_files(self, name: str = None, category: SearchCategory = None, parent_file_id: str = 'root',
                     drive_id: str = None, body: SearchFileRequest = None, **kwargs) -> List[BaseFile]:
        """search files"""
        if body is None:
            query = ''
            if parent_file_id != 'root':
                query = f'parent_file_id = "{parent_file_id}"'
            if name:
                if query:
                    query += ' and '
                query += f'name match "{name}"'
            if category is not None:
                if query:
                    query += ' and '
                query += f'category = "{category}"'
            body = SearchFileRequest(query=query, drive_id=drive_id, **kwargs)
        result = self._core_search_files(body)
        return list(result)

    @overload
    def search_aims(self, keyword: str, category: BaseFileCategory = 'image',
                    drive_id: str = None, **kwargs) -> List[BaseFile]:
        """
        搜索目标/标签
        :param keyword: [必选] 搜索的关键字
        :param category: [可选] 搜索的文件类型
        :param drive_id: [可选] 搜索的文件所在的网盘
        :param kwargs: [可选] 其他参数
        :return: [List[BaseFile]]

        用法示例：
        >>> from aligo import Aligo
        >>> ali = Aligo()
        >>> files1 = ali.search_aims('test')
        >>> files2 = ali.search_aims('test', category='video')
        """

    @overload
    def search_aims(self, body: AimSearchRequest) -> List[BaseFile]:
        """
        搜索目标/标签
        :param body: [必选] 搜索目标/标签请求对象
        :return: [List[BaseFile]]

        用法示例：
        >>> from aligo import Aligo, AimSearchRequest
        >>> ali = Aligo()
        >>> files = ali.search_aims(body=AimSearchRequest(query='keywords = "test"'))
        >>> print(files)
        """

    def search_aims(self, keyword: str = None, category: BaseFileCategory = 'image', drive_id: str = None,
                    body: AimSearchRequest = None, **kwargs) -> List[BaseFile]:
        """search_aims"""
        if body is None:
            body = AimSearchRequest(
                query=f"keywords = '{keyword}' and type = 'file' and category = '{category}'",
                drive_id=drive_id,
                **kwargs
            )
        result = self._core_search_aims(body)
        return list(result)
