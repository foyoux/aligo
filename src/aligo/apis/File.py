"""文件相关"""
import os
from typing import List, overload, Union, Callable

from aligo.core import *
from aligo.core.Config import *
from aligo.request import *
from aligo.response import *
from aligo.types import *
from aligo.types.Enum import *


class File(Core):
    """..."""

    @overload
    def get_file(self, file_id: str, drive_id: str = None) -> BaseFile:
        """
        获取文件
        :param file_id: [str] 文件ID
        :param drive_id: Optional[str] 存储桶ID
        :return: [BaseFile] 文件对象

        用法示例:
        >>> from aligo import Aligo, BaseFile
        >>> ali = Aligo()
        >>> file = ali.get_file('file_id')
        >>> assert isinstance(file, BaseFile)
        >>> print(file)
        """

    @overload
    def get_file(self, body: GetFileRequest) -> BaseFile:
        """
        获取文件
        :param body: [GetFileRequest] 获取文件请求体
        :return: [BaseFile] 文件对象

        用法示例:
        >>> from aligo import Aligo, BaseFile, GetFileRequest
        >>> ali = Aligo()
        >>> file = ali.get_file(body=GetFileRequest(file_id='file_id'))
        >>> assert isinstance(file, BaseFile)
        >>> print(file)
        """

    def get_file(self,
                 file_id: str = None,
                 drive_id: str = None,
                 body: GetFileRequest = None,
                 **kwargs) -> BaseFile:
        """get_file"""
        if body is None:
            body = GetFileRequest(
                file_id=file_id, drive_id=drive_id,
                **kwargs
            )
        return self._core_get_file(body)

    @overload
    def get_file_list(self, parent_file_id: str = 'root', drive_id: str = None, **kwargs) -> List[BaseFile]:
        """
        获取文件列表
        :param parent_file_id: Optional[str] 文件夹ID，默认为根目录
        :param drive_id: Optional[str] 存储桶ID
        :param kwargs: [dict] 其他参数
        :return: [List[BaseFile]] 文件列表

        用法示例:
        >>> from aligo import Aligo
        >>> ali = Aligo()
        >>> file_list = ali.get_file_list('<parent_file_id>')
        >>> assert isinstance(file_list, list)
        >>> print(file_list)
        """

    @overload
    def get_file_list(self, body: GetFileListRequest) -> List[BaseFile]:
        """
        获取文件列表
        :param body: [GetFileListRequest] 获取文件列表请求体
        :return: [List[BaseFile]] 文件列表

        用法示例:
        >>> from aligo import Aligo, BaseFile, GetFileListRequest
        >>> ali = Aligo()
        >>> file_list = ali.get_file_list(body=GetFileListRequest(parent_file_id='<parent_file_id>'))
        >>> assert isinstance(file_list, list)
        >>> print(file_list)
        """

    def get_file_list(self, parent_file_id: str = 'root', drive_id: str = None, body: GetFileListRequest = None,
                      **kwargs) -> List[BaseFile]:
        """get_file_list"""
        if body is None:
            body = GetFileListRequest(drive_id=drive_id, parent_file_id=parent_file_id, **kwargs)
        result = self._core_get_file_list(body)
        return list(result)

    def batch_get_files(self, file_id_list: List[str], drive_id: str = None) -> List[BatchSubResponse]:
        """
        批量获取文件
        :param file_id_list: [List[str]] 文件ID列表
        :param drive_id: [str] 存储桶ID
        :return: [List[BatchSubResponse]] 批量获取文件响应列表

        用法示例:
        >>> from aligo import Aligo, Null
        >>> ali = Aligo()
        >>> file_list = ali.batch_get_files(['file_id1', 'file_id2'])
        >>> assert isinstance(file_list, list)
        >>> # 实际使用中一般不需要判断，这里写出来只是提供一个判断示例
        >>> if isinstance(file_list[-1], Null):
        >>>     print('出现错误')
        >>> for e in file_list:
        >>>     assert isinstance(e, BatchSubResponse)
        >>> print(file_list)
        """
        body = BatchGetFileRequest(file_id_list=file_id_list, drive_id=drive_id)
        result = self._core_batch_get_files(body)
        return list(result)

    def get_folder_by_path(
            self, path: str = '/', parent_file_id: str = 'root', create_folder: bool = False,
            check_name_mode: CheckNameMode = 'refuse', drive_id: str = None
    ) -> Union[BaseFile, CreateFileResponse, None]:
        """
        根据文件路径，获取网盘文件对象
        :param path: [str] 完整路径，无需以 '/' 开始或结束
        :param parent_file_id: Optional[str] 父文件夹ID，默认为根目录，意思是基于根目录查找
        :param create_folder:  Optional[bool] 不存在是否创建，默认：True. 此行为效率最高
        :param check_name_mode: Optional[CheckNameMode] 检查名称模式，默认为 'refuse'
        :param drive_id: Optional[str] 存储桶ID，一般情况下，drive_id 参数都无需提供
        :return: 文件对象，或创建文件夹返回的对象，或 None

        用法示例:
        >>> from aligo import Aligo
        >>> ali = Aligo()
        >>> folder = ali.get_folder_by_path('path/to/folder')
        >>> assert isinstance(folder, BaseFile)
        >>> print(folder)
        """
        path = path.strip('/')
        if not path:
            return self.get_file(file_id=parent_file_id, drive_id=drive_id)
        folder = None
        if create_folder:
            for folder_name in path.split('/'):
                folder = self._core_create_folder(
                    CreateFolderRequest(
                        name=folder_name, parent_file_id=parent_file_id,
                        check_name_mode=check_name_mode, drive_id=drive_id
                    )
                )
                parent_file_id = folder.file_id
            return folder
        else:
            for folder_name in path.split('/'):
                folders = self.get_file_list(parent_file_id=parent_file_id, drive_id=drive_id, type='folder')
                # 获取目标 folder
                for folder in folders:
                    if folder.name == folder_name:
                        parent_file_id = folder.file_id
                        break
                else:
                    return None
            return folder

    def get_file_by_path(self, path: str = '/', parent_file_id: str = 'root',
                         check_name_mode: CheckNameMode = 'refuse',
                         drive_id: str = None) -> Optional[BaseFile]:
        """
        根据路径获取云盘文件对象, 先找到啥就返回啥（早期可能存在同名文件（夹）），否则返回None
        :param path: [str] 路径，无需以'/'开头
        :param parent_file_id: Optional[str] 父文件夹ID，默认为根目录，意思是基于根目录查找
        :param check_name_mode: Optional[CheckNameMode] 检查名称模式，默认为 'refuse'
        :param drive_id: Optional[str] 存储桶ID
        :return: [BaseFile] 文件对象，或 None

        用法示例:
        >>> from aligo import Aligo
        >>> ali = Aligo()
        >>> file = ali.get_file_by_path('path/to/file')
        >>> assert isinstance(file, BaseFile)
        >>> print(file)
        """
        path = path.strip('/')
        folder_path, file_name = os.path.split(path)
        folder = None
        if folder_path != '':
            folder = self.get_folder_by_path(
                folder_path, parent_file_id=parent_file_id, create_folder=False,
                check_name_mode=check_name_mode, drive_id=drive_id
            )
            if folder is None:
                return None
            parent_file_id = folder.file_id

        if file_name == '':
            return folder

        file_list = self.get_file_list(parent_file_id=parent_file_id, drive_id=drive_id, type='file')

        for file in file_list:
            if file_name == file.name:
                return file

        return None

    def walk_files(self, callback: Callable[[str, BaseFile], None], parent_file_id: str = 'root', drive_id: str = None,
                   _path: str = ''):
        """遍历指定文件夹下所有文件

        :param drive_id:
        :param parent_file_id: 文件夹 id，默认 root
        :param callback: 回调函数
        :param _path: 当前文件基于指定文件夹的路径
        :return:
        """
        for f in self._core_get_file_list(GetFileListRequest(parent_file_id=parent_file_id, drive_id=drive_id)):
            if f.type == 'file':
                callback(_path, f)
                continue
            self.walk_files(callback, parent_file_id=f.file_id, drive_id=drive_id, _path=os.path.join(_path, f.name))

    def get_folder_size_info(self, file_id: str, drive_id: str = None) -> FolderSizeInfo:
        """获取文件夹信息，文件夹个数，以及文件个数及其大小，不递归"""
        response = self._post(ADRIVE_V1_FILE_GET_FOLDER_SIZE_INFO, body={'file_id': file_id, 'drive_id': drive_id})
        return self._result(response, FolderSizeInfo)
