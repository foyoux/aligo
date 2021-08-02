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
        for i in self._list_file(V2_FILE_LIST, body, GetFileListResponse):
            yield i

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
