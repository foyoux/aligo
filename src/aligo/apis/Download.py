"""..."""
import os
from typing import List, overload, Callable

from aligo.core import *
from aligo.error import AligoException
from aligo.request import *
from aligo.response import *
from aligo.types import *


class Download(Core):
    """..."""

    def get_download_url(self,
                         file_id: str,
                         file_name: str = None,
                         expire_sec: int = 14400,
                         drive_id: str = None,
                         ) -> GetDownloadUrlResponse:
        """
        获取下载链接: 一般在已知 file_id 或 download_url 失效时使用
        :param file_id: [str] 文件 id
        :param file_name: Optional[str] 文件名
        :param expire_sec: Optional[int] 下载链接有效时间, 默认为 4 小时, 这也是允许的最大值
        :param drive_id: Optional[str] 文件所在的网盘 id
        :return: [GetDownloadUrlResponse]

        用法示例:
        >>> from aligo import Aligo
        >>> ali = Aligo()
        >>> result = ali.get_download_url(file_id='<file_id>')
        >>> print(result)
        """
        body = GetDownloadUrlRequest(
            file_id=file_id,
            drive_id=drive_id,
            file_name=file_name,
            expire_sec=expire_sec,
        )
        return self._core_get_download_url(body)

    def batch_download_url(self,
                           file_id_list: List[str],
                           expire_sec: int = 14400,
                           drive_id=None) -> List[BatchDownloadUrlResponse]:
        """
        批量获取下载链接
        :param file_id_list: [List[str]] 文件 id 列表
        :param expire_sec: [int] 下载链接有效时间, 默认为 4 小时, 这也是允许的最大值
        :param drive_id: [str] 文件所在的网盘 id
        :return: [List[BatchDownloadUrlResponse]]

        用法示例:
        >>> from aligo import Aligo
        >>> ali = Aligo()
        >>> result = ali.batch_download_url(file_id_list=['<file1_id>', '<file2_id>'])
        >>> print(result)
        """
        body = BatchDownloadUrlRequest(
            drive_id=drive_id,
            file_id_list=file_id_list,
            expire_sec=expire_sec
        )
        result = self._core_batch_download_url(body)
        return list(result)

    def download_folder(self, folder_file_id: str, local_folder: str = '.', drive_id: str = None,
                        file_filter: Callable[[BaseFile], bool] = lambda x: False) -> str:
        """
        下载文件夹
        :param folder_file_id: [str] 文件夹 id
        :param local_folder: [str] 本地文件夹路径, 默认为当前目录, 即下载到哪里
        :param drive_id: [str] 文件夹所在的网盘 id
        :param file_filter: 文件过滤函数
        :return: [str] 本地文件夹路径

        用法示例:
        >>> from aligo import Aligo
        >>> ali = Aligo()
        >>> result = ali.download_folder(folder_file_id='<folder_file_id>')
        >>> print(result)
        """
        if folder_file_id != 'root':
            folder = self._core_get_file(GetFileRequest(file_id=folder_file_id, drive_id=drive_id))
            local_folder = os.path.join(local_folder, self._del_special_symbol(folder.name))
        return self.__download_folder(folder_file_id, local_folder, drive_id, file_filter=file_filter)

    def __download_folder(self, folder_file_id: str, local_folder: str = '.', drive_id: str = None,
                          file_filter: Callable[[BaseFile], bool] = lambda x: False) -> str:
        """下载文件夹"""
        # 创建文件夹, 即使文件夹为空
        os.makedirs(local_folder, exist_ok=True)
        files = []
        for file in self._core_get_file_list(GetFileListRequest(parent_file_id=folder_file_id, drive_id=drive_id)):
            if file_filter(file):
                continue
            if file.type == 'folder':
                self.__download_folder(folder_file_id=file.file_id,
                                       local_folder=os.path.join(local_folder, self._del_special_symbol(file.name)))
                continue
            files.append(file)
        self.download_files(files, local_folder=local_folder)
        return os.path.abspath(local_folder)

    @overload
    def download_file(self, *, file_path: str, url: str) -> str:
        """
        根据下载地址下载文件
        :param file_path: [str] 文件路径
        :param url: [str] 下载地址
        :return: [str] 本地文件路径

        用法示例:
        >>> from aligo import Aligo
        >>> ali = Aligo()
        >>> result = ali.download_file(file_path='<file_path>', url='<url>')
        >>> print(result)
        """

    @overload
    def download_file(self, *, file_id: str, local_folder: str = '.') -> str:
        """
        根据 file_id 下载文件
        :param file_id: [str] 文件 id
        :param local_folder: Optional[str] 本地文件夹路径, 默认为当前目录, 即下载到哪里
        :return: [str] 本地文件路径

        用法示例:
        >>> from aligo import Aligo
        >>> ali = Aligo()
        >>> result = ali.download_file(file_id='<file_id>')
        >>> print(result)
        """

    @overload
    def download_file(self, *, file: BaseFile, local_folder: str = '.') -> str:
        """
        根据 BaseFile 对象下载文件
        :param file: [BaseFile] 文件对象
        :param local_folder: Optional[str] 本地文件夹路径, 默认为当前目录, 即下载到哪里
        :return: [str] 本地文件路径

        用法示例:
        >>> from aligo import Aligo
        >>> ali = Aligo()
        >>> # ll = ali.get_file_list()
        >>> # result = ali.download_file(file=ll[-1])
        >>> result = ali.download_file(file=BaseFile(file_id='<file_id>'))
        >>> print(result)
        """

    def download_file(
            self, *, file_path: str = None, url: str = None,
            local_folder: str = '.', file_id: str = None,
            file: BaseFile = None, drive_id=None
    ) -> str:
        """download_file"""
        if file_id:
            file = self._core_get_file(GetFileRequest(file_id=file_id, drive_id=drive_id))

        if file:
            if file.type == 'folder':
                raise AligoException('文件类型不对：期待文件，得到的是文件夹')
            file_path = os.path.join(local_folder, file.name)
            url = file.download_url or file.url

        return self._core_download_file(file_path, url)
