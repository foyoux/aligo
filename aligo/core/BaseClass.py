"""..."""
import logging
from typing import NoReturn, List

import requests

from aligo.types import DataType


class BaseClass:
    """..."""

    @classmethod
    def _debug_log(cls, response: requests.Response) -> NoReturn:
        """..."""
        r = response.request
        logging.debug(f'[method status_code] {r.method} {response.status_code}')
        logging.debug(f'[url] {response.url}')
        logging.debug(f'[headers] {r.headers}')
        logging.debug(f'[request body] {r.body}')
        logging.debug(f'[response body] {response.text}')

    @classmethod
    def _error_log_exit(cls, response: requests.Response) -> NoReturn:
        """打印错误日志并退出"""
        cls._debug_log(response)
        exit(-1)

    @staticmethod
    def _list_split(ll: List[DataType], n: int) -> List[List[DataType]]:
        rt = []
        for i in range(0, len(ll), n):
            rt.append(ll[i:i + n])
        return rt
