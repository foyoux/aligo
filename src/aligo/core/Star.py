"""收藏相关"""
from dataclasses import asdict
from typing import Iterator

from aligo.core.Config import *
from aligo.request import *
from aligo.response import *
from aligo.types import *
from .Update import Update


class Star(Update):
    """..."""
    _MAX_STAR_COUNT: int = 500

    def _core_starred_file(self, body: StarredFileRequest) -> BaseFile:
        """收藏(或取消) 文件"""
        return self.update_file(UpdateFileRequest(**asdict(body)))

    def _core_batch_star_files(self, body: BatchStarFilesRequest) -> Iterator[BatchSubResponse[BaseFile]]:
        """批量收藏文件"""
        if body.drive_id is None:
            body.drive_id = self.default_drive_id
        if body.starred:
            custom_index_key = 'starred_yes'
        else:
            custom_index_key = ''

        yield from self.batch_request(BatchRequest(
            requests=[BatchSubRequest(
                id=file_id,
                url='/file/update',
                method='PUT',
                body=StarredFileRequest(
                    drive_id=body.drive_id, file_id=file_id,
                    starred=body.starred, custom_index_key=custom_index_key
                )
            ) for file_id in body.file_id_list]
        ), BaseFile)

    def _core_get_starred_list(self, body: GetStarredListRequest) -> Iterator[BaseFile]:
        """收藏(或取消) 文件列表"""
        yield from self._list_file(V2_FILE_LIST_BY_CUSTOM_INDEX_KEY, body, GetStarredListResponse)
