"""..."""
from typing import List

from aligo.core import *
from aligo.request import *
from aligo.types import *
from aligo.types.Enum import *


class Update(Core):
    """..."""

    def rename_file(self,
                    name: str,
                    file_id: str,
                    check_name_mode: CheckNameMode = 'refuse',
                    drive_id: str = None) -> BaseFile:
        """重命名文件(夹)"""
        body = RenameFileRequest(
            name=name,
            file_id=file_id,
            check_name_mode=check_name_mode,
            drive_id=drive_id,
        )
        return self._core_rename_file(body)

    def batch_rename_files(
            self,
            file_id_list: List[str],
            new_name_list: List[str],
            check_name_mode: CheckNameMode = 'refuse',
            drive_id: str = None) -> List[BaseFile]:
        """..."""
        if drive_id is None:
            drive_id = self.default_drive_id

        ids_len = len(file_id_list)
        if ids_len != len(new_name_list):
            self._auth.log.warning(f'长度不一致 file_id_list{ids_len}, new_name_list {len(new_name_list)}')
            return

        result = []
        for i in self.batch_request(BatchRequest(
                requests=[BatchSubRequest(
                    id=file_id_list[j],
                    url='/file/update',
                    body=RenameFileRequest(
                        name=new_name_list[j],
                        file_id=file_id_list[j],
                        drive_id=drive_id,
                        check_name_mode=check_name_mode
                    )
                ) for j in range(ids_len)]
        ), BaseFile):
            result.append(i)

        return result
