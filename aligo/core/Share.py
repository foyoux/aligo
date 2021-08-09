"""分享相关"""
from dataclasses import asdict
from typing import Iterator

from aligo.core import *
from aligo.core.Config import *
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

    def batch_cancel_share(self, body: BatchCancelShareRequest) -> Iterator[BatchSubResponse]:
        """批量取消分享"""
        yield from self.batch_request(BatchRequest(
                requests=[BatchSubRequest(
                    id=share_id,
                    url='/share_link/cancel',
                    body=CancelShareLinkRequest(
                        share_id=share_id
                    )
                ) for share_id in body.share_id_list]
        ), CancelShareLinkResponse)

    def get_share_list(self, body: GetShareLinkListRequest = None) -> Iterator[ShareLinkSchema]:
        """获取自己的分享链接

        :param body: GetShareLinkListRequest对象
        :return: ShareLinkSchema对象的迭代器
        """
        yield from self._list_file(ADRIVE_V2_SHARE_LINK_LIST, body, GetShareLinkListResponse)

    # 处理其他人的分享
    def get_share_info(self, body: GetShareInfoRequest) -> GetShareInfoResponse:
        """..."""
        response = self._post(ADRIVE_V2_SHARE_LINK_GET_SHARE_BY_ANONYMOUS, body=body)
        share_info = self._result(response, GetShareInfoResponse)
        return share_info

    def get_share_token(self, body: GetShareTokenRequest) -> GetShareTokenResponse:
        """..."""
        response = self._post(V2_SHARE_LINK_GET_SHARE_TOKEN, body=body)
        share_token = self._result(response, GetShareTokenResponse)
        return share_token

    def get_share_file_list(self, body: GetShareFileListRequest, x_share_token: str) -> Iterator[BaseShareFile]:
        """..."""
        response = self._auth.post(V2_FILE_LIST, body=asdict(body), headers={'x-share-token': x_share_token})
        file_list = self._result(response, GetShareFileListResponse)
        if isinstance(file_list, Null):
            yield file_list
            return
        yield from file_list.items
        if file_list.next_marker != '':
            body.marker = file_list.next_marker
            yield from self.get_share_file_list(body=body, x_share_token=x_share_token)

    def get_share_file(self, body: GetShareFileRequest, x_share_token: str) -> BaseShareFile:
        """..."""
        response = self._auth.post(V2_FILE_GET, body=asdict(body), headers={'x-share-token': x_share_token})
        share_file = self._result(response, BaseShareFile)
        return share_file

    def get_share_link_download_url(self, body: GetShareLinkDownloadUrlRequest,
                                    x_share_token: str) -> GetShareLinkDownloadUrlResponse:
        """..."""
        response = self._auth.post(V2_FILE_GET_SHARE_LINK_DOWNLOAD_URL, body=asdict(body),
                                   headers={'x-share-token': x_share_token})
        download_url = self._result(response, GetShareLinkDownloadUrlResponse)
        return download_url

    def share_file_saveto_drive(self, body: ShareFileSaveToDriveRequest,
                                x_share_token: str) -> ShareFileSaveToDriveResponse:
        """..."""
        if body.to_drive_id is None:
            body.to_drive_id = self.default_drive_id
        response = self._auth.post(V2_FILE_COPY, body=asdict(body), headers={'x-share-token': x_share_token})
        return self._result(response, ShareFileSaveToDriveResponse, [201, 202])

    def batch_share_file_saveto_drive(self, body: BatchShareFileSaveToDriveRequest,
                                      x_share_token: str) -> Iterator[BatchShareFileSaveToDriveResponse]:
        """..."""
        if body.to_drive_id is None:
            body.to_drive_id = self.default_drive_id

        for file_id_list in self._list_split(body.file_id_list, self.BATCH_COUNT):
            response = self._auth.post(ADRIVE_V2_BATCH, body={
                "requests": [
                    {
                        "body": asdict(ShareFileSaveToDriveRequest(
                            file_id=file_id,
                            share_id=body.share_id,
                            to_parent_file_id=body.to_parent_file_id,
                            to_drive_id=body.to_drive_id,
                            overwrite=body.overwrite,
                            auto_rename=body.auto_rename,
                        )),
                        "headers": {
                            'Content-Type': 'application/json',
                        },
                        "id": file_id,
                        "method": 'POST',
                        "url": '/file/copy'
                    } for file_id in file_id_list
                ],
                "resource": 'file'
            }, headers={'x-share-token': x_share_token})

            if response.status_code != 200:
                yield Null(response)
                return

            for batch in response.json()['responses']:
                i = BatchSubResponse(**batch)
                if i.body:
                    i.body = BatchShareFileSaveToDriveResponse(**i.body)
                yield i
