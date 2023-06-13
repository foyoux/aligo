"""分享相关"""
import warnings
from typing import List, overload

from aligo.core import *
from aligo.request import *
from aligo.response import *
from aligo.types import *
from aligo.types.Enum import *


def _deprecation_warning(kwargs):
    if 'share_id' in kwargs:
        kwargs.pop('share_id')
        warnings.warn('share 相关方法已删除 `share_id` 参数，因为 share_token 已包含了 share_id 信息',
                      DeprecationWarning, stacklevel=3)


class Share(Core):
    """..."""

    def share_file(self,
                   file_id: str,
                   share_pwd: str = None,
                   expiration: str = None,
                   drive_id: str = None,
                   description: str = None) -> CreateShareLinkResponse:
        """
        官方：分享文件
        :param file_id: [必选] 文件id
        :param share_pwd: [可选] 分享密码，默认：None，表示无密码
        :param expiration: [可选] 有效期，utc时间字符串：YYYY-MM-DDTHH:mm:ss.SSSZ
        :param drive_id: [可选] 所属网盘id
        :param description: [可选] 描述
        :return: [CreateShareLinkResponse]

        用法示例：
        >>> from aligo import Aligo
        >>> ali = Aligo()
        >>> share = ali.share_file('<file1_id>', share_pwd='2020', expiration='2021-12-01T00:00:00.000Z', description='description')
        >>> print(share)
        """
        return self.share_files([file_id], share_pwd, expiration, drive_id, description)

    def share_files(self,
                    file_id_list: List[str],
                    share_pwd: str = None,
                    expiration: str = None,
                    drive_id: str = None,
                    description: str = None) -> CreateShareLinkResponse:
        """
        官方：分享文件
        :param file_id_list: [必选] 文件id列表
        :param share_pwd: [可选] 分享密码，默认：None，表示无密码
        :param expiration: [可选] 有效期，utc时间字符串：YYYY-MM-DDTHH:mm:ss.SSSZ
        :param drive_id: [可选] 所属网盘id
        :param description: [可选] 描述
        :return: [CreateShareLinkResponse]

        用法示例：
        >>> from aligo import Aligo
        >>> ali = Aligo()
        >>> share = ali.share_files(['<file1_id>','<file2_id>'], share_pwd='2020', expiration='2021-12-01T00:00:00.000Z', description='description')
        >>> print(share)
        """
        body = CreateShareLinkRequest(
            file_id_list=file_id_list,
            share_pwd=share_pwd,
            expiration=expiration,
            drive_id=drive_id,
            description=description,
        )
        return self._core_share_file(body)

    def update_share(
            self,
            share_id: str,
            share_pwd: str = None,
            expiration: str = None,
            description: str = None,
    ) -> UpdateShareLinkResponse:
        """
        官方：更新分享
        :param share_id: [必选] 分享id
        :param share_pwd: [可选] 分享密码，默认：None，表示无密码
        :param expiration: [可选] 有效期，utc时间字符串：YYYY-MM-DDTHH:mm:ss.SSSZ
        :param description: [可选] 描述
        :return: [UpdateShareLinkResponse]

        用法示例：
        >>> from aligo import Aligo
        >>> ali = Aligo()
        >>> old_share = ali.share_file('<file_id>')
        >>> new_share = ali.update_share(old_share.share_id)
        >>> print(new_share)
        """
        body = UpdateShareLinkRequest(
            share_id=share_id,
            share_pwd=share_pwd,
            expiration=expiration,
            description=description,
        )
        return self._core_update_share(body)

    def cancel_share(self, share_id: str) -> CancelShareLinkResponse:
        """
        官方：取消分享
        :param share_id: [必选] 分享id
        :return: [CancelShareLinkResponse]

        用法示例：
        >>> from aligo import Aligo
        >>> ali = Aligo()
        >>> share = ali.share_file('<file_id>')
        >>> cancel_share = ali.cancel_share(share.share_id)
        >>> print(cancel_share)
        """
        body = CancelShareLinkRequest(share_id=share_id)
        return self._core_cancel_share(body)

    def batch_cancel_share(self, share_id_list: List[str]) -> List[BatchSubResponse]:
        """
        官方：批量取消分享
        :param share_id_list: [必选] 分享id列表
        :return: [List[BatchSubResponse]]

        用法示例：
        >>> from aligo import Aligo
        >>> ali = Aligo()
        >>> share1 = ali.share_file('<file1_id>')
        >>> share2 = ali.share_file('<file2_id>')
        >>> # noinspection PyShadowingNames
        >>> share_id_list = [share1.share_id, share2.share_id]
        >>> cancel_share = ali.batch_cancel_share(share_id_list)
        >>> print(cancel_share)
        """
        body = BatchCancelShareRequest(share_id_list=share_id_list)
        result = self._core_batch_cancel_share(body)
        return list(result)

    def get_share_list(self,
                       order_by: GetShareLinkListOrderBy = 'created_at',
                       order_direction: OrderDirection = 'DESC',
                       include_canceled: bool = False) -> List[ShareLinkSchema]:
        """
        官方：获取分享列表
        :param order_by: [可选] 排序字段，默认：created_at
        :param order_direction: [可选] 排序方向，默认：DESC
        :param include_canceled: [可选] 是否包含已取消的分享，默认：False
        :return: [List[ShareLinkSchema]]

        用法示例：
        >>> from aligo import Aligo
        >>> ali = Aligo()
        >>> share_list = ali.get_share_list()
        >>> print(share_list)
        """
        body = GetShareLinkListRequest(
            creator=self.user_id,
            limit=100,
            order_by=order_by,
            order_direction=order_direction,
            include_canceled=include_canceled,
        )
        result = self._core_get_share_list(body)
        return list(result)

    # 处理其他人的分享
    def get_share_info(self, share_id: str) -> GetShareInfoResponse:
        """
        官方：获取分享信息
        :param share_id: [必选] 分享id
        :return: [GetShareInfoResponse]

        用法示例：
        >>> from aligo import Aligo
        >>> ali = Aligo()
        >>> share = ali.share_file('<file_id>')
        >>> share_info = ali.get_share_info(share.share_id)
        >>> print(share_info)
        """
        body = GetShareInfoRequest(share_id=share_id)
        return self._core_get_share_info(body)

    def get_share_token(self, share_id: str, share_pwd: str = '') -> GetShareTokenResponse:
        """
        官方：获取分享token
        :param share_id: [必选] 分享id
        :param share_pwd: [可选] 分享密码，默认：None，表示无密码
        :return: [GetShareTokenResponse]

        用法示例：
        >>> from aligo import Aligo
        >>> ali = Aligo()
        >>> share = ali.share_file('<file_id>')
        >>> share_token = ali.get_share_token(share.share_id)
        >>> print(share_token)
        """
        body = GetShareTokenRequest(share_id=share_id, share_pwd=share_pwd)
        return self._core_get_share_token(body)

    @overload
    def get_share_file_list(
            self,
            share_token: GetShareTokenResponse,
            parent_file_id: str = 'root',
            **kwargs
    ) -> List[BaseShareFile]:
        """
        官方：获取分享文件列表
        :param share_token: [必选] 分享token
        :param parent_file_id:
        :param kwargs: [可选] 其他参数
        :return: [List[BaseShareFile]]

        用法示例：
        >>> from aligo import Aligo
        >>> ali = Aligo()
        >>> share = ali.share_file('<file_id>')
        >>> # noinspection PyShadowingNames
        >>> share_token = ali.get_share_token(share.share_id)
        >>> share_file_list = ali.get_share_file_list(share_token)
        >>> print(share_file_list)
        """

    @overload
    def get_share_file_list(
            self,
            body: GetShareFileListRequest,
            share_token: GetShareTokenResponse
    ) -> List[BaseShareFile]:
        """
        官方：获取分享文件列表
        :param body: [必选] 请求体
        :param share_token: [必选] 分享token
        :return: [List[BaseShareFile]]

        用法示例：
        >>> from aligo import Aligo, GetShareFileListRequest
        >>> ali = Aligo()
        >>> share = ali.share_file('<file_id>')
        >>> # noinspection PyShadowingNames
        >>> share_token = ali.get_share_token(share.share_id)
        >>> # noinspection PyShadowingNames
        >>> body = GetShareFileListRequest(share_id=share_token.share_id)
        >>> share_file_list = ali.get_share_file_list(body=body, share_token=share_token)
        >>> print(share_file_list)
        """

    def get_share_file_list(
            self,
            share_token: GetShareTokenResponse = None,
            parent_file_id: str = 'root',
            body: GetShareFileListRequest = None,
            **kwargs
    ) -> List[BaseShareFile]:
        """get_share_file_list"""
        _deprecation_warning(kwargs)
        if body is None:
            body = GetShareFileListRequest(share_id=share_token.share_id, parent_file_id=parent_file_id, **kwargs)
        result = self._core_get_share_file_list(body, share_token)
        return list(result)

    def list_by_share(
            self,
            share_token: GetShareTokenResponse = None,
            parent_file_id: str = 'root',
            body: GetShareFileListRequest = None,
            **kwargs
    ) -> List[BaseShareFile]:
        """get_share_file_list"""
        _deprecation_warning(kwargs)
        if body is None:
            body = GetShareFileListRequest(share_id=share_token.share_id, parent_file_id=parent_file_id, **kwargs)
        result = self._core_list_by_share(body, share_token)
        return list(result)

    @overload
    def get_share_file(
            self,
            file_id: str,
            share_token: GetShareTokenResponse,
            **kwargs
    ) -> BaseShareFile:
        """
        官方：获取分享文件
        :param file_id: [必选] 文件id
        :param share_token: [必选] 分享token
        :param kwargs: [可选] 其他参数
        :return: [BaseShareFile]

        用法示例：
        >>> from aligo import Aligo
        >>> ali = Aligo()
        >>> share = ali.share_file('<file_id>')
        >>> # noinspection PyShadowingNames
        >>> share_token = ali.get_share_token(share.share_id)
        >>> share_file = ali.get_share_file(share.file_id, share_token)
        >>> print(share_file)
        """

    @overload
    def get_share_file(self, body: GetShareFileRequest, share_token: GetShareTokenResponse) -> BaseShareFile:
        """
        官方：获取分享文件
        :param body: [必选] 请求体
        :param share_token: [必选] 分享token
        :return: [BaseShareFile]

        用法示例：
        >>> from aligo import Aligo, GetShareFileRequest
        >>> ali = Aligo()
        >>> share = ali.share_file('<file_id>')
        >>> # noinspection PyShadowingNames
        >>> share_token = ali.get_share_token(share.share_id)
        >>> # noinspection PyShadowingNames
        >>> body = GetShareFileRequest(share_id=share.share_id, file_id=share.file_id)
        >>> share_file = ali.get_share_file(body=body, share_token=share_token)
        >>> print(share_file)
        """

    def get_share_file(
            self,
            file_id: str = None,
            share_token: GetShareTokenResponse = None,
            body: GetShareFileRequest = None,
            **kwargs
    ) -> BaseShareFile:
        """get_share_file"""
        _deprecation_warning(kwargs)
        if body is None:
            body = GetShareFileRequest(share_id=share_token.share_id, file_id=file_id, **kwargs)
        return self._core_get_share_file(body, share_token)

    def get_by_file(
            self,
            file_id: str = None,
            share_token: GetShareTokenResponse = None,
            body: GetShareFileRequest = None,
            **kwargs
    ) -> BaseShareFile:
        """get_share_file"""
        _deprecation_warning(kwargs)
        if body is None:
            body = GetShareFileRequest(share_id=share_token.share_id, file_id=file_id, **kwargs)
        return self._core_get_by_share(body, share_token)

    @overload
    def get_share_link_download_url(
            self,
            file_id: str,
            share_token: GetShareTokenResponse,
            **kwargs
    ) -> GetShareLinkDownloadUrlResponse:
        """
        官方：获取分享文件下载链接
        :param file_id: [必选] 文件id
        :param share_token: [必选] 分享token
        :param kwargs: [可选] 其他参数
        :return: [GetShareLinkDownloadUrlResponse]

        用法示例：
        >>> from aligo import Aligo
        >>> ali = Aligo()
        >>> share = ali.share_file('<file_id>')
        >>> # noinspection PyShadowingNames
        >>> share_token = ali.get_share_token(share.share_id)
        >>> share_link_download_url = ali.get_share_link_download_url(share.file_id, share_token)
        >>> print(share_link_download_url)
        """

    @overload
    def get_share_link_download_url(
            self,
            body: GetShareLinkDownloadUrlRequest,
            share_token: GetShareTokenResponse
    ) -> GetShareLinkDownloadUrlResponse:
        """
        官方：获取分享文件下载链接
        :param body: [必选] 请求体
        :param share_token: [必选] 分享token
        :return: [GetShareLinkDownloadUrlResponse]

        用法示例：
        >>> from aligo import Aligo, GetShareLinkDownloadUrlRequest
        >>> ali = Aligo()
        >>> share = ali.share_file('<file_id>')
        >>> # noinspection PyShadowingNames
        >>> share_token = ali.get_share_token(share.share_id)
        >>> # noinspection PyShadowingNames
        >>> body = GetShareLinkDownloadUrlRequest(share_id=share.share_id, file_id=share.file_id)
        >>> share_link_download_url = ali.get_share_link_download_url(body=body, share_token=share_token)
        >>> print(share_link_download_url)
        """

    def get_share_link_download_url(
            self,
            file_id: str = None,
            share_token: GetShareTokenResponse = None,
            body: GetShareLinkDownloadUrlRequest = None,
            **kwargs
    ) -> GetShareLinkDownloadUrlResponse:
        """get_share_link_download_url"""
        _deprecation_warning(kwargs)
        if body is None:
            body = GetShareLinkDownloadUrlRequest(share_id=share_token.share_id, file_id=file_id, **kwargs)
        return self._core_get_share_link_download_url(body, share_token)

    @overload
    def share_file_saveto_drive(
            self,
            file_id: str,
            share_token: GetShareTokenResponse,
            to_parent_file_id: str = 'root',
            to_drive_id: str = None,
            new_name: str = None,
            **kwargs
    ) -> ShareFileSaveToDriveResponse:
        """
        官方：保存分享文件到指定的网盘
        :param file_id: [必选] 文件id
        :param share_token: [必选] 分享token
        :param to_parent_file_id: [必选] 目标父文件夹id，默认为根目录
        :param to_drive_id: [可选] 目标网盘id，默认为当前网盘
        :param new_name: [可选] 新文件名
        :param kwargs: [可选] 其他参数
        :return: [ShareFileSaveToDriveResponse]

        用法示例：
        >>> from aligo import Aligo
        >>> ali = Aligo()
        >>> share = ali.share_file('<file_id>')
        >>> # noinspection PyShadowingNames
        >>> share_token = ali.get_share_token(share.share_id)
        >>> share_file_saveto_drive = ali.share_file_saveto_drive(share.file_id, share_token)
        >>> print(share_file_saveto_drive)
        """

    @overload
    def share_file_saveto_drive(
            self,
            body: ShareFileSaveToDriveRequest,
            share_token: GetShareTokenResponse
    ) -> ShareFileSaveToDriveResponse:
        """
        官方：保存分享文件到指定的网盘
        :param body: [必选] 请求体
        :param share_token: [必选] 分享token
        :return: [ShareFileSaveToDriveResponse]

        用法示例：
        >>> from aligo import Aligo, ShareFileSaveToDriveRequest
        >>> ali = Aligo()
        >>> share = ali.share_file('<file_id>')
        >>> # noinspection PyShadowingNames
        >>> share_token = ali.get_share_token(share.share_id)
        >>> # noinspection PyShadowingNames
        >>> body = ShareFileSaveToDriveRequest(share_id=share.share_id, file_id=share.file_id)
        >>> share_file_saveto_drive = ali.share_file_saveto_drive(body=body,share_token=share_token)
        >>> print(share_file_saveto_drive)
        """

    def share_file_saveto_drive(
            self,
            file_id: str = None,
            share_token: GetShareTokenResponse = None,
            to_parent_file_id: str = 'root',
            to_drive_id: str = None,
            new_name: str = None,
            body: ShareFileSaveToDriveRequest = None,
            **kwargs
    ) -> ShareFileSaveToDriveResponse:
        """share_file_saveto_drive"""
        _deprecation_warning(kwargs)
        if body is None:
            body = ShareFileSaveToDriveRequest(
                share_id=share_token.share_id,
                file_id=file_id,
                to_parent_file_id=to_parent_file_id,
                to_drive_id=to_drive_id,
                new_name=new_name,
                **kwargs
            )
        return self._core_share_file_saveto_drive(body, share_token)

    @overload
    def batch_share_file_saveto_drive(
            self,
            file_id_list: List[str],
            share_token: GetShareTokenResponse,
            to_parent_file_id: str = 'root',
            to_drive_id: str = None,
            **kwargs
    ) -> List[BatchShareFileSaveToDriveResponse]:
        """
        官方：批量保存分享文件到指定的网盘
        :param file_id_list: [必选] 文件id列表
        :param share_token: [必选] 分享token
        :param to_parent_file_id: [必选] 目标父文件夹id，默认为根目录
        :param to_drive_id: [可选] 目标网盘id，默认为当前网盘
        :param kwargs: [可选] 其他参数
        :return: [List[BatchShareFileSaveToDriveResponse]]

        用法示例：
        >>> from aligo import Aligo
        >>> ali = Aligo()
        >>> share = ali.share_file('<file_id>')
        >>> # noinspection PyShadowingNames
        >>> share_token = ali.get_share_token(share.share_id)
        >>> batch_share_file_saveto_drive = ali.batch_share_file_saveto_drive(share.file_id_list, share_token)
        >>> print(batch_share_file_saveto_drive[0].file_id)
        """

    @overload
    def batch_share_file_saveto_drive(
            self, body: BatchShareFileSaveToDriveRequest,
            share_token: GetShareTokenResponse
    ) -> List[BatchShareFileSaveToDriveResponse]:
        """
        官方：批量保存分享文件到指定的网盘
        :param body: [必选] 请求体
        :param share_token: [必选] 分享token
        :return: [List[BatchShareFileSaveToDriveResponse]]

        用法示例：
        >>> from aligo import Aligo, BatchShareFileSaveToDriveRequest
        >>> ali = Aligo()
        >>> share = ali.share_file('<file_id>')
        >>> # noinspection PyShadowingNames
        >>> share_token = ali.get_share_token(share.share_id)
        >>> # noinspection PyShadowingNames
        >>> body = BatchShareFileSaveToDriveRequest(share_id=share.share_id, file_id_list=share.file_id_list)
        >>> batch_share_file_saveto_drive = ali.batch_share_file_saveto_drive(body=body,share_token=share_token)
        >>> print(batch_share_file_saveto_drive[0].file_id)
        """

    def batch_share_file_saveto_drive(
            self,
            file_id_list: List[str] = None,
            share_token: GetShareTokenResponse = None,
            to_parent_file_id: str = 'root',
            auto_rename: bool = True,
            to_drive_id: str = None,
            body: BatchShareFileSaveToDriveRequest = None,
            **kwargs,
    ) -> List[BatchShareFileSaveToDriveResponse]:
        """batch_share_file_saveto_drive"""
        _deprecation_warning(kwargs)
        if body is None:
            body = BatchShareFileSaveToDriveRequest(
                share_id=share_token.share_id,
                file_id_list=file_id_list,
                to_parent_file_id=to_parent_file_id,
                auto_rename=auto_rename,
                to_drive_id=to_drive_id,
            )
        result = self._core_batch_share_file_saveto_drive(body, share_token)
        return list(result)

    def share_file_save_all_to_drive(
            self,
            share_token: GetShareTokenResponse,
            to_parent_file_id: str = 'root',
            parent_file_id: str = 'root',
            auto_rename: bool = True,
            to_drive_id: str = None,
            **kwargs,
    ) -> List[BatchShareFileSaveToDriveResponse]:
        """保存所有分享文件到云盘"""
        _deprecation_warning(kwargs)
        file_list = self.get_share_file_list(share_token, parent_file_id=parent_file_id)
        result = self.batch_share_file_saveto_drive(
            [file.file_id for file in file_list],
            share_token,
            to_parent_file_id=to_parent_file_id,
            to_drive_id=to_drive_id,
            auto_rename=auto_rename,
        )
        return result

    def search_share_files(self, keyword: str, share_token: GetShareTokenResponse,
                           order_by: SearchFileOrderBy = 'name', order_direction: OrderDirection = 'DESC',
                           body: SearchShareFileRequest = None, **kwargs) -> List[BaseShareFile]:
        """在分享中搜索文件"""
        _deprecation_warning(kwargs)
        if body is None:
            body = SearchShareFileRequest(share_id=share_token.share_id, keyword=keyword,
                                          order_by=f'{order_by} {order_direction}', **kwargs)
        result = self._core_search_share_files(body, share_token)
        return list(result)

    def private_share_file(self, file_id: str, drive_id: str = None):
        """APP 中的快传，有效期 24 小时，只能一个人保存"""
        return self.private_share_files([file_id], drive_id)

    def private_share_files(self, file_id_list: List[str], drive_id: str = None):
        """APP 中的快传，有效期 24 小时，只能一个人保存"""
        if drive_id is None:
            drive_id = self.default_drive_id
        return self._core_private_share_files(PrivateShareRequest(
            drive_file_list=[
                DriveFile(file_id=file_id, drive_id=drive_id)
                for file_id in file_id_list
            ]
        ))
