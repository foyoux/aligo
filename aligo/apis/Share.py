"""todo"""
from typing import List

from aligo.core import *
from aligo.request import *
from aligo.response import *
from aligo.types import *


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

    def batch_cancel_share(self, share_id_list: List[str]) -> List[BatchResponse]:
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
