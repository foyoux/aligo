"""..."""
from typing import List

from aligo.core import *
from aligo.request import *
from aligo.types import *
from aligo.types.Enum import *


class Search(Core):
    """..."""

    def search_file(self, name: str = None, category: SearchCategory = None, drive_id: str = None,
                    body: SearchFileRequest = None, **kwargs) -> List[BaseFile]:
        """搜索文件"""
        if body is None:
            query = f'name match "{name}"'
            if category is not None:
                query += f' and category = "{category}"'
            body = SearchFileRequest(query=query, **kwargs)
        result = super(Search, self).search_file(body)
        return [i for i in result]

    def search_aims(self, keyword: str = None, category: BaseFileCategory = 'image', drive_id: str = None,
                    body: AimSearchRequest = None, **kwargs) -> List[BaseFile]:
        """搜索目标/标签"""
        if body is None:
            body = AimSearchRequest(
                query=f"keywords ='{keyword}' and type = 'file' and category = '{category}'",
                drive_id=drive_id,
                **kwargs
            )
        result = super(Search, self).search_aims(body)
        return [i for i in result]
