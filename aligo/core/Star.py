"""收藏相关"""
from typing import Iterator, List

from aligo.core import *
from aligo.request import *
from aligo.response import *
from aligo.types import *


class Star(Update):
    """..."""
    MAX_STAR_COUNT: int = 500

    def starred_file(self, body: StarredFileRequest) -> BaseFile:
        """收藏(或取消) 文件"""
        return self.update_file(UpdateFileRequest(**body.__dict__))

    def _batch_star_files(self, body: BatchStarFilesRequest) -> List[BatchResponse]:
        """批量收藏文件"""
        if body.drive_id is None:
            body.drive_id = self.default_drive_id
        if body.starred:
            custom_index_key = 'starred_yes'
        else:
            custom_index_key = ''
        response = self._post(V2_BATCH, body={
            "requests": [
                {
                    "body": {"drive_id": body.drive_id, "file_id": file, "starred": body.starred,
                             "custom_index_key": custom_index_key},
                    "headers": {"Content-Type": "application/json"},
                    "id": file,
                    "method": "PUT",
                    "url": "/file/update"
                } for file in body.file_id_list
            ],
            "resource": "file"
        })
        if response.status_code != 200:
            return Null(response)

        return [BatchResponse(**file) for file in response.json()['responses']]

    def batch_star_files(self, body: BatchStarFilesRequest) -> Iterator[BatchResponse]:
        """..."""
        for i in range(0, len(body.file_id_list), self.MAX_STAR_COUNT):
            for j in self._batch_star_files(BatchStarFilesRequest(
                    drive_id=body.drive_id,
                    file_id_list=body.file_id_list[i:i + self.MAX_STAR_COUNT],
                    starred=body.starred
            )):
                yield j

    def get_starred_list(self, body: GetStarredListRequest) -> Iterator[BaseFile]:
        """收藏(或取消) 文件列表"""
        for i in self._list_file(V2_FILE_LIST_BY_CUSTOM_INDEX_KEY, body, GetStarredListResponse):
            yield i
