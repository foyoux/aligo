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

    def share_link_extract_code(self, content: str) -> ShareLinkExtractCodeResponse:
        response = self._post(ADRIVE_V2_SHARE_LINK_EXTRACT_CODE, body={
            'content': content
        })
        return self._result(response, ShareLinkExtractCodeResponse, field='data')

    def _core_share_file(self, body: CreateShareLinkRequest) -> CreateShareLinkResponse:
        """分享文件, 支持批量分享

        目前(2021年07月17日)官方只开放分享部分类型文件
        """
        response = self._post(ADRIVE_V2_SHARE_LINK_CREATE, body=body)
        return self._result(response, CreateShareLinkResponse)

    def _core_update_share(self, body: UpdateShareLinkRequest) -> UpdateShareLinkResponse:
        """更新分享, 如更新 密码, 有效期 等"""
        response = self._post(V2_SHARE_LINK_UPDATE, body=body)
        return self._result(response, UpdateShareLinkResponse)

    def _core_cancel_share(self, body: CancelShareLinkRequest) -> CancelShareLinkResponse:
        """取消分享"""
        response = self._post(ADRIVE_V2_SHARE_LINK_CANCEL, body=body)
        return self._result(response, CancelShareLinkResponse)

    def _core_batch_cancel_share(self, body: BatchCancelShareRequest) -> Iterator[BatchSubResponse]:
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

    def _core_get_share_list(self, body: GetShareLinkListRequest = None) -> Iterator[ShareLinkSchema]:
        """获取自己的分享链接

        :param body: GetShareLinkListRequest对象
        :return: ShareLinkSchema对象的迭代器
        """
        yield from self._list_file(ADRIVE_V3_SHARE_LINK_LIST, body, GetShareLinkListResponse)

    # 处理其他人的分享
    def _core_get_share_info(self, body: GetShareInfoRequest) -> GetShareInfoResponse:
        """..."""
        response = self._post(ADRIVE_V2_SHARE_LINK_GET_SHARE_BY_ANONYMOUS, body=body, ignore_auth=True)
        share_info = self._result(response, GetShareInfoResponse)
        return share_info

    def _core_get_share_token(self, body: GetShareTokenRequest) -> GetShareTokenResponse:
        """..."""
        # noinspection PyProtectedMember
        response = self._post(V2_SHARE_LINK_GET_SHARE_TOKEN, body=body, ignore_auth=True)
        share_token: GetShareTokenResponse = self._result(response, GetShareTokenResponse)
        share_token.share_id = body.share_id
        share_token.share_pwd = body.share_pwd
        return share_token

    def _core_get_share_file_list(
            self,
            body: GetShareFileListRequest,
            x_share_token: GetShareTokenResponse
    ) -> Iterator[BaseShareFile]:
        """..."""
        response = self._auth.post(ADRIVE_V3_FILE_LIST, body=asdict(body), headers={'x-share-token': x_share_token},
                                   ignore_auth=True)
        file_list = self._result(response, GetShareFileListResponse)
        if isinstance(file_list, Null):
            yield file_list
            return
        yield from file_list.items
        if file_list.next_marker != '':
            body.marker = file_list.next_marker
            yield from self._core_get_share_file_list(body=body, x_share_token=x_share_token)

    def _core_list_by_share(
            self,
            body: GetShareFileListRequest,
            x_share_token: GetShareTokenResponse
    ) -> Iterator[BaseShareFile]:
        """..."""
        response = self._auth.post(ADRIVE_V2_FILE_LIST_BY_SHARE, body=asdict(body),
                                   headers={'x-share-token': x_share_token}, ignore_auth=True)
        file_list = self._result(response, GetShareFileListResponse)
        if isinstance(file_list, Null):
            yield file_list
            return
        yield from file_list.items
        if file_list.next_marker != '':
            body.marker = file_list.next_marker
            yield from self._core_list_by_share(body=body, x_share_token=x_share_token)

    def _core_get_share_file(
            self,
            body: GetShareFileRequest,
            x_share_token: GetShareTokenResponse
    ) -> BaseShareFile:
        """..."""
        response = self._auth.post(V2_FILE_GET, body=asdict(body), headers={'x-share-token': x_share_token},
                                   ignore_auth=True)
        share_file = self._result(response, BaseShareFile)
        return share_file

    def _core_get_by_share(
            self,
            body: GetShareFileRequest,
            x_share_token: GetShareTokenResponse
    ) -> BaseShareFile:
        """..."""
        response = self._auth.post(ADRIVE_V2_FILE_GET_BY_SHARE, body=asdict(body),
                                   headers={'x-share-token': x_share_token},
                                   ignore_auth=True)
        share_file = self._result(response, BaseShareFile)
        return share_file

    def _core_get_share_link_download_url(
            self,
            body: GetShareLinkDownloadUrlRequest,
            x_share_token: GetShareTokenResponse
    ) -> GetShareLinkDownloadUrlResponse:
        """..."""
        response = self._auth.post(
            V2_FILE_GET_SHARE_LINK_DOWNLOAD_URL,
            body=asdict(body),
            headers={'x-share-token': x_share_token})
        download_url = self._result(response, GetShareLinkDownloadUrlResponse)
        return download_url

    def _core_share_file_saveto_drive(
            self, body: ShareFileSaveToDriveRequest,
            x_share_token: GetShareTokenResponse
    ) -> ShareFileSaveToDriveResponse:
        """..."""
        if body.to_drive_id is None:
            body.to_drive_id = self.default_drive_id
        response = self._auth.post(V2_FILE_COPY, body=asdict(body), headers={'x-share-token': x_share_token})
        return self._result(response, ShareFileSaveToDriveResponse, [201, 202])

    def _core_batch_share_file_saveto_drive(
            self, body: BatchShareFileSaveToDriveRequest,
            x_share_token: GetShareTokenResponse
    ) -> Iterator[BatchShareFileSaveToDriveResponse]:
        """..."""
        if body.to_drive_id is None:
            body.to_drive_id = self.default_drive_id

        for file_id_list in self._list_split(body.file_id_list, self._BATCH_COUNT):
            response = self._auth.post(ADRIVE_V2_BATCH, body={
                "requests": [
                    {
                        "body": asdict(ShareFileSaveToDriveRequest(
                            file_id=file_id,
                            share_id=body.share_id,
                            to_parent_file_id=body.to_parent_file_id,
                            to_drive_id=body.to_drive_id,
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
                i = DataClass.fill_attrs(BatchSubResponse, batch)
                if i.body:
                    # noinspection PyArgumentList
                    i.body = DataClass.fill_attrs(BatchShareFileSaveToDriveResponse, i.body)
                yield i

    def _core_search_share_files(self, body: SearchShareFileRequest, share_token) -> Iterator[BaseShareFile]:
        """
        关于 query 的语法, 参考下段代码
        {
            key: "getPDSSearchQuery", value: function () {
                var n = ['name match "'.concat(this.queryToSearch, '"')];
                return this.filter && ("folder" === this.filter ? n.push('type = "'.concat(this.filter, '"'))
                : n.push('category = "'.concat(this.filter, '"'))), n.join(" and ")
            }
        }
        eg: 'name match "epub"'
        eg: 'name match "epub" and category = "image"'
        category : BaseFileCategory
        """
        yield from self._list_file(
            RECOMMEND_V1_SHARELINK_SEARCH, body, SearchShareFileResponse, headers={'x-share-token': share_token})

    def _core_private_share_files(self, body: PrivateShareRequest) -> PrivateShareResponse:
        response = self._post(ADRIVE_V1_SHARE_CREATE, body=body)
        return self._result(response, PrivateShareResponse)
