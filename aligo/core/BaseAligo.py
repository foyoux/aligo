"""..."""
import json
import subprocess
import traceback
from dataclasses import asdict
from typing import Generic, List, Iterator, Dict, Callable
from typing import Union

import requests

from aligo.core import *
from aligo.core.Config import *
from aligo.request import *
from aligo.response import *
from aligo.types import *
from aligo.types.DataClass import DataType
from aligo.types.Enum import *


class BaseAligo:
    """..."""

    def __init__(self, auth: Optional[Auth] = None, use_aria2: bool = False):
        self._auth: Auth = auth or Auth()
        self._session: requests.Session = self._auth.session
        self._token: Token = self._auth.token
        self._user: Optional[BaseUser] = None
        self._personal_info: Optional[GetPersonalInfoResponse] = None
        self._default_drive: Optional[BaseDrive] = None
        try:
            subprocess.run(['aria2c', '-h'], capture_output=True)
            self._has_aria2c = use_aria2
        except FileNotFoundError:
            self._has_aria2c = False

    def _post(self, path: str, host: str = API_HOST, body: Union[DataType, Dict] = None) -> requests.Response:
        """统一处理数据类型和 drive_id"""
        if body is None:
            body = {}
        elif isinstance(body, DataClass):
            body = asdict(body)

        if 'drive_id' in body and body['drive_id'] is None:
            # 如果存在 attr drive_id 并且它是 None，并将 default_drive_id 设置为它
            body['drive_id'] = self.default_drive_id

        return self._auth.post(path=path, host=host, body=body)

    @property
    def default_drive_id(self):
        """默认 drive_id"""
        return self._token.default_drive_id

    @property
    def default_sbox_drive_id(self):
        """默认保险箱 drive_id"""
        return self._token.default_sbox_drive_id

    @property
    def user_name(self):
        """用户名"""
        return self._token.user_name

    @property
    def user_id(self):
        """用户 id"""
        return self._token.user_id

    @property
    def nick_name(self):
        """昵称"""
        return self._token.nick_name

    def _result(self, response: requests.Response,
                dcls: Generic[DataType],
                status_code: Union[List, int] = 200) -> Union[Null, DataType]:
        """统一处理响应

        :param response:
        :param dcls:
        :param status_code:
        :return:
        """
        if isinstance(status_code, int):
            status_code = [status_code]
        if response.status_code in status_code:
            text = response.text
            if not text.startswith('{'):
                return dcls()
            try:
                return dcls(**json.loads(text))
            except TypeError:
                self._auth.debug_log(response)
                traceback.print_exc()
        self._auth.log.warning(f'{response.status_code} {response.text}')
        return Null(response)

    def _list_file(self, PATH: str, body: DataClass, ResponseType: Callable) -> Iterator[DataType]:
        """枚举文件: 用于统一处理 1.文件列表 2.搜索文件列表 3.收藏列表 4.回收站列表"""
        response = self._post(PATH, body=body)
        file_list = self._result(response, ResponseType)
        if isinstance(file_list, Null):
            yield file_list
            return
        for item in file_list.items:
            yield item
        if file_list.next_marker != '':
            body.marker = file_list.next_marker
            yield from self._list_file(PATH=PATH, body=body, ResponseType=ResponseType)

    def _core_get_file(self, body: GetFileRequest) -> BaseFile:
        """获取文件信息, 其他类中可能会用到, 所以放到基类中"""
        response = self._post(V2_FILE_GET, body=body)
        return self._result(response, BaseFile)

    def get_personal_info(self) -> GetPersonalInfoResponse:
        """..."""
        response = self._post(V2_DATABOX_GET_PERSONAL_INFO)
        return self._result(response, GetPersonalInfoResponse)

    _BATCH_COUNT = 100

    @staticmethod
    def _list_split(ll: List[DataType], n: int) -> List[List[DataType]]:
        rt = []
        for i in range(0, len(ll), n):
            rt.append(ll[i:i + n])
        return rt

    def batch_request(self, body: BatchRequest, body_type: DataType):
        """..."""
        for request_list in self._list_split(body.requests, self._BATCH_COUNT):
            response = self._post(V2_BATCH, body={
                "requests": [
                    {
                        "body": asdict(request.body),
                        "headers": request.headers,
                        "id": request.id,
                        "method": request.method,
                        "url": request.url
                    } for request in request_list
                ],
                "resource": body.resource
            })

            if response.status_code != 200:
                yield Null(response)
                return

            for batch in response.json()['responses']:
                i = BatchSubResponse(**batch)
                if i.body:
                    try:
                        # 不是都会成功
                        # eg: {'code': 'AlreadyExist.File', 'message': "The resource file has already exists. drive has the same file, can't update, file_id 609887cca951bf4feca54c6ebd0a91a03b826949"}
                        # status 409
                        i.body = body_type(**i.body)
                    except TypeError:
                        # self._auth.log.warning(i)
                        pass
                yield i
