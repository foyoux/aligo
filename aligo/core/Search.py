"""..."""
from typing import Iterator

from aligo.config import *
from aligo.core import *
from aligo.request import *
from aligo.response import *
from aligo.types import *


class Search(BaseAligo):
    """..."""

    def search_file(self, body: SearchFileRequest) -> Iterator[BaseFile]:
        """
        关于 query 的语法, 参考下段代码
        {
            key: "getPDSSearchQuery", value: function () {
                var n = ['name match "'.concat(this.queryToSearch, '"')];
                return this.filter && ("folder" === this.filter ? n.push('type = "'.concat(this.filter, '"')) : n.push('category = "'.concat(this.filter, '"'))), n.join(" and ")
            }
        }
        eg: 'name match "epub"'
        eg: 'name match "epub" and category = "image"'
        category : BaseFileCategory
        """
        for i in self._list_file(V2_FILE_SEARCH, body, SearchFileResponse):
            yield i

    # @lru_memoize()
    # def _cache_search_file(self, body: SearchFileRequest) -> SearchFileResponse:
    #     """..."""
    #     response = self._post(V2_FILE_SEARCH, body=body)
    #     return self._result(response, SearchFileResponse)
    #
    # @overload
    # def search_file(self, body: SearchFileRequest, f5: bool = False) -> Iterator[BaseFile]:
    #     """..."""
    #     ...
    #
    # @overload
    # def search_file(
    #         self,
    #         name: str,
    #         category: BaseFileCategory = None,
    #         limit: int = None,
    #         drive_id: str = None,
    #         f5: bool = False
    # ) -> Iterator[BaseFile]:
    #     """..."""
    #     ...
    #
    # def search_file(self, body: SearchFileRequest = None, name: str = None, category: BaseFileCategory = None,
    #                 limit: int = None, drive_id: str = None,
    #                 f5: bool = False) -> Iterator[BaseFile]:
    #     """
    #     关于 query 的语法, 参考下段代码
    #     {
    #         key: "getPDSSearchQuery", value: function () {
    #             var n = ['name match "'.concat(this.queryToSearch, '"')];
    #             return this.filter && ("folder" === this.filter ? n.push('type = "'.concat(this.filter, '"')) : n.push('category = "'.concat(this.filter, '"'))), n.join(" and ")
    #         }
    #     }
    #     eg: 'name match "epub"'
    #     eg: 'name match "epub" and category = "image"'
    #     category : BaseFileCategory
    #     """
    #     if body is None:
    #         query = f'name match "{name}"'
    #         if category is not None:
    #             query += f' and category = "{category}"'
    #         body = SearchFileRequest(query=query, limit=limit, drive_id=drive_id)
    #
    #     if body.drive_id is None:
    #         body.drive_id = self.default_drive_id
    #
    #     if f5:
    #         key = self._cache_search_file.cache_key(self=self, body=body)
    #         self._cache_search_file.cache.delete(key)
    #
    #     resp = self._cache_search_file(body=body)
    #     if isinstance(resp, Null):
    #         yield resp
    #         return
    #     for item in resp.items:
    #         yield item
    #     if resp.next_marker != '':
    #         body.marker = resp.next_marker
    #         for it in self.search_file(body=body, f5=f5):
    #             yield it
