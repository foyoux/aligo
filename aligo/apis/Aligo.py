"""Aligo class"""
import json
import logging
from typing import Callable, Dict, Tuple

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


class Aligo(
    Audio,
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
            name: str = 'aligo',
            refresh_token: str = None,
            show: Callable[[str], None] = None,
            level: int = logging.DEBUG,
            use_aria2: bool = False,
            proxies: Dict = None,
            port: int = None,
            email: Tuple[str, str] = None,
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
        :param email: (可选) 发送扫码登录邮件 ("接收邮件的邮箱地址", "防伪字符串"). 提供此值时，将不再弹出或打印二维码
            关于防伪字符串: 为了方便大家使用, aligo 自带公开邮箱, 省去邮箱配置的麻烦.
                        所以收到登录邮件后, 一定要对比确认防伪字符串和你设置一致才可扫码登录, 否则将导致: 包括但不限于云盘文件泄露.
            关于防伪字符串: 为了方便大家使用, aligo 自带公开邮箱, 省去邮箱配置的麻烦.
                        所以收到登录邮件后, 一定要对比确认防伪字符串和你设置一致才可扫码登录, 否则将导致: 包括但不限于云盘文件泄露.
            关于防伪字符串: 为了方便大家使用, aligo 自带公开邮箱, 省去邮箱配置的麻烦.
                        所以收到登录邮件后, 一定要对比确认防伪字符串和你设置一致才可扫码登录, 否则将导致: 包括但不限于云盘文件泄露.

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
            config = json.loads(config.open().read())
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

        super().__init__(
            name,
            refresh_token,
            show,
            level,
            use_aria2,
            proxies,
            port,
            email,
        )
