"""认证模块"""

import base64
import logging
import os
import time
from pathlib import Path
from typing import Callable, overload, List, NoReturn, Dict
from urllib import parse

import coloredlogs
import jsonpickle
import requests
import ujson

from aligo.auth import *
from aligo.config import *
from aligo.types import *

_aligo = Path.home().joinpath('.aligo')
_aligo.mkdir(parents=True, exist_ok=True)


class Auth(BaseClass):
    """认证对象

    login & auth
    :param name: (可选) 默认: "aligo", 保存到的配置文件名称(ID)
    :param refresh_token: (可选) refresh_token
    :param show: (可选) 默认: 用于显示二维码, 参数是一个链接字符串, Windows上默认 BaseClass._show_windows, Linux上默认 BaseClass._show_console(Linux)
    :param level: (可选) 默认: logging.DEBUG, 日志等级
    :param loglog: (可选) 默认: False, 记录日志文件文件
    """

    @staticmethod
    def get_configurations() -> List[str]:
        """获取配置文件列表"""
        list_: List[str] = []
        file_: os.DirEntry
        for file_ in os.scandir(_aligo):
            list_.append(os.path.splitext(file_.name)[0])
        return list_

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
            level=logging.DEBUG,
            loglog: bool = False
    ):
        self._name = _aligo.joinpath(f'{name}.json')

        coloredlogs.install(
            level=level,
            milliseconds=True,
            datefmt='%X',
            fmt='%(asctime)s.%(msecs)03d %(levelname)5s %(message)s'
        )

        if loglog:
            logfile = logging.FileHandler(filename=str(self._name)[:-5] + '.log', mode='w', encoding='utf-8')
            logfile.setLevel(logging.DEBUG)
            formatter = logging.Formatter('%(asctime)s  %(filename)s  %(funcName)s : %(levelname)s  %(message)s',
                                          datefmt='%F %X')
            logfile.setFormatter(formatter)
            logging.getLogger().addHandler(logfile)

        logging.debug(f'name {self._name}')

        #
        self.session = requests.session()
        self.session.params.update(UNI_PARAMS)
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
        logging.debug(f'SESSIONID {SESSIONID}')

        #
        self.token: Optional[Token] = None
        if show is None:
            if os.name == 'nt':
                show = self._show_windows
            else:
                show = self._show_console
        self._show = show

        # refresh_token 登录
        if refresh_token:
            self._refesh_token(refresh_token)
            return

        if self._name.exists():
            logging.info(f'发现配置文件: {self._name}')
            # logging.info(f'Loading configuration: {self._name}')
            self.token = Token(**ujson.load(self._name.open()))
        else:
            logging.info(f'未发现配置文件: {self._name}')
            self._login_()

        #
        self.session.headers.update({
            'Authorization': f'Bearer {self.token.access_token}'
        })

    def _save(self) -> NoReturn:
        """保存配置文件"""
        logging.info(f'保存配置文件: {self._name}')
        ujson.dump(self.token.__dict__, self._name.open('w'))

    def _login_(self):
        """登录"""
        logging.info('开始登录 ...')
        response = self._login_by_qrcode()

        if response.status_code != 200:
            logging.error('登录失败 ~')
            self._error_log_exit(response)

        bizExt = response.json()['content']['data']['bizExt']
        bizExt = base64.b64decode(bizExt).decode('gb18030')
        accessToken = ujson.loads(bizExt)['pds_login_result']['accessToken']

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

        self.token = Token(**response.json())

        #
        logging.info('登录成功 ~')
        logging.info(f'username: {self.token.user_name} nickname: {self.token.nick_name} user_id: {self.token.user_id}')

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
                logging.info('等待扫描二维码 ...')
            elif qrCodeStatus == 'SCANED':
                logging.info('已扫描, 等待确认 ...')
            elif qrCodeStatus == 'CONFIRMED':
                logging.info(f'已确认 (你可以关闭二维码图像了.)')
                return response
            else:
                logging.warning('未知错误: 可能二维码已经过期.')
                self._error_log_exit(response)
            time.sleep(2)

    def _refesh_token(self, refresh_token=None):
        """刷新 token"""
        if refresh_token is None:
            refresh_token = self.token.refresh_token
        logging.info('刷新 token ...')
        response = self.session.post(
            WEBSV_HOST + TOKEN_REFRESH,
            json={'refresh_token': refresh_token}
        )
        if response.status_code == 200:
            logging.info('刷新 token 成功')
            self.token = Token(**response.json())
            self.session.headers.update({
                'Authorization': f'Bearer {self.token.access_token}'
            })
            self._save()
        else:
            logging.error('刷新 token 失败 ~')
            self._debug_log(response)
            self._login_()
            # error_log_exit(response)

    def request(self, method: str, url: str,
                params: Dict = None, headers: Dict = None, data=None,
                files: object = None, verify: bool = None, body: Dict = None) -> requests.Response:
        """统一请求方法"""
        # 添加头参数
        # if params is None:
        #     params = {}
        # params.update({**UNI_PARAMS})
        # if headers is None:
        #     headers = {}
        # headers.update({**UNI_HEADERS})
        # 移至session.headers中

        # 删除值为None的键
        if body is not None:
            body = {k: v for k, v in body.items() if v is not None}

        if data is not None and isinstance(data, dict):
            data = {k: v for k, v in data.items() if v is not None}

        # if 'part_info_list' in body:
        #     body['part_info_list'] = [i.__dict__ for i in body['part_info_list']]

        while True:
            # 移至session.headers中
            # headers['Authorization'] = f'Bearer {self.token.access_token}'
            response = self.session.request(method=method, url=url, params=params,
                                            data=data, headers=headers, files=files,
                                            verify=verify,
                                            json=jsonpickle.loads(jsonpickle.dumps(body, unpicklable=False)))
            status_code = response.status_code
            if status_code == 401:
                self._refesh_token()
                continue

            return response

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
