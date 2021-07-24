"""..."""

import base64
import json
import logging
import os
import random
import re
import sys
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
    """..."""

    @staticmethod
    def get_configurations() -> List[str]:
        """..."""
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
        ...

    @overload
    def __init__(
            self,
            name: str = 'aligo',
            phone_num: str = None,
            # show: Callable[[str], NoReturn] = None,
            level=logging.DEBUG,
            loglog: bool = False
    ):
        ...

    @overload
    def __init__(
            self,
            name: str = 'aligo',
            username: str = None,
            password: str = None,
            # show: Callable[[str], NoReturn] = None,
            level=logging.DEBUG,
            loglog: bool = False
    ):
        ...

    @overload
    def __init__(
            self,
            name: str = 'aligo',
            username: str = None,
            password2: str = None,
            # show: Callable[[str], NoReturn] = None,
            level=logging.DEBUG,
            loglog: bool = False
    ):
        ...

    @overload
    def __init__(
            self,
            name: str = 'aligo',
            refresh_token: str = None,
            # show: Callable[[str], NoReturn] = None,
            level=logging.DEBUG,
            loglog: bool = False
    ):
        ...

    def __init__(
            self, name: str = 'aligo',
            username: str = None,
            password: str = None,
            password2: str = None,
            phone_num: str = None,
            refresh_token: str = None,
            show: Callable[[str], NoReturn] = None,
            level=logging.DEBUG,
            loglog: bool = False
    ):
        """
        login & auth
        :param name: (Optional) default: "aligo", configuration file name
        :param username: (Optional) your aliyundrive account username
        :param password: (Optional) your ... password
        :param password2: (Optional) captured password2
        :param phone_num: (Optional) your phone number
        :param refresh_token: (Optional) refresh_token
        :param show: (Optional) default: show_windows,show qrcode function
        :param level: (Optional) default: logging.INFO, level of log
        :param loglog: (Optional) default: False, records log file
        """

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
        }, stream=True).close()

        #
        SESSIONID = self.session.cookies.get('SESSIONID')
        logging.debug(f'SESSIONID {SESSIONID}')

        #
        self.token: Optional[Token] = None
        self._username = username
        self._password = password
        self._password2 = password2
        self._phone_num = phone_num
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

        self._login_by_id_file()

        #
        self.session.headers.update({
            'Authorization': f'Bearer {self.token.access_token}'
        })

    def _save(self) -> NoReturn:
        """..."""
        logging.info(f'Save configuration file: {self._name}')
        ujson.dump(self.token.__dict__, self._name.open('w'))

    def _login_by_id_file(self):
        """..."""
        if self._name.exists():
            logging.info(f'Found configuration file: {self._name}')
            logging.info(f'Loading configuration: {self._name}')
            self.token = Token(**ujson.load(self._name.open()))
        else:
            logging.info(f'Not found configuration file: {self._name}')
            self._login_()

    def _login_(self):
        """..."""
        logging.info('Start login ...')
        if self._password2:
            response = self._login_by_password2(self._username, self._password2)
        elif self._password:
            response = self._login_by_password(self._username, self._password)
        elif self._phone_num:
            response = self._login_by_sms(self._phone_num)
        else:
            response = self._login_by_qrcode()

        if response.status_code != 200:
            logging.error('Login failed ')
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
        logging.info('Login success')
        logging.info(f'username: {self.token.user_name} nickname: {self.token.nick_name} user_id: {self.token.user_id}')

        # 保存
        self._save()

    def _login_by_sms(self, phone_num: str) -> requests.Response:
        """..."""
        rnd = random.random()
        response = self.session.get('https://passport.aliyundrive.com/mini_login.htm', params={
            'lang': 'zh_cn',
            'appName': 'aliyun_drive',
            'appEntrance': 'web',
            'styleType': 'auto',
            'bizParams': '',
            'notLoadSsoView': 'false',
            'notKeepLogin': 'false',
            'isMobile': 'false',
            'hidePhoneCode': 'true',
            'rnd': rnd,
        })
        body = {
            'phoneCode': '86',
            'loginId': '15549727151',
            'countryCode': 'CN',
            'ua': '140#JvbDE6FAzzFHazo22i+uCtSd093GP+FprAVAok37dKiBQXLehCRx5Z23qt+BmhCFJXdQ1CZEKviXhupw2Y+DcIzK+6hqzzngxMFOrZzzzFb2VY/BUbzx2DD3VthqzF+jtM3ylpOdzPzYVXE/lbcwFIdkdzwpOSvZrI7ZbiomCSbsYSTnxCgj0VbyfaNsSCajRUQOHkQpakLuUH9d8M1G5kpEg9kMwqcMDqmK91P9z5BE6VAyeeMsNyCM4tDXRNYDdTr0cmtggva45fi4UlX5zbiGRHAUi7pDk/vFA770xXx2sWRzHyNMf53k40HjmkRSn4kQzhT5TUSii8F8yPl+dPvZtBBUV7wq/fX8g9ryd2MQAA3VkkMTTkxjb/5fOBjQRhQEL05XrDO9/0dOQz4JOgZobM0zmukCWTReb468ez14T+tw8N1VxicqSj5WAE83gCWoeWzfo9cucm0ZS10a4jD4rRMp3HwQeQJWmTuUNcGYjNWRnltWfOHXONnllgIW1YiV6/oqhhpnIk2NNst2EIIG5exCho1LSS9X7G0+xguXD3mEPTSiyIJJ48Gk5pcTRR0BO1z5ECN55t2HQWRhXWwEWv0prMKLKPVWQ5jNLg1asDnVYzYFrWCOf62FY0AvEnCPc+V+BTiZORpBKxsmAtxFC0B50eg52rp/zP4qshp9PF/MOxUcmePaeOOjgYPT+tNZ6VEiFSnIycuoeVg6eBEI5XEtmqZKYDsfYnhR688r+dRsCjsxQsiam9g7gnZAkW/hwAd/fFHo+VFv/mqu6XFwnF0XdiADKGdrWnxeFkrNjbshpPhVl8U/z7HeG7dK2y/ZVlHcz3pWQVpd/COSaoNy/g76CNZ0FcSOAxcRwujjcMCtNOCFMYI07ZXN8iGeJrqBa5wCD6b7134Mk7gqW4swV9gxuMD0lGJFzh/v6zjJe2oRuAv2cVvlvZSrELmDFtPzLguK1lvee2aAHRDRNkI5QzQVI8Dt+ZaVGphv32T9EtrlD9+2nh9feF2RUbn1kGCIvPMvDWmvL8f9hxDuRz0xI9X+pESykJjekT5JWMHB0D8ddXRgbThRnq/n2egKIIvXjS5jJrjX+pR0d9jOtH5nAWqjbG0dj2gTgo+tzMi6POR6Lfq705DoB7fqZPjBItvjPZSw9BOVKNWppefjyHeG9PC4arUNo2JfP/MUP2ErjNr6ZadA/BNmfLvlJEWKOYZKS7k/',
            'bx-ua': '213!HzUiTuhRSJjlHlJz2j9QH1Iw32zXh05U54ROagQ2Sh/k3Df0aRfuJbJwvAYWHEThL0N1tFMTF2IVaM5w3rvTqAAZAEYwrK1/uf Vup5c2hf/vgClF9fuOo8KhnMNGDSnesR8sVy6msQUTGe/0Yuk/6d9yrwRTMD8xV8 4I8TJwyttKfFn9nlOaZOZazVHq0EukAOwkf1sstHIJpt7UM0NnzdAOh2wgvUfHFKXIDOckvoZ/ZJq58fN5VY1GkcJCJzmBnQ7Q3U3ihJXfCNoYbjm83jnIcGPefX7QwvLFN2p4RxcXjt JpJQ5pPuBe4fYXdz1aOB6rju4A1ow pNZHdYO2XiMSdkuiULcCPacVO4mzGyoLIMo3tGJ9Jar1t500hK7uJXn/r3uSCYy5Y8/ASFg7Rr72DGxzN88GJcJ7iBllds4Hyh6uGzzaD2VMswV70yRCw4cE9Mb09M vEZ4Tgu/Cqe46Zxbv9bVnl4ZLFh1xxkcK4cJotBLvRuyFNLR4A45ia9L6B8YRBJaX1j CHY5rLBcgRYXVJO4W/WDzqbyN8gAVc IgvrlWXS/Yozqa7RwIuPXZEt0fBG6kuZgZ6Wv 6m HxRhxuwG4J10p8 dTHMljkgdW98Wp4frB986IocfLX20fRYknuLuaAD73Er65TUPoqxmS2AL0H51D70Da7LCWPSnqv4pZ PPzBtnfW iEhpb RWUYNQhNnpCJ65YSpODZurzlSbzIcDO1km1jUdDOwz645TWAh qY3eBGyg0q9KasWYJ8 lED08Q8j4YKWQZW8cJcuYJn36bx/zpmDWU/PInlHZjfmuftMxyht5lypWb1UQHEF9wrTR5pds1  uMb7xyeG5mdNdzCDUDjCa/9B1dUOsTrG6gD9SGcGSTmP//O5GRGrtEE4xhFTI67E1/jYl2UHfoS0EXqjKdJcl7n3/rPIWjK6rIddqewLbjlb/U1 tOLIRmJLNHYn3I/rDRNhvY4r7CyxvV4gu5CjJK1MStprv8aAko ex898sQTyErcQojhPBZRT8uHYnn5cDnd6xV/6m/iBA2PSgrZGBov8i8jBh14fkGGeDbGcz8m/OCGsCi RpbW7ihtffe10Sezkf11tR44 rfuH17GRseh9CqlX29yOq0uPy0OOHBaKqNTkHuTxIqTV4hg 0VWvuE LDl9QUqq6T1e8bXvRcQYWZnTjDjRING6dmEF87nTP jN3lZy1JyIX18dRNDoW48rsUBkM6/v2NWKROzkalmPpTr GjLloNtxIuEQMP9oYs7gT3jpvJa1FnZhmCZjK2K/PBd/OqqBxUNt0pUnetigKNYD5FdGFShWIpevbHzEUxx6lLSSpvpsGKoE0gNQIQUeOIHlBtIrdH7ph/i4uZcCnW0sSGV6C8Wja8Hpr3R/iHjM3IuUyl6ddALo2lqiy8P4juheUPYQU5EG17EtAsfX/TDEBIdsrIDNPsjD5uw61dhF ORCH1tgZmFUcV t1hE79wXp2M/I5m/t3I QP5G911n/65KsAHgIT07AX1TtJmsJYXac23Z3qRQjD6fSbqDgK 2VyCF4p3EGJ/n5vva ZyX2yCvNk9dF8T9g0h3vhdEz1V yVtWuoN/aFCYn38EPnX7pqhwpKmGkDXLAmzdFzhUVI/rC/dtGPL7dRat3N8bBijkXQhYPHhfVjmtukMA/I3Cm6bYaJj6SugZEJfGqDIxwl1EpEgsh6aw7V1si0lkfmxfYi3 BmtpSzC89YVNheqoO pv2QBvfR5yZiKtzFyXcnjpbCreA5S5QVJtfUf8SKOsb/PMZnkjtFiuZj 3iyfRbAtVnlVLh=',
            'navUserAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
        }

        rt = re.findall('"loginFormData":({[^}]+})', response.text)
        body.update(json.loads(rt[0]))

        while True:
            response = self.session.post(
                PASSPORT_HOST + NEWLOGIN_SMS_SEND_DO,
                params={
                    'appName': 'aliyun_drive',
                    'fromSite': 52,
                    '_bx-v': '2.0.47',
                }, data=body
            )
            rtData = response.json()['content']['data']
            if 'smsToken' in rtData:
                logging.info(f'Send SMS code success: {phone_num} ')
                break
            else:
                logging.info(f'{rtData["titleMsg"]}')
                time.sleep(30)
                logging.info(f'Sleep 30s ...')

        smsToken = rtData['smsToken']
        #
        sys.stdout.flush()
        smsCode = input('Please type SMS code: ').strip()

        body.update({
            **body,
            'smsCode': smsCode,
            'smsToken': smsToken
        })
        response = self.session.post(
            PASSPORT_HOST + NEWLOGIN_SMS_LOGIN_DO,
            data=body
        )
        return response

    def _login_by_qrcode(self) -> requests.Response:
        """..."""
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
                logging.info('Waiting scan qrcode ...')
            elif qrCodeStatus == 'SCANED':
                logging.info('Scanned, waiting for confirmation ...')
            elif qrCodeStatus == 'CONFIRMED':
                logging.info(f'Scan success (you can close the qrcode image.)')
                return response
            else:
                logging.warning('Unknow error: maybe qrcode already expired')
                self._error_log_exit(response)
            time.sleep(2)

    def _login_by_password(self, username: str, password: str) -> requests.Response:
        """..."""
        self._password2 = self._rsa_password(password)
        return self._login_by_password2(username, self._password2)

    def _login_by_password2(self, username: str, password2: str) -> requests.Response:
        """..."""
        response = self.session.post(
            PASSPORT_HOST + NEWLOGIN_LOGIN_DO,
            data={
                'loginId': username,
                'password2': password2
            }
        )
        return response

    def _refesh_token(self, refresh_token=None):
        if refresh_token is None:
            refresh_token = self.token.refresh_token
        logging.info('Refresh token ...')
        response = self.session.post(
            WEBSV_HOST + TOKEN_REFRESH,
            json={'refresh_token': refresh_token}
        )
        if response.status_code == 200:
            logging.info('Refresh token success')
            self.token = Token(**response.json())
            self.session.headers.update({
                'Authorization': f'Bearer {self.token.access_token}'
            })
            self._save()
        else:
            logging.error('Refresh token failed')
            self._debug_log(response)
            self._login_()
            # error_log_exit(response)

    def request(self, method: str, url: str,
                params: Dict = None, headers: Dict = None, data=None,
                files: object = None, verify: bool = None, body: Dict = None) -> requests.Response:
        """..."""
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
