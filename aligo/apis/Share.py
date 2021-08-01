"""分享相关"""
from typing import List

from aligo.core import *
from aligo.request import *
from aligo.response import *
from aligo.types import *
from aligo.types.Enum import *


class Share(Core):
    """..."""

    def share_file(self,
                   file_id_list: List[str],
                   share_name: str = None,
                   share_pwd: str = None,
                   expiration: str = None,
                   drive_id: str = None,
                   description: str = None) -> CreateShareLinkResponse:
        """..."""
        body = CreateShareLinkRequest(
            file_id_list=file_id_list,
            share_name=share_name,
            share_pwd=share_pwd,
            expiration=expiration,
            drive_id=drive_id,
            description=description,
        )
        return super(Share, self).share_file(body)

    def update_share(self,
                     share_id: str,
                     share_pwd: str = None,
                     expiration: str = None,
                     description: str = None,
                     share_name: str = None) -> UpdateShareLinkResponse:
        """更新分享, 如更新 密码, 有效期 等"""
        body = UpdateShareLinkRequest(
            share_id=share_id,
            share_pwd=share_pwd,
            expiration=expiration,
            description=description,
            share_name=share_name,
        )
        return super(Share, self).update_share(body)

    def cancel_share(self, share_id: str) -> CancelShareLinkResponse:
        """取消分享"""
        body = CancelShareLinkRequest(share_id=share_id)
        return super(Share, self).cancel_share(body)

    def batch_cancel_share(self, share_id_list: List[str]) -> List[BatchSubResponse]:
        """批量取消分享"""
        body = BatchCancelShareRequest(share_id_list=share_id_list)
        result = super(Share, self).batch_cancel_share(body)
        return [i for i in result]

    def get_share_list(self,
                       limit: int = 100,
                       order_by: GetShareLinkListOrderBy = 'created_at',
                       order_direction: OrderDirection = 'DESC',
                       include_canceled: bool = False) -> List[ShareLinkSchema]:
        """获取自己的分享链接"""
        body = GetShareLinkListRequest(
            limit=limit,
            order_by=order_by,
            order_direction=order_direction,
            include_canceled=include_canceled,
        )
        result = super(Share, self).get_share_list(body)
        return [i for i in result]

    # 处理其他人的分享
    def get_share_info(self, share_id: str) -> GetShareInfoResponse:
        """..."""
        body = GetShareInfoRequest(share_id=share_id)
        return super(Share, self).get_share_info(body)

    def get_share_token(self, share_id: str, share_pwd: str = '') -> GetShareTokenResponse:
        """..."""
        body = GetShareTokenRequest(share_id=share_id, share_pwd=share_pwd)
        return super(Share, self).get_share_token(body)

    def get_share_file_list(
            self,
            share_id: str,
            share_token: str,
            body: GetShareFileListRequest = None,
            **kwargs
    ) -> List[BaseShareFile]:
        """..."""
        if body is None:
            body = GetShareFileListRequest(share_id=share_id, **kwargs)
        result = super(Share, self).get_share_file_list(body, share_token)
        return [i for i in result]

    def get_share_file(
            self,
            share_id: str,
            file_id: str,
            share_token: str,
            body: GetShareFileRequest = None,
            **kwargs
    ) -> BaseShareFile:
        """..."""
        if body is None:
            body = GetShareFileRequest(share_id=share_id, file_id=file_id, **kwargs)
        return super(Share, self).get_share_file(body, share_token)

    def get_share_link_download_url(
            self,
            share_id: str,
            file_id: str,
            share_token: str,
            body: GetShareLinkDownloadUrlRequest = None,
            **kwargs
    ) -> GetShareLinkDownloadUrlResponse:
        """..."""
        if body is None:
            body = GetShareLinkDownloadUrlRequest(share_id=share_id, file_id=file_id, **kwargs)
        return super(Share, self).get_share_link_download_url(body, share_token)

    def share_file_saveto_drive(
            self,
            share_id: str,
            file_id: str,
            share_token: str,
            to_parent_file_id: str = 'root',
            to_drive_id: str = None,
            new_name: str = None,
            body: ShareFileSaveToDriveRequest = None,
            **kwargs
    ) -> ShareFileSaveToDriveResponse:
        """..."""
        if body is None:
            body = ShareFileSaveToDriveRequest(
                share_id=share_id,
                file_id=file_id,
                to_parent_file_id=to_parent_file_id,
                to_drive_id=to_drive_id,
                new_name=new_name,
                **kwargs
            )
        return super(Share, self).share_file_saveto_drive(body, share_token)

    def batch_share_file_saveto_drive(
            self,
            share_id: str,
            file_id_list: List[str],
            share_token: str,
            to_parent_file_id: str = 'root',
            to_drive_id: str = None,
            body: BatchShareFileSaveToDriveRequest = None,
            **kwargs
    ) -> List[BatchShareFileSaveToDriveResponse]:
        """..."""
        if body is None:
            body = BatchShareFileSaveToDriveRequest(
                share_id=share_id,
                file_id_list=file_id_list,
                to_parent_file_id=to_parent_file_id,
                to_drive_id=to_drive_id,
                **kwargs
            )
        result = super(Share, self).batch_share_file_saveto_drive(body, share_token)
        return [i for i in result]
