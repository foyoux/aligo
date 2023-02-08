"""Recyclebin class"""
from typing import List, overload

from aligo.core import *
from aligo.request import *
from aligo.response import *
from aligo.types import *


class Recyclebin(Core):
    """删除文件太过危险, 只提供移动文件到回收站的功能"""

    def move_file_to_trash(self, file_id: str, drive_id: str = None) -> MoveFileToTrashResponse:
        """
        移动文件到回收站
        :param file_id: [必须] 文件ID
        :param drive_id: [可选] 文件所在的网盘ID
        :return: [MoveFileToTrashResponse]

        用法示例:
        >>> from aligo import Aligo
        >>> ali = Aligo()
        >>> result = ali.move_file_to_trash('<file_id>')
        >>> print(result)
        """
        body = MoveFileToTrashRequest(file_id=file_id, drive_id=drive_id)
        return self._core_move_file_to_trash(body)

    def batch_move_to_trash(self, file_id_list: List[str], drive_id: str = None) -> List[BatchSubResponse]:
        """
        批量移动文件到回收站
        :param file_id_list: [必须] 文件ID列表
        :param drive_id: [可选] 文件所在的网盘ID
        :return: [BatchSubResponse]

        用法示例:
        >>> from aligo import Aligo
        >>> ali = Aligo()
        >>> result = ali.batch_move_to_trash(['<file1_id>', '<file2_id>'])
        >>> print(result)
        """
        body = BatchMoveToTrashRequest(drive_id=drive_id, file_id_list=file_id_list)
        result = self._core_batch_move_to_trash(body)
        return list(result)

    def restore_file(self, file_id: str, drive_id: str = None) -> RestoreFileResponse:
        """
        恢复文件
        :param file_id: [必须] 文件ID
        :param drive_id: [可选] 文件所在的网盘ID
        :return: [RestoreFileResponse]

        用法示例:
        >>> from aligo import Aligo
        >>> ali = Aligo()
        >>> result = ali.restore_file('<file_id>')
        >>> print(result)
        """
        body = RestoreFileRequest(drive_id=drive_id, file_id=file_id)
        return self._core_restore_file(body)

    def batch_restore_files(self, file_id_list: List[str], drive_id: str = None) -> List[BatchSubResponse]:
        """
        批量恢复文件
        :param file_id_list: [必须] 文件ID列表
        :param drive_id: [可选] 文件所在的网盘ID
        :return: [BatchSubResponse]

        用法示例:
        >>> from aligo import Aligo
        >>> ali = Aligo()
        >>> result = ali.batch_restore_files(['<file1_id>', '<file2_id>'])
        >>> print(result)
        """
        body = BatchRestoreRequest(drive_id=drive_id, file_id_list=file_id_list)
        result = self._core_batch_restore_files(body)
        return list(result)

    @overload
    def get_recyclebin_list(self, **kwargs) -> List[BaseFile]:
        """
        获取回收站列表
        :param kwargs: [可选] 其他参数
        :return: [BaseFile]

        用法示例:
        >>> from aligo import Aligo
        >>> ali = Aligo()
        >>> result = ali.get_recyclebin_list()
        >>> print(result)
        """

    @overload
    def get_recyclebin_list(self, body: GetRecycleBinListRequest) -> List[BaseFile]:
        """
        获取回收站列表
        :param body: [必须] 请求参数
        :return: [BaseFile]

        用法示例:
        >>> from aligo import Aligo
        >>> ali = Aligo()
        >>> body = GetRecycleBinListRequest()
        >>> result = ali.get_recyclebin_list(body)
        >>> print(result)
        """

    def get_recyclebin_list(self, body: GetRecycleBinListRequest = None, **kwargs) -> List[BaseFile]:
        """get_recyclebin_list"""
        if body is None:
            body = GetRecycleBinListRequest(**kwargs)
        result = self._core_get_recyclebin_list(body)
        return list(result)
