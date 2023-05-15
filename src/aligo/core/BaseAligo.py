"""..."""
import json
import logging
import subprocess
import traceback
from dataclasses import asdict, is_dataclass
from typing import Generic, List, Iterator, Dict, Callable, Union, Type

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

    def __init__(
            self,
            name: str = 'aligo',
            refresh_token: str = None,
            show: Callable[[str], None] = None,
            level: int = logging.DEBUG,
            use_aria2: bool = False,
            proxies: Dict = None,
            port: int = None,
            email: EMailConfig = None,
            request_failed_delay: float = 3,
            requests_timeout: float = None,
            login_timeout: float = None,
            re_login: bool = True
    ):
        """
        BaseAligo
        :param name: (可选, 默认: aligo) 配置文件名称, 便于使用不同配置文件进行身份验证
        :param refresh_token:
        :param show: (可选) 显示二维码的函数
        :param level: (可选) 控制控制台输出
        :param use_aria2: [bool] 是否使用 aria2 下载
        :param proxies: (可选) 自定义代理 [proxies={"https":"localhost:10809"}],支持 http 和 socks5（具体参考requests库的用法）
        :param port: (可选) 开启 http server 端口，用于网页端扫码登录. 提供此值时，将不再弹出或打印二维码
        :param email: (可选) 邮箱配置，参考 EMailConfig
        :param request_failed_delay: 请求失败后，延迟时间，单位：秒
        :param requests_timeout: same as requests timeout
        :param login_timeout: 登录超时时间，单位：秒
        :param re_login: refresh_token 失效后是否继续登录（弹出二维码或邮件，需等待） fix #73
        """
        self._auth: Auth = Auth(  # type: ignore
            name=name,
            refresh_token=refresh_token,
            show=show,
            level=level,
            proxies=proxies,
            port=port,
            email=email,
            request_failed_delay=request_failed_delay,
            requests_timeout=requests_timeout,
            login_timeout=login_timeout,
            re_login=re_login,
        )
        # 因为 self._auth.session 没有被重新赋值, 所以可以这么用
        self._session: requests.Session = self._auth.session
        # 在刷新 token 时, self._auth.token 被重新赋值, 而 self._token 却不会被更新
        # self._token: Token = self._auth.token
        self._user: Optional[BaseUser] = None
        self._personal_info: Optional[GetPersonalInfoResponse] = None
        self._default_drive: Optional[BaseDrive] = None

        if use_aria2:
            try:
                subprocess.run(['aria2c', '-h'], capture_output=True)
                self._has_aria2c = True
                self._auth.log.info('发现 aria2c, 将使用 aria2c 下载文件')
            except FileNotFoundError:
                self._auth.log.warning('未发现 aria2c')
                self._has_aria2c = False
        else:
            self._has_aria2c = False

    def _post(
            self,
            path: str,
            host: str = API_HOST,
            body: Union[DataType, Dict] = None,
            headers: dict = None,
            ignore_auth: bool = False,
            params: dict = None,
    ) -> requests.Response:
        """统一处理数据类型和 drive_id"""
        if body is None:
            body = {}
        elif isinstance(body, DataClass):
            body = asdict(body)

        if 'drive_id' in body and body['drive_id'] is None:
            # 如果存在 attr drive_id 并且它是 None，并将 default_drive_id 设置为它
            body['drive_id'] = self.default_drive_id

        return self._auth.post(path=path, host=host, body=body, headers=headers, ignore_auth=ignore_auth, params=params)

    @property
    def default_drive_id(self):
        """默认 drive_id"""
        return self._auth.token.default_drive_id

    @property
    def default_sbox_drive_id(self):
        """默认保险箱 drive_id"""
        return self._auth.token.default_sbox_drive_id

    @property
    def user_name(self):
        """用户名"""
        return self._auth.token.user_name

    @property
    def user_id(self):
        """用户 id"""
        return self._auth.token.user_id

    @property
    def nick_name(self):
        """昵称"""
        return self._auth.token.nick_name

    def _result(self, response: requests.Response,
                cls: Generic[DataType],
                status_code: Union[List, int] = 200, field: str = None) -> Union[Null, DataType]:
        """统一处理响应

        :param response:
        :param cls:
        :param status_code:
        :return:
        """
        if isinstance(status_code, int):
            status_code = [status_code]
        if response.status_code in status_code:
            text = response.text
            if not text.startswith('{'):
                return cls()
            try:
                # noinspection PyProtectedMember
                d = json.loads(text)
                if field:
                    for i in field.split('.'):
                        d = d[i]
                if isinstance(d, list):
                    return [DataClass.fill_attrs(cls, i) for i in d]
                return DataClass.fill_attrs(cls, d)
            except TypeError:
                self._auth.debug_log(response)
                self._auth.log.error(cls)
                traceback.print_exc()
        self._auth.log.warning(f'{response.status_code} {response.text[:200]}')
        return Null(response)

    def _list_file(
            self, path: str, body: Union[DataClass, Dict],
            resp_type: Generic[DataType], headers: dict = None, params: dict = None) -> Iterator[DataType]:
        """
        枚举文件: 用于统一处理 1.文件列表 2.搜索文件列表 3.收藏列表 4.回收站列表
        :param path: [str] 批量处理的路径
        :param body: [DataClass] 批量处理的参数
        :param resp_type: [Callable] 响应类型
        :return: [Iterator[DataType]] 响应结果

        如何判断请求失败与否（适用于所有使用此方法的上层方法）：
        >>> from aligo import Aligo
        >>> ali = Aligo()
        >>> result = ali.get_file_list('<file_id>')
        >>> if isinstance(result[-1], Null):
        >>>     print('请求失败')
        """
        response = self._post(path, body=body, headers=headers, params=params)
        file_list = self._result(response, resp_type)
        if isinstance(file_list, Null):
            yield file_list
            return
        yield from file_list.items
        if file_list.next_marker != '':
            if isinstance(body, dict):
                body['marker'] = file_list.next_marker
            else:
                body.marker = file_list.next_marker
            yield from self._list_file(path=path, body=body, resp_type=resp_type, headers=headers, params=params)

    def _core_get_file(self, body: GetFileRequest) -> BaseFile:
        """获取文件信息, 其他类中可能会用到, 所以放到基类中"""
        response = self._post(V2_FILE_GET, body=body)
        return self._result(response, BaseFile)

    def get_personal_info(self) -> GetPersonalInfoResponse:
        """
        获取个人信息
        :return: [GetPersonalInfoResponse]
        """
        response = self._post(V2_DATABOX_GET_PERSONAL_INFO)
        return self._result(response, GetPersonalInfoResponse)

    _BATCH_COUNT = 100

    @staticmethod
    def _list_split(ll: List[DataType], n: int) -> List[List[DataType]]:
        rt = []
        for i in range(0, len(ll), n):
            rt.append(ll[i:i + n])
        return rt

    def batch_request(self, body: BatchRequest, body_type: Type[DataType]) -> Iterator[BatchSubResponse[DataType]]:
        """
        批量请求：官方最大支持 100 个请求，所以这里按照 100 个一组进行分组，然后分别请求，使用时无需关注这个。
        :param body:[BatchRequest] 批量请求的参数
        :param body_type: [DataType] 批量请求的参数类型
        :return: [Iterator[DataType]]

        如何判断请求失败与否（适用于所有使用此方法的上层方法）：
        >>> from aligo import Aligo
        >>> ali = Aligo()
        >>> result = ali.batch_get_files(['<file1_id>', '<file2_id>'])
        >>> if isinstance(result[-1], Null):
        >>>     print('请求失败')
        """
        for request_list in self._list_split(body.requests, self._BATCH_COUNT):
            response = self._post(V3_BATCH, body={
                "requests": [
                    {
                        "body": asdict(request.body) if is_dataclass(request.body) else request.body,
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
                i = DataClass.fill_attrs(BatchSubResponse, batch)
                if i.body:
                    try:
                        # 不是都会成功
                        # eg: {
                        #       'code': 'AlreadyExist.File',
                        #       'message': "The resource file has already exists. drive has the same file,
                        #                   can't update, file_id 609887cca951bf4feca54c6ebd0a91a03b826949"
                        # }
                        # status 409
                        i.body = DataClass.fill_attrs(body_type, i.body)
                    except TypeError:
                        # self._auth.log.warning(i)
                        pass
                yield i
