"""Copy class"""
from typing import List, overload

from aligo.core import *
from aligo.request import *
from aligo.response import *


class Copy(Core):
    """复制文件相关
    说明：官方虽然提供文件（夹）复制接口，但并未公开文件（夹）复制的功能。
        所以后期可能会失效，不过有替代方案，如果此接口失效我会补上。
    """

    @overload
    def copy_file(self, file_id: str,
                  to_parent_file_id: str = 'root',
                  new_name: str = None,
                  drive_id: str = None,
                  to_drive_id: str = None,
                  **kwargs) -> CopyFileResponse:
        """
        复制文件（夹）
        :param file_id: [str] 文件（夹）ID
        :param to_parent_file_id: Optional[str] 目标目录ID
        :param new_name: Optional[str] 新文件（夹）名
        :param drive_id: Optional[str] 文件（夹）所在的网盘ID
        :param to_drive_id: Optional[str] 目标网盘ID
        :param kwargs: 额外参数
        :return: [CopyFileResponse]

        用法示例：
        >>> from aligo import Aligo
        >>> ali = Aligo()
        >>> result = ali.copy_file('<file_id>')
        >>> print(result)
        """

    @overload
    def copy_file(self, body: CopyFileRequest) -> CopyFileResponse:
        """
        复制文件（夹）
        :param body: [CopyFileRequest]
        :return: [CopyFileResponse]

        用法示例：
        >>> from aligo import Aligo, CopyFileRequest
        >>> ali = Aligo()
        >>> result = ali.copy_file(body=CopyFileRequest(file_id='<file_id>'))
        >>> print(result)
        """

    def copy_file(self, file_id: str = None,
                  to_parent_file_id: str = 'root',
                  new_name: str = None,
                  drive_id: str = None,
                  to_drive_id: str = None,
                  body: CopyFileRequest = None,
                  **kwargs) -> CopyFileResponse:
        """copy_file"""
        if body is None:
            body = CopyFileRequest(
                file_id=file_id,
                drive_id=drive_id,
                to_drive_id=to_drive_id,
                to_parent_file_id=to_parent_file_id,
                new_name=new_name,
                **kwargs
            )
        return self._core_copy_file(body)

    @overload
    def batch_copy_files(self,
                         file_id_list: List[str],
                         to_parent_file_id: str = 'root',
                         drive_id: str = None,
                         **kwargs) -> List[BatchSubResponse[CopyFileResponse]]:
        """
        复制文件（夹）
        :param file_id_list: [List[str]] 文件（夹）ID列表
        :param to_parent_file_id: Optional[str] 目标目录ID
        :param drive_id: Optional[str] 文件（夹）所在的网盘ID
        :param kwargs: 额外参数
        :return: [BatchSubResponse]

        用法示例：
        >>> from aligo import Aligo
        >>> ali = Aligo()
        >>> result = ali.batch_copy_files(file_id_list=['<file1_id>', '<file2_id>'])
        >>> print(result[0].body.file_id)
        """

    @overload
    def batch_copy_files(self, body: BatchCopyFilesRequest) -> List[BatchSubResponse[CopyFileResponse]]:
        """
        复制文件（夹）
        :param body: [BatchCopyFilesRequest]
        :return: [BatchSubResponse]

        用法示例：
        >>> from aligo import Aligo, BatchCopyFilesRequest
        >>> ali = Aligo()
        >>> result = ali.batch_copy_files(body=BatchCopyFilesRequest(file_id_list=['<file1_id>', '<file2_id>']))
        >>> print(result[0].body.file_id)
        """

    def batch_copy_files(self,
                         file_id_list: List[str] = None,
                         to_parent_file_id: str = 'root',
                         drive_id: str = None,
                         body: BatchCopyFilesRequest = None,
                         **kwargs) -> List[BatchSubResponse[CopyFileResponse]]:
        """batch_copy_files"""
        if body is None:
            body = BatchCopyFilesRequest(drive_id=drive_id,
                                         file_id_list=file_id_list,
                                         to_parent_file_id=to_parent_file_id,
                                         **kwargs)
        result = self._core_batch_copy_files(body)
        return list(result)
