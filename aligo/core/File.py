"""..."""
from typing import Iterator

from aligo.core import *
from aligo.core.Config import *
from aligo.request import *
from aligo.response import *
from aligo.types import *


class File(BaseAligo):
    """..."""

    def get_file_list(self, body: GetFileListRequest) -> Iterator[BaseFile]:
        """..."""
        for i in self._list_file(V2_FILE_LIST, body, GetFileListResponse):
            yield i

    # @lru_memoize()  # for cache of get_file_list fun
    # def _cache_get_file_list(self, body: GetFileListRequest) -> GetFileListResponse:
    #     """..."""
    #     response = self._post(V2_FILE_LIST, body=body)
    #     return self._result(response, GetFileListResponse)
    #
    # @overload
    # def get_file_list(self, body: Union[GetFileListRequest, BaseFile], f5: bool = False) -> Iterator[BaseFile]:
    #     """..."""
    #     ...
    #
    # @overload
    # def get_file_list(self, parent_file_id: str = 'root', drive_id: str = None, f5: bool = False) -> Iterator[BaseFile]:
    #     """..."""
    #     ...
    #
    # # @lru_cache # for the generator, repeated acquisition will only get empty
    # def get_file_list(
    #         self,
    #         body: Union[GetFileListRequest, BaseFile] = None,
    #         parent_file_id: str = 'root',
    #         drive_id: str = None,
    #         f5: bool = False
    # ) -> Iterator[BaseFile]:
    #     """
    #     1. If body is missing and list drive root files
    #     2. Usually you only need to provide GetFileListRequest.parent_file_id, default is 'root'
    #     """
    #     # Generate GetFileListRequest
    #     if body is None:
    #         body = GetFileListRequest(parent_file_id=parent_file_id, drive_id=drive_id)
    #
    #     if isinstance(body, BaseFile):
    #         body = GetFileListRequest(drive_id=body.drive_id, parent_file_id=body.file_id)
    #
    #     if body.drive_id is None:
    #         body.drive_id = self.default_drive_id
    #
    #     if f5:
    #         key = self._cache_get_file_list.cache_key(self=self, body=body)
    #         self._cache_get_file_list.cache.delete(key)
    #
    #     resp = self._cache_get_file_list(body=body)
    #     if isinstance(resp, Null):
    #         yield resp
    #         return
    #     for item in resp.items:
    #         yield item
    #     if resp.next_marker != '':
    #         body.marker = resp.next_marker
    #         for it in self.get_file_list(body=body, f5=f5):
    #             yield it
