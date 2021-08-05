"""认证模块"""

import base64
import json
import logging
import os
import tempfile
import time
from dataclasses import asdict
from pathlib import Path
from typing import Callable, overload, List, NoReturn, Dict
from urllib import parse

import coloredlogs
import qrcode
import qrcode_terminal
import requests

from aligo.core.Config import *
from aligo.types import *
from aligo.types.Enum import *

_aligo = Path.home().joinpath('.aligo')
_aligo.mkdir(parents=True, exist_ok=True)


def get_configurations() -> List[str]:
    """获取配置文件列表"""
    list_: List[str] = []
    file_: os.DirEntry
    for file_ in os.scandir(_aligo):
        list_.append(os.path.splitext(file_.name)[0])
    return list_


class Auth:
    """..."""

    def debug_log(self, response: requests.Response) -> NoReturn:
        """打印错误日志, 便于分析调试"""
        r = response.request
        self.log.warning(f'[method status_code] {r.method} {response.status_code}')
        self.log.warning(f'[url] {response.url}')
        self.log.warning(f'[headers] {r.headers}')
        self.log.warning(f'[request body] {r.body}')
        self.log.warning(f'[response body] {response.text[:1024]}')

    def error_log_exit(self, response: requests.Response) -> NoReturn:
        """打印错误日志并退出"""
        self.debug_log(response)
        exit(-1)

    @overload
    def __init__(
            self,
            name: str = 'aligo',
            show: Callable[[str], NoReturn] = None,
            level=logging.DEBUG,
            loglog: bool = False
    ):
        """扫描二维码登录"""

    @overload
    def __init__(
            self,
            name: str = 'aligo',
            refresh_token: str = None,
            level=logging.DEBUG,
            loglog: bool = False
    ):
        """refresh_token 登录"""

    def __init__(
            self, name: str = 'aligo',
            refresh_token: str = None,
            show: Callable[[str], NoReturn] = None,
            level: int = logging.DEBUG,
            loglog: bool = False
    ):
        """登录验证

        :param name: (可选, 默认: aligo) 配置文件名称, 便于使用不同配置文件进行身份验证
        :param refresh_token:
        :param show: (可选) 显示二维码的函数
        :param level: (可选) 控制控制台输出
        :param loglog: (可选) 控制文件输出
        """
        self._name = _aligo.joinpath(f'{name}.json')

        self.log = logging.getLogger(f'{__name__}:{name}')

        # if level <= logging.DEBUG:
        #     fmt = '%(asctime)s.%(msecs)03d %(levelname)5s %(message)s :%(filename)s %(lineno)s'
        # else:
        fmt = '%(asctime)s.%(msecs)03d %(levelname)5s %(message)s'

        coloredlogs.install(
            level=level,
            logger=self.log,
            milliseconds=True,
            datefmt='%X',
            fmt=fmt
        )

        if loglog:
            logfile = logging.FileHandler(filename=str(self._name)[:-5] + '.log', mode='w', encoding='utf-8')
            logfile.setLevel(logging.DEBUG)
            formatter = logging.Formatter('%(asctime)s  %(filename)s  %(funcName)s : %(levelname)s  %(message)s',
                                          datefmt='%F %X')
            logfile.setFormatter(formatter)
            self.log.addHandler(logfile)

        self.log.info(f'Config {self._name}')
        self.log.info(f'日志等级 {logging.getLevelName(level)}')

        #
        self.session = requests.session()
        self.session.params.update(UNI_PARAMS)  # type:ignore
        self.session.headers.update(UNI_HEADERS)

        self.session.get(AUTH_HOST + V2_OAUTH_AUTHORIZE, params={
            'login_type': 'custom',
            'response_type': 'code',
            'redirect_uri': 'https://www.aliyundrive.com/sign/callback',
            'client_id': CLIENT_ID,
            'state': r'{"origin":"file://"}',
            # 'state': '{"origin":"https://www.aliyundrive.com"}',
        }, stream=True).close()

        #
        SESSIONID = self.session.cookies.get('SESSIONID')
        self.log.debug(f'SESSIONID {SESSIONID}')

        #
        self.token: Optional[Token] = None
        if show is None:
            if os.name == 'nt':
                self.log.debug('Windows 操作系统')
                show = self._show_windows
            else:
                self.log.debug('类 Unix 操作系统')
                show = self._show_console
        self._show = show

        if self._name.exists():
            self.log.info(f'加载配置文件 {self._name}')
            self.token = Token(**json.load(self._name.open()))
        else:
            if refresh_token:
                self.log.debug('使用 refresh_token 方式登录')
                self._refesh_token(refresh_token)
                return
            self.log.info('使用 扫描二维码 方式登录')
            self._login()

        #
        self.session.headers.update({
            'Authorization': f'Bearer {self.token.access_token}'
        })

    def _save(self) -> NoReturn:
        """保存配置文件"""
        self.log.info(f'保存配置文件: {self._name}')
        json.dump(asdict(self.token), self._name.open('w'))

    def _login(self):
        """登录"""
        self.log.info('开始登录 ...')
        response = self._login_by_qrcode()

        if response.status_code != 200:
            self.log.error('登录失败 ~')
            self.error_log_exit(response)

        bizExt = response.json()['content']['data']['bizExt']
        bizExt = base64.b64decode(bizExt).decode('gb18030')
        accessToken = json.loads(bizExt)['pds_login_result']['accessToken']

        # 使用accessToken持久化身份认证
        response = self.session.post(
            AUTH_HOST + V2_OAUTH_TOKEN_LOGIN,
            json={
                'token': accessToken
            }
        )
        goto = response.json()['goto']
        code: str = parse.parse_qs(parse.urlparse(goto).query)['code'][0]  # type: ignore

        response = self.session.post(
            WEBSV_HOST + TOKEN_GET,
            json={
                'code': code
            }
        )

        if response.status_code != 200:
            self.log.error(f'登陆失败 ~')
            self.error_log_exit(response)

        self.token = Token(**response.json())

        #
        self.log.info('登录成功 ~')
        self.log.info(
            f'username: {self.token.user_name} nickname: {self.token.nick_name} user_id: {self.token.user_id}')

        # 保存
        self._save()

    def _login_by_qrcode(self) -> requests.Response:
        """二维码登录"""
        response = self.session.get(
            PASSPORT_HOST + NEWLOGIN_QRCODE_GENERATE_DO
        )
        data = response.json()['content']['data']
        self._show(data['codeContent'])
        while True:
            response = self.session.post(
                PASSPORT_HOST + NEWLOGIN_QRCODE_QUERY_DO,
                data=data
            )
            login_data = response.json()['content']['data']
            qrCodeStatus = login_data['qrCodeStatus']
            if qrCodeStatus == 'NEW':
                self.log.info('等待扫描二维码 ...')
            elif qrCodeStatus == 'SCANED':
                self.log.info('已扫描, 等待确认 ...')
            elif qrCodeStatus == 'CONFIRMED':
                self.log.info(f'已确认 (你可以关闭二维码图像了.)')
                return response
            else:
                self.log.warning('未知错误: 可能二维码已经过期.')
                self.error_log_exit(response)
            time.sleep(2)

    def _refesh_token(self, refresh_token=None):
        """刷新 token"""
        if refresh_token is None:
            refresh_token = self.token.refresh_token
        self.log.info('刷新 token ...')
        response = self.session.post(
            WEBSV_HOST + TOKEN_REFRESH,
            json={'refresh_token': refresh_token}
        )
        if response.status_code == 200:
            self.token = Token(**response.json())
            self.session.headers.update({
                'Authorization': f'Bearer {self.token.access_token}'
            })
            self._save()
        else:
            self.log.error('刷新 token 失败 ~')
            self.debug_log(response)
            self._login()
            # error_log_exit(response)

    def request(self, method: str, url: str,
                params: Dict = None, headers: Dict = None, data=None,
                files: object = None, verify: bool = None, body: Dict = None) -> requests.Response:
        """统一请求方法"""
        # 删除值为None的键
        if body is not None:
            body = {k: v for k, v in body.items() if v is not None}

        if data is not None and isinstance(data, dict):
            data = {k: v for k, v in data.items() if v is not None}

        for i in range(3):
            response = self.session.request(method=method, url=url, params=params,
                                            data=data, headers=headers, files=files,
                                            verify=verify, json=body)
            status_code = response.status_code
            self.log.info(
                f'{response.request.method} {response.url} {status_code} {response.headers.get("Content-Length", 0)}'
            )
            if status_code == 401 or (
                    # aims search 手机端apis
                    status_code == 400 and response.text == 'AccessToken is invalid. AccessTokenExpired'
            ):
                self._refesh_token()
                continue

            return response

        self.log.info(f'重试3次仍旧失败~')
        self.error_log_exit(response)

    def get(self, path: str, host: str = API_HOST, params: dict = None, headers: dict = None,
            verify: bool = None) -> requests.Response:
        """..."""
        return self.request(method='GET', url=host + path, params=params,
                            headers=headers, verify=verify)

    def post(self, path: str, host: str = API_HOST, params: dict = None, headers: dict = None, data: dict = None,
             files=None, verify: bool = None, body: dict = None) -> requests.Response:
        """..."""
        return self.request(method='POST', url=host + path, params=params, data=data,
                            headers=headers, files=files, verify=verify, body=body)

    @staticmethod
    def _show_console(qr_link: str) -> NoReturn:
        """
        在控制台上显示二维码
        :param qr_link: 二维码链接
        :return: NoReturn
        """
        qrcode_terminal.draw(qr_link)

    @staticmethod
    def _show_windows(qr_link: str) -> NoReturn:
        """
        通过 *.png 的关联应用程序显示 qrcode
        :param qr_link: 二维码链接
        :return: NoReturn
        """
        qr_img = qrcode.make(qr_link)
        png = tempfile.mktemp('.png')
        qr_img.save(png)
        os.startfile(png)
