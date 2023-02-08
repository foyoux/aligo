"""..."""
from typing import List

from aligo.core import *
from aligo.request import *
from aligo.types import *
from aligo.types.Enum import *


class Update(Core):
    """..."""

    def rename_file(self,
                    file_id: str,
                    name: str,
                    check_name_mode: CheckNameMode = 'refuse',
                    drive_id: str = None) -> BaseFile:
        """
        文件重命名
        :param file_id: [必选] 文件id
        :param name: [必选] 新的文件名
        :param check_name_mode: [可选] 检查文件名模式
        :param drive_id: [可选] 文件所在的网盘id
        :return: [BaseFile] 文件信息

        :Example:
        >>> from aligo import Aligo
        >>> ali = Aligo()
        >>> new_file = ali.rename_file('<file_id>', 'new_name')
        >>> print(new_file.name)
        """
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
        """
        批量重命名文件
        :param file_id_list: [必选] 文件id列表
        :param new_name_list: [必选] 新的文件名列表
        :param check_name_mode: [可选] 检查文件名模式
        :param drive_id: [可选] 文件所在的网盘id
        :return: [List[BaseFile]] 文件信息列表

        :Example:
        >>> from aligo import Aligo
        >>> ali = Aligo()
        >>> new_file_list = ali.batch_rename_files(['<file_id_list>'], ['<new_name_list>'])
        >>> print(new_file_list[0].name)
        """
        if drive_id is None:
            drive_id = self.default_drive_id

        ids_len = len(file_id_list)
        if ids_len != len(new_name_list):
            self._auth.log.warning(f'长度不一致 file_id_list{ids_len}, new_name_list {len(new_name_list)}')
            return []

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
