"""todo"""
from typing import Iterator, List

from aligo.config import *
from aligo.core import *
from aligo.request import *
from aligo.response import *
from aligo.types import *


class Share(BaseAligo):
    """分享相关"""

    def share_file(self, body: CreateShareLinkRequest) -> CreateShareLinkResponse:
        """分享文件, 支持批量分享

        目前(2021年07月17日)官方只开放分享部分类型文件
        """
        response = self._post(ADRIVE_V2_SHARE_LINK_CREATE, body=body)
        return self._result(response, CreateShareLinkResponse)

    def update_share(self, body: UpdateShareLinkRequest) -> UpdateShareLinkResponse:
        """更新分享, 如更新 密码, 有效期 等"""
        response = self._post(V2_SHARE_LINK_UPDATE, body=body)
        return self._result(response, UpdateShareLinkResponse)

    def cancel_share(self, body: CancelShareLinkRequest) -> CancelShareLinkResponse:
        """取消分享"""
        response = self._post(ADRIVE_V2_SHARE_LINK_CANCEL, body=body)
        return self._result(response, CancelShareLinkResponse)

    def batch_cancel_share(self, body: List[CancelShareLinkRequest]):
        """批量取消分享"""
        requests = []
        for i in body:
            requests.append(
                {
                    "body": {
                        "share_id": i.share_id
                    },
                    "headers": {
                        "Content-Type": "application/json"
                    },
                    "id": "dunNKhtSmUE",
                    "method": "POST",
                    "url": "/share_link/cancel"
                }
            )
        response = self._post(ADRIVE_V2_BATCH, body={"requests": requests, "resource": "file"})

    def get_share_list(self, body: GetShareLinkListRequest = None) -> Iterator[ShareLinkSchema]:
        """获取自己的分享链接

        :param body: GetShareLinkListRequest对象
        :return: ShareLinkSchema对象的迭代器
        """
        response = self._post(ADRIVE_V2_SHARE_LINK_LIST, body=body)
        file_list = self._result(response, GetShareLinkListResponse)
        if isinstance(file_list, Null):
            yield file_list
            return
        for item in file_list.items:
            yield item
        if file_list.next_marker != '':
            body.marker = file_list.next_marker
            for it in self.get_share_list(body=body):
                yield it
