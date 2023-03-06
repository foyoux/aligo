"""..."""
from typing import Iterator

from aligo.core import *
from aligo.core.Config import *
from aligo.request import *
from aligo.response import *
from aligo.types import *


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
