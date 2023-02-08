"""..."""
from typing import List, overload

from aligo.core import *
from aligo.request import *
from aligo.response import *


class Move(Core):
    """..."""

    @overload
    def move_file(self, file_id: str,
                  to_parent_file_id: str = 'root',
                  new_name: str = None,
                  drive_id: str = None,
                  to_drive_id: str = None,
                  **kwargs) -> MoveFileResponse:
        """
        移动文件
        :param file_id: [必选] 文件ID
        :param to_parent_file_id: [可选] 目标文件夹ID
        :param new_name: [可选] 新文件名
        :param drive_id: [可选] 文件所在的网盘ID
        :param to_drive_id: [可选] 目标网盘ID
        :param kwargs: [可选] 其他参数
        :return: [MoveFileResponse]

        用法示例：
        >>> from aligo import Aligo, MoveFileRequest
        >>> ali = Aligo()
        >>> result = ali.move_file(file_id='<file_id>')  # 默认移动到 根目录
        >>> print(result)
        """

    @overload
    def move_file(self, body: MoveFileRequest) -> MoveFileResponse:
        """
        移动文件
        :param body: [必选] 移动文件请求体
        :return: [MoveFileResponse]

        用法示例：
        >>> from aligo import Aligo, MoveFileRequest
        >>> ali = Aligo()
        >>> body = MoveFileRequest(file_id='<file_id>')  # 默认移动到 根目录
        >>> result = ali.move_file(body=body)
        >>> print(result)
        """

    def move_file(self, file_id: str = None,
                  to_parent_file_id: str = 'root',
                  new_name: str = None,
                  drive_id: str = None,
                  to_drive_id: str = None,
                  body: MoveFileRequest = None,
                  **kwargs) -> MoveFileResponse:
        """move_file"""
        if body is None:
            body = MoveFileRequest(
                file_id=file_id,
                drive_id=drive_id,
                to_drive_id=to_drive_id,
                to_parent_file_id=to_parent_file_id,
                new_name=new_name,
                **kwargs
            )
        return self._core_move_file(body)

    @overload
    def batch_move_files(self,
                         file_id_list: List[str],
                         to_parent_file_id: str = 'root',
                         drive_id: str = None,
                         **kwargs) -> List[BatchSubResponse[MoveFileResponse]]:
        """
        批量移动文件
        :param file_id_list: [必选] 文件ID列表
        :param to_parent_file_id: [可选] 目标文件夹ID
        :param drive_id: [可选] 文件所在的网盘ID
        :param kwargs: [可选] 其他参数
        :return: [List[BatchSubResponse]]

        用法示例：
        >>> from aligo import Aligo, BatchMoveFilesRequest
        >>> ali = Aligo()
        >>> file_id_list = ['<file1_id>', '<file2_id>']
        >>> result = ali.batch_move_files(file_id_list=file_id_list)  # 默认移动到 根目录
        >>> print(result[0].body.file_id)
        """

    @overload
    def batch_move_files(self, body: BatchMoveFilesRequest) -> List[BatchSubResponse[MoveFileResponse]]:
        """
        批量移动文件
        :param body: [必选] 批量移动文件请求体
        :return: [List[BatchSubResponse]]

        用法示例：
        >>> from aligo import Aligo, BatchMoveFilesRequest
        >>> ali = Aligo()
        >>> body = BatchMoveFilesRequest(file_id_list=['<file1_id>', '<file2_id>'])  # 默认移动到 根目录
        >>> result = ali.batch_move_files(body=body)
        >>> print(result[0].body.file_id)
        """

    def batch_move_files(self,
                         file_id_list: List[str] = None,
                         to_parent_file_id: str = 'root',
                         drive_id: str = None,
                         body: BatchMoveFilesRequest = None,
                         **kwargs) -> List[BatchSubResponse[MoveFileResponse]]:
        """batch_move_files"""
        if body is None:
            body = BatchMoveFilesRequest(
                drive_id=drive_id,
                file_id_list=file_id_list,
                to_parent_file_id=to_parent_file_id,
                **kwargs
            )
        result = self._core_batch_move_files(body)
        return list(result)
