"""..."""
import traceback
from typing import Generic, List, Iterator, Dict
from typing import Union

import requests
import ujson

from aligo.auth import *
from aligo.config import *
from aligo.request import *
from aligo.response import *
from aligo.types import *


class BaseAligo(BaseClass):
    """Aliyundrive apis lib"""

    def __init__(self, auth: Optional[Auth] = None):
        self._auth: Auth = auth or Auth()
        self._session: requests.Session = self._auth.session
        self._token: Token = self._auth.token
        self._user: Optional[BaseUser] = None
        self._personal_info: Optional[GetPersonalInfoResponse] = None
        self._default_drive: Optional[BaseDrive] = None

    def _post(self, path: str, host: str = API_HOST, body: Union[DataType, Dict] = None) -> requests.Response:
        """..."""
        if body is None:
            body = {}
        elif isinstance(body, DataClass):
            body = body.__dict__
        # else:
        #     body = body

        if 'drive_id' in body and body['drive_id'] is None:
            # if exist attr drive_id and it is None, and set default_drive_id to it
            body['drive_id'] = self.default_drive_id

        return self._auth.post(path=path, host=host, body=body)

    def __hash__(self):
        """简化cacheout key的计算"""
        return self._token.user_id

    @property
    def default_drive_id(self):
        """..."""
        return self._token.default_drive_id

    @property
    def default_sbox_drive_id(self):
        """..."""
        return self._token.default_sbox_drive_id

    @property
    def user_name(self):
        """..."""
        return self._token.user_name

    @property
    def user_id(self):
        """..."""
        return self._token.user_id

    @property
    def device_id(self):
        """..."""
        return self._token.device_id

    @property
    def nick_name(self):
        """..."""
        return self._token.nick_name

    @classmethod
    def _result(cls, response: requests.Response,
                dcls: Generic[DataType],
                status_code: Union[List, int] = 200) -> Union[Null, DataType]:
        """
        Unified processing response
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
                return dcls(**ujson.loads(text))
            except TypeError:
                cls._debug_log(response)
                traceback.print_exc()
        # debug_log(response)
        return Null(response)

    def _list_file(self, PATH: str, body: DataType, ResponseType: Generic[DataType]) -> Iterator[BaseFile]:
        """..."""
        response = self._post(PATH, body=body)
        file_list = self._result(response, ResponseType)
        if isinstance(file_list, Null):
            yield file_list
            return
        for item in file_list.items:
            yield item
        if file_list.next_marker != '':
            body.marker = file_list.next_marker
            for it in self._list_file(PATH=PATH, body=body, ResponseType=ResponseType):
                yield it

    def get_file(self, body: GetFileRequest) -> BaseFile:
        """获取文件信息, 其他类中可能会用到, 所以放到基类中"""
        response = self._post(V2_FILE_GET, body=body)
        return self._result(response, BaseFile)
