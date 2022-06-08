"""认证模块"""
import _thread
import base64
import json
import logging
import os
import sys
import tempfile
import time
from dataclasses import asdict
from http.server import HTTPServer
from pathlib import Path
from typing import Callable, overload, List, Dict, Tuple

import coloredlogs
import qrcode
import qrcode_terminal
import requests

from aligo.core.Config import *
from aligo.types import *
from aligo.types.Enum import *
from .EMail import send_email
from .LoginServer import LoginServer

aligo_config_folder = Path.home().joinpath('.aligo')
aligo_config_folder.mkdir(parents=True, exist_ok=True)


def get_configurations() -> List[str]:
    """获取配置文件列表"""
    list_: List[str] = []
    file_: os.DirEntry
    for file_ in os.scandir(aligo_config_folder):
        list_.append(os.path.splitext(file_.name)[0])
    return list_


class Auth:
    """..."""

    _SLEEP_TIME_SEC = None
    _SHARE_PWD_DICT = {}

    def debug_log(self, response: requests.Response):
        """打印错误日志, 便于分析调试"""
        r = response.request
        self.log.warning(f'[method status_code] {r.method} {response.status_code}')
        self.log.warning(f'[url] {response.url}')
        self.log.warning(f'[headers] {r.headers}')
        self.log.warning(f'[request body] {r.body}')
        self.log.warning(f'[response body] {response.text[:200]}')

    def error_log_exit(self, response: requests.Response):
        """打印错误日志并退出"""
        self.debug_log(response)
        exit(-1)

    @overload
    def __init__(
            self,
            name: str = 'aligo',
            show: Callable[[str], None] = None,
            level=logging.DEBUG,
            proxies: Dict = None,
            port: int = None,
            email: Tuple[str, str] = None,
    ):
        """扫描二维码登录"""

    @overload
    def __init__(
            self,
            name: str = 'aligo',
            refresh_token: str = None,
            level=logging.DEBUG,
            proxies: Dict = None,
            port: int = None,
            email: Tuple[str, str] = None,
    ):
        """refresh_token 登录"""

    def __init__(
            self, name: str = 'aligo',
            refresh_token: str = None,
            show: Callable[[str], None] = None,
            level: int = logging.DEBUG,
            proxies: Dict = None,
            port: int = None,
            email: Tuple[str, str] = None,
    ):
        """登录验证

        :param name: (可选, 默认: aligo) 配置文件名称, 便于使用不同配置文件进行身份验证
        :param refresh_token:
        :param show: (可选) 显示二维码的函数
        :param level: (可选) 控制控制台输出
        :param proxies: (可选) 自定义代理 [proxies={"https":"localhost:10809"}],支持 http 和 socks5（具体参考requests库的用法）
        :param port: (可选) 开启 http server 端口，用于网页端扫码登录. 提供此值时，将不再弹出或打印二维码
        :param email: (可选) 发送扫码登录邮件 ("接收邮件的邮箱地址", "防伪字符串"). 提供此值时，将不再弹出或打印二维码
            关于防伪字符串: 为了方便大家使用, aligo 自带公开邮箱, 省去邮箱配置的麻烦.
                        所以收到登录邮件后, 一定要对比确认防伪字符串和你设置一致才可扫码登录, 否则将导致: 包括但不限于云盘文件泄露.
        """
        self._name_name = name
        self._name = aligo_config_folder.joinpath(f'{name}.json')
        self._port = port
        self._webServer: HTTPServer = None  # type: ignore
        self._email = email
        self.log = logging.getLogger(f'{__name__}:{name}')

        fmt = f'%(asctime)s.%(msecs)03d {name}.%(levelname)s %(message)s'

        coloredlogs.install(
            level=level,
            logger=self.log,
            milliseconds=True,
            datefmt='%X',
            fmt=fmt
        )

        self.log.info(f'Config {self._name}')
        self.log.info(f'日志等级 {logging.getLevelName(level)}')

        #
        self.session = requests.session()
        self.session.trust_env = False
        self.session.proxies = proxies
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
                show = self._show_qrcode_in_window
            elif sys.platform.startswith('darwin'):
                self.log.debug('MacOS 操作系统')
                show = self._show_qrcode_in_window
            else:
                self.log.debug('类 Unix 操作系统')
                show = self._show_console
        self._show = show

        if refresh_token:
            self.log.debug('登录方式 refresh_token')
            self._refresh_token(refresh_token)
            return

        if self._name.exists():
            self.log.info(f'加载配置文件 {self._name}')
            self.token = Token(**json.load(self._name.open()))
        else:
            self.log.info('登录方式 扫描二维码')
            self._login()

        #
        self.session.headers.update({
            'Authorization': self.token.access_token
        })

    def _save(self):
        """保存配置文件"""
        self.log.info(f'保存配置文件 {self._name}')
        json.dump(asdict(self.token), self._name.open('w'))

    def _login(self):
        """登录"""
        self.log.info('开始登录')
        response = self._login_by_qrcode()

        if response.status_code != 200:
            self.log.error('登录失败')
            self.error_log_exit(response)

        bizExt = response.json()['content']['data']['bizExt']
        bizExt = base64.b64decode(bizExt).decode('gb18030')

        # 获取解析出来的 refreshToken, 使用这个token获取下载链接是直链, 不需要带 referer header
        refresh_token = json.loads(bizExt)['pds_login_result']['refreshToken']
        self._refresh_token(refresh_token, True)

    def _login_by_qrcode(self) -> requests.Response:
        """二维码登录"""
        response = self.session.get(
            PASSPORT_HOST + NEWLOGIN_QRCODE_GENERATE_DO, params=UNI_PARAMS
        )
        self._log_response(response)
        data = response.json()['content']['data']

        qr_link = data['codeContent']

        # 开启服务
        if self._port or self._email:
            if self._port:
                # noinspection HttpUrlsUsage
                self.log.info(f'请访问 http://<YOUR_IP>:{self._port} 扫描二维码')
                _thread.start_new_thread(self._show_qrcode_in_web, (qr_link,))
            if self._email:
                self._send_email(qr_link)
        else:
            qrcode_png = self._show(qr_link)
            if qrcode_png:
                self.log.info(f'二维码图片文件 {qrcode_png}')
        self.log.info('等待扫描二维码')

        while True:
            response = self.session.post(
                PASSPORT_HOST + NEWLOGIN_QRCODE_QUERY_DO,
                data=data, params=UNI_PARAMS
            )
            self._log_response(response)
            login_data = response.json()['content']['data']
            qrCodeStatus = login_data['qrCodeStatus']
            if qrCodeStatus == 'NEW':
                pass
            elif qrCodeStatus == 'SCANED':
                self.log.info('已扫描 等待确认')
            elif qrCodeStatus == 'CONFIRMED':
                self.log.info(f'已确认 可关闭二维码窗口')
                if self._port:
                    try:
                        self.session.get(f'http://localhost:{self._port}/close')
                    except requests.exceptions.ConnectionError:
                        pass
                return response
            else:
                self.log.warning('未知错误 可能二维码已经过期')
                self.error_log_exit(response)
            time.sleep(3)

    def _refresh_token(self, refresh_token=None, loop_call: bool = False):
        """刷新 token"""
        if refresh_token is None:
            refresh_token = self.token.refresh_token
        self.log.info('刷新 token')
        response = self.session.post(
            API_HOST + V2_ACCOUNT_TOKEN,
            json={
                'refresh_token': refresh_token,
                'grant_type': 'refresh_token'
            }
        )
        self._log_response(response)
        if response.status_code == 200:
            self.log.info('刷新 token 成功')
            self.token = Token(**response.json())
            self._save()
        else:
            self.log.warning('刷新 token 失败')
            if loop_call:
                # 从 _login 调用，则不继续调用 _login，防止循环调用
                # 走到这里 说明 登录失败，则 退出
                self.error_log_exit(response)
            else:
                self.debug_log(response)
                self._login()

        self.session.headers.update({
            'Authorization': self.token.access_token
        })

    _VERIFY_SSL = True

    def request(self, method: str, url: str, params: Dict = None,
                headers: Dict = None, data=None, body: Dict = None) -> requests.Response:
        """统一请求方法"""
        # 删除值为None的键
        if body is not None:
            body = {k: v for k, v in body.items() if v is not None}

        if data is not None and isinstance(data, dict):
            data = {k: v for k, v in data.items() if v is not None}

        response = None
        for i in range(1, 6):
            response = self.session.request(
                method=method, url=url, params=params, data=data,
                headers=headers, verify=self._VERIFY_SSL, json=body
            )
            status_code = response.status_code
            self._log_response(response)

            if status_code == 401:
                if 'ShareLinkToken' not in response.text:
                    self._refresh_token()
                else:
                    # 刷新 share_token
                    share_id = body['share_id']
                    share_pwd = self._SHARE_PWD_DICT[share_id]
                    r = self.post(
                        V2_SHARE_LINK_GET_SHARE_TOKEN,
                        body={
                            'share_id': share_id,
                            'share_pwd': share_pwd
                        }
                    )
                    share_token = r.json()['share_token']
                    headers['x-share-token'].share_token = share_token
                continue

            if status_code == 429 or status_code == 500:
                if self._SLEEP_TIME_SEC is None:
                    sleep_int = 5 ** (i % 4)
                else:
                    sleep_int = self._SLEEP_TIME_SEC
                self.log.warning(f'被限制了 暂停 {sleep_int} 秒')
                time.sleep(sleep_int)
                continue

            return response

        self.log.info(f'重试 5 次仍旧失败')
        self.error_log_exit(response)

    def get(self, path: str, host: str = API_HOST, params: dict = None, headers: dict = None) -> requests.Response:
        """..."""
        return self.request(method='GET', url=host + path, params=params, headers=headers)

    def post(self, path: str, host: str = API_HOST, params: dict = None, headers: dict = None,
             data: dict = None, body: dict = None, ignore_auth: bool = False) -> requests.Response:
        """..."""
        if ignore_auth:
            if headers is None:
                headers = {}
            headers['Authorization'] = None
        return self.request(method='POST', url=host + path, params=params,
                            data=data, headers=headers, body=body)

    @staticmethod
    def _show_console(qr_link: str) -> str:
        """
        在控制台上显示二维码
        :param qr_link: 二维码链接
        :return: NoReturn
        """
        qr_img = qrcode.make(qr_link)

        # try open image
        # 1.
        qr_img.show()

        # show qrcode on console
        # 2.
        qrcode_terminal.draw(qr_link)

        # save image to file
        # 3.
        qrcode_png = tempfile.mktemp('.png')
        qr_img.save(qrcode_png)
        return qrcode_png

    @staticmethod
    def _show_qrcode_in_window(qr_link: str):
        """
        通过 *.png 的关联应用程序显示 qrcode
        :param qr_link: 二维码链接
        :return: NoReturn
        """
        # show qrcode in windows & macos
        qr_img = qrcode.make(qr_link)
        qr_img.show()

    def _show_qrcode_in_web(self, qr_link: str):
        """浏览器显示二维码"""
        qr_img = qrcode.make(qr_link)
        qr_img.get_image()
        qr_img_path = tempfile.mktemp()
        qr_img.save(qr_img_path)
        self._webServer = HTTPServer(('0.0.0.0', self._port), LoginServer)
        self._webServer.qrData = open(qr_img_path, 'rb').read()
        os.remove(qr_img_path)
        try:
            self._webServer.serve_forever()
        except OSError:
            pass

    def _send_email(self, qr_link: str):
        """发送邮件"""
        qr_img = qrcode.make(qr_link)
        qr_img.get_image()
        qr_img_path = tempfile.mktemp()
        qr_img.save(qr_img_path)
        qr_data = open(qr_img_path, 'rb').read()
        send_email(self._email[0], self._name_name, self._email[1], qr_data)
        os.remove(qr_img_path)
        self.log.info(f'登录二维码已发送至 {self._email[0]}')

    def _log_response(self, response: requests.Response):
        """打印响应日志"""
        self.log.info(
            f'{response.request.method} {response.url} {response.status_code} {len(response.content)}'
        )

    def logout(self):
        """退出"""
        self._name.unlink()
