"""..."""
from typing import Iterator


from aligo.core import *
from aligo.request import *
from aligo.response import *
from aligo.types import *


class Recyclebin(BaseAligo):
    """删除文件太过危险, 只提供移动文件到回收站的功能"""

    def move_file_to_trash(self, body: MoveFileToTrashRequest) -> MoveFileToTrashResponse:
        """移动文件到回收站"""
        response = self._post(V2_RECYCLEBIN_TRASH, body=body)
        return self._result(response, MoveFileToTrashResponse, [202, 204])

    def batch_move_to_trash(self, body: BatchMoveToTrashRequest) -> Iterator[BatchResponse]:
        """..."""
        if body.drive_id is None:
            body.drive_id = self.default_drive_id
        response = self._post(V2_BATCH, body={
            "requests": [
                {
                    "body": {
                        "drive_id": body.drive_id,
                        "file_id": file_id
                    },
                    "headers": {"Content-Type": "application/json"},
                    "id": file_id,
                    "method": "POST",
                    "url": "/recyclebin/trash"
                } for file_id in body.file_id_list
            ],
            "resource": "file"
        })

        if response.status_code != 200:
            return Null(response)

        for batch in response.json()['responses']:
            yield BatchResponse(**batch)

    def restore_file(self, body: RestoreFileRequest) -> RestoreFileResponse:
        """恢复文件"""
        response = self._post(V2_RECYCLEBIN_RESTORE, body=body)
        return self._result(response, RestoreFileResponse, 204)

    def batch_restore_files(self, body: BatchRestoreRequest):
        """..."""
        if body.drive_id is None:
            body.drive_id = self.default_drive_id
        response = self._post(V2_BATCH, body={
            "requests": [
                {
                    "body": {
                        "drive_id": body.drive_id,
                        "file_id": file_id
                    },
                    "headers": {"Content-Type": "application/json"},
                    "id": file_id,
                    "method": "POST",
                    "url": "/recyclebin/restore"
                } for file_id in body.file_id_list
            ],
            "resource": "file"
        })

        if response.status_code != 200:
            return Null(response)

        for batch in response.json()['responses']:
            yield BatchResponse(**batch)

    def get_recyclebin_list(self, body: GetRecycleBinListRequest) -> Iterator[BaseFile]:
        """获取回收站文件列表"""
        for i in self._list_file(V2_RECYCLEBIN_LIST, body, GetRecycleBinListResponse):
            yield i

    # def delete_file(self):
    #     """删除文件"""
    #     raise NotImplementedError

    # @overload
    # def trash_file(self, body: Union[MoveFileToTrashRequest, BaseFile]) -> MoveFileToTrashResponse:
    #     """..."""
    #     ...
    #
    # @overload
    # def trash_file(
    #         self, file_id: str,
    #         drive_id: str = None
    # ) -> MoveFileToTrashResponse:
    #     """..."""
    #     ...
    #
    # # 回收站相关
    # def trash_file(self, body: Union[MoveFileToTrashRequest, BaseFile] = None, file_id: str = None,
    #                drive_id: str = None) -> MoveFileToTrashResponse:
    #     """移动文件到回收站"""
    #     if body is None:
    #         body = MoveFileToTrashRequest(file_id=file_id, drive_id=drive_id)
    #     if isinstance(body, BaseFile):
    #         body = MoveFileToTrashRequest(drive_id=body.drive_id, file_id=body.file_id)
    #     # 无需缓存, drive_id 可由_post方法处理
    #     # if body.drive_id is None:
    #     #     body.drive_id = self.default_drive_id
    #
    #     response = self._post(V2_RECYCLEBIN_TRASH, body=body)
    #     return self._result(response, MoveFileToTrashResponse, 202)

    # @lru_memoize()
    # def _cache_get_recyclebin_list(self, body: GetRecycleBinListRequest) -> GetRecycleBinListResponse:
    #     """
    #     带缓存回收站列表, 此函数一般仅清空缓存时调用, ali._cache_get_recyclebin_list.cache.clear()
    #     """
    #     response = self._post(V2_RECYCLEBIN_LIST, body=body)
    #     return self._result(response, GetRecycleBinListResponse)
    #
    # def get_recyclebin_list(
    #         self,
    #         body: GetRecycleBinListRequest = None,
    #         f5: bool = False) -> Iterator[BaseFile]:
    #     """获取回收站文件列表"""
    #     if body is None:
    #         body = GetRecycleBinListRequest()
    #
    #     if body.drive_id is None:
    #         body.drive_id = self.default_drive_id
    #
    #     if f5:
    #         key = self._cache_get_recyclebin_list.cache_key(self=self, body=body)
    #         self._cache_get_recyclebin_list.cache.delete(key)
    #
    #     resp = self._cache_get_recyclebin_list(body=body)
    #     if isinstance(resp, Null):
    #         yield resp
    #         return
    #     for item in resp.items:
    #         yield item
    #     if resp.next_marker != '':
    #         body.marker = resp.next_marker
    #         for it in self.get_recyclebin_list(body=body, f5=f5):
    #             yield it

    # @overload
    # def restore_file(self, body: Union[RestoreFileRequest, BaseFile]) -> RestoreFileResponse:
    #     """..."""
    #     ...
    #
    # @overload
    # def restore_file(self, file_id: str,
    #                  drive_id: str = None) -> RestoreFileResponse:
    #     """..."""
    #     ...
    #
    # def restore_file(self, body: Union[RestoreFileRequest, BaseFile] = None, file_id: str = None,
    #                  drive_id: str = None) -> RestoreFileResponse:
    #     """..."""
    #     if body is None:
    #         body = RestoreFileRequest(file_id=file_id, drive_id=drive_id)
    #     if isinstance(body, BaseFile):
    #         body = RestoreFileRequest(drive_id=body.drive_id, file_id=body.file_id)
    #     # 没有缓存, drive_id再_post中处理
    #     response = self._post(V2_RECYCLEBIN_RESTORE, body=body)
    #     return self._result(response, RestoreFileResponse, 204)
