"""..."""
import logging
from typing import NoReturn

import requests


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
