"""..."""
from typing import Iterator, Union

from aligo.core import *
from aligo.core.Config import *
from aligo.request import *
from aligo.response import *
from aligo.types import *


class File(BaseAligo):
    """..."""

    def get_file_list(self, body: GetFileListRequest) -> Iterator[BaseFile]:
        """..."""
        yield from self._list_file(V2_FILE_LIST, body, GetFileListResponse)

    def get_file_by_path(self, path: str = '/', parent_file_id: str = 'root',
                         drive_id: str = None) -> Union[BaseFile, None]:
        """成功则返回一个BaseFile对象, 失败返回None"""
        path = path.strip('/')
        if len(path) == 0:
            if parent_file_id == 'root':
                return None
            else:
                return self.get_file(GetFileRequest(file_id=parent_file_id, drive_id=drive_id))

        file = None
        for name in path.split('/'):
            file_list = File.get_file_list(self, GetFileListRequest(parent_file_id=parent_file_id, drive_id=drive_id))
            find: bool = False
            for file in file_list:
                if file.name == name:
                    find = True
                    parent_file_id = file.file_id
                    break
            if not find:
                return None
        return file

    def batch_get_files(self, body: BatchGetFileRequest) -> Iterator[BatchSubResponse]:
        """..."""
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
