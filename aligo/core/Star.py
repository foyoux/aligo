"""收藏相关"""
from typing import Iterator

from aligo.core import *
from aligo.request import *
from aligo.response import *
from aligo.types import *
from .Update import Update
from dataclasses import asdict


class Star(Update):
    """..."""
    MAX_STAR_COUNT: int = 500

    def starred_file(self, body: StarredFileRequest) -> BaseFile:
        """收藏(或取消) 文件"""
        return self.update_file(UpdateFileRequest(**asdict(body)))

    def batch_star_files(self, body: BatchStarFilesRequest) -> Iterator[BatchResponse]:
        """批量收藏文件"""
        if body.drive_id is None:
            body.drive_id = self.default_drive_id
        if body.starred:
            custom_index_key = 'starred_yes'
        else:
            custom_index_key = ''

        for file_id_list in self._list_split(body.file_id_list, self.MAX_STAR_COUNT):
            response = self._post(V2_BATCH, body={
                "requests": [
                    {
                        "body": {"drive_id": body.drive_id, "file_id": file, "starred": body.starred,
                                 "custom_index_key": custom_index_key},
                        "headers": {"Content-Type": "application/json"},
                        "id": file,
                        "method": "PUT",
                        "url": "/file/update"
                    } for file in file_id_list
                ],
                "resource": "file"
            })
            if response.status_code != 200:
                yield Null(response)
                return

            for file in response.json()['responses']:
                yield BatchResponse(**file)

    def get_starred_list(self, body: GetStarredListRequest) -> Iterator[BaseFile]:
        """收藏(或取消) 文件列表"""
        for i in self._list_file(V2_FILE_LIST_BY_CUSTOM_INDEX_KEY, body, GetStarredListResponse):
            yield i
