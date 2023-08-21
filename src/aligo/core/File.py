"""..."""
from typing import Iterator

from aligo.core import BaseAligo
from aligo.core.Config import ADRIVE_V3_FILE_LIST, V2_FILE_WALK, V2_FILE_SCAN
from aligo.request import BatchGetFileRequest, GetFileListRequest, GetFileRequest, BatchRequest, BatchSubRequest
from aligo.response import BatchSubResponse, GetFileListResponse
from aligo.types import BaseFile
from aligo.types.Enum import BaseFileType, BaseFileCategory


class File(BaseAligo):
    """..."""

    def _core_get_file_list(self, body: GetFileListRequest) -> Iterator[BaseFile]:
        """..."""
        yield from self._list_file(ADRIVE_V3_FILE_LIST, body, GetFileListResponse, params={
            'jsonmask': ('next_marker,items(name,file_id,drive_id,type,size,created_at,updated_at,'
                         'category,file_extension,parent_file_id,mime_type,starred,thumbnail,url,'
                         'streams_info,content_hash,user_tags,user_meta,trashed,video_media_metadata,'
                         'video_preview_metadata,sync_meta,sync_device_flag,sync_flag,punish_flag')
        })

    def _core_batch_get_files(self, body: BatchGetFileRequest) -> Iterator[BatchSubResponse]:
        """batch_get_files"""
        if body.drive_id is None:
            body.drive_id = self.default_drive_id

        yield from self.batch_request(BatchRequest(
            requests=[BatchSubRequest(
                id=file_id,
                url='/file/get',
                body=GetFileRequest(
                    drive_id=body.drive_id, file_id=file_id
                )
            ) for file_id in body.file_id_list]
        ), GetFileRequest)

    def _core_walk_file(
            self,
            parent_file_id: str = 'root',
            drive_id: str = None,
            type_: BaseFileType = None,
            url_expire_sec: int = 86400,
            limit: int = 1000,
    ) -> Iterator[BaseFile]:
        """..."""
        yield from self._list_file(V2_FILE_WALK, {
            'parent_file_id': parent_file_id,
            'drive_id': drive_id or self.default_drive_id,
            'type': type_,
            'url_expire_sec': url_expire_sec,
            'limit': limit,
        }, GetFileListResponse)

    def _core_scan_file(
            self,
            drive_id: str = None,
            category: BaseFileCategory = None,
            limit: int = 1000,
    ) -> Iterator[BaseFile]:
        """..."""
        yield from self._list_file(V2_FILE_SCAN, {
            'drive_id': drive_id or self.default_drive_id,
            'category': category,
            'limit': limit,
        }, GetFileListResponse)
