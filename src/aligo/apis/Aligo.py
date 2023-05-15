"""Aligo class"""
import json
import logging
from typing import Callable, Dict

from .Album import Album
from .Audio import Audio
from .Compress import Compress
from .Copy import Copy
from .Copy import aligo_config_folder
from .Create import Create
from .CustomShare import CustomShare
from .Download import Download
from .Drive import Drive
from .Duplicate import Duplicate
from .File import File
from .Move import Move
from .Other import Other
from .Recyclebin import Recyclebin
from .Search import Search
from .Share import Share
from .Star import Star
from .SyncFolder import SyncFolder
from .Update import Update
from .Video import Video
from aligo.types import EMailConfig


class Aligo(
    Audio,
    Album,
    Compress,
    Copy,
    Create,
    CustomShare,
    Download,
    Drive,
    Duplicate,
    File,
    Move,
    Other,
    Recyclebin,
    Search,
    Share,
    Star,
    SyncFolder,
    Update,
    Video,
):
    """阿里云盘"""

    def __init__(
            self,
            name: str = 'aligo', *,
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
        Aligo
        :param name: (可选, 默认: aligo) 配置文件名称, 便于使用不同配置文件进行身份验证
        :param refresh_token:
        :param show: (可选) 显示二维码的函数
        :param level: (可选) 控制控制台输出
        :param use_aria2: [bool] 是否使用 aria2 下载
        :param proxies: (可选) 自定义代理 [proxies={"https":"localhost:10809"}],支持 http 和 socks5（具体参考requests库的用法）
        :param port: (可选) 开启 http server 端口，用于网页端扫码登录. 提供此值时，将不再弹出或打印二维码
        :param email: (可选) 邮箱配置，参考 EMailConfig
        :param request_failed_delay: (可选) 由于网络异常导致的 request 异常，等待多少秒后重试
        :param requests_timeout: (可选) 应网友提议，添加 requests timeout 参数
        :param login_timeout: (可选) 登录超时时间，单位：秒。
        :param re_login: refresh_token 失效后是否继续登录（弹出二维码或邮件，需等待） fix #73

        level, use_aria2, proxies, port, email 可以通过 配置文件 配置默认值，在 <用户家目录>/.aligo/config.json5 中
        ```json5
        {
          "level": 10,
          "use_aria2": false,
          "proxies": {
            "https": "http://localhost:10809",
            // "https": "socks5://localhost:10808", # 不支持注释，写的时候删掉
          },
          "port": 8080,
          "email": ["邮箱地址", "防伪字符串"]
        }
        ```
        """
        config = aligo_config_folder / 'config.json5'
        if config.exists():
            config = json.loads(config.read_text(encoding='utf8'))
            if level == logging.DEBUG and 'level' in config:
                level = config.get('level')
            if not use_aria2:
                use_aria2 = config.get('use_aria2')
            if proxies is None:
                proxies = config.get('proxies')
            if port is None:
                port = config.get('port')
            if email is None:
                email = config.get('email')
            if request_failed_delay == 3:
                requests_timeout = config.get('request_failed_delay', 3)
            if requests_timeout is None:
                requests_timeout = config.get('requests_timeout')
            if requests_timeout is None:
                login_timeout = config.get('login_timeout')
            if re_login is True:
                re_login = config.get('re_login')

        super().__init__(
            name,
            refresh_token,
            show,
            level,
            use_aria2,
            proxies,
            port,
            email,
            request_failed_delay,
            requests_timeout,
            login_timeout,
            re_login,
        )
