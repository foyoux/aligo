"""todo 解析其他客户端地址"""

from typing import Union, overload

import yaml

from aligo.core import *
from aligo.types import *


class Client(BaseAligo):
    """..."""

    @overload
    def get_latest_win32_client(self) -> ClientInfo:
        """..."""

    @overload
    def get_latest_win32_client(self) -> Null:
        """..."""

    def get_latest_win32_client(self) -> Union[ClientInfo, Null]:
        """获取最新win32客户端"""
        response = self._auth.get(path='/manifest/dtron/aDrive/win32/ia32/latest.yml', host='https://im.dingtalk.com')
        if response.status_code == 200:
            return ClientInfo(**yaml.safe_load(response.text))
        return Null(response)
