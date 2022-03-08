"""Aligo class"""
import json
import logging
from typing import Callable, Dict

from typing_extensions import NoReturn

from .Audio import Audio, aligo_config_folder
from .Copy import Copy
from .Create import Create
from .CustomShare import CustomShare
from .Download import Download
from .Drive import Drive
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
    Video,
    Copy,
    Create,
    Drive,
    File,
    Move,
    Download,
    Recyclebin,
    Search,
    Share,
    CustomShare,
    Star,
    Update,
    Other,
    SyncFolder,
):
    """阿里云盘"""

    def __init__(
            self,
            name: str = 'aligo',
            refresh_token: str = None,
            show: Callable[[str], NoReturn] = None,
            level: int = logging.DEBUG,
            use_aria2: bool = False,
            proxies: Dict = None,
            port: int = None
    ):
        """
        Aligo
        :param name: (可选, 默认: aligo) 配置文件名称, 便于使用不同配置文件进行身份验证
        :param refresh_token:
        :param show: (可选) 显示二维码的函数
        :param level: (可选) 控制控制台输出
        :param use_aria2: [bool] 是否使用 aria2 下载
        :param proxies: (可选) 自定义代理 [proxies={"https":"localhost:10809"}],支持 http 和 socks5（具体参考requests库的用法）

        level, use_aria2, proxies 三个参数可以通过 配置文件 配置默认值，在 <用户家目录>/.aligo/config.json5 中
        ```json5
        {
          "level": 10,
          "use_aria2": false,
          "proxies": {
            "https": "http://localhost:10809",
            // "https": "socks5://localhost:10808", # 不支持注释，写的时候删掉
          },
          "port": 8080
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

        super().__init__(name, refresh_token, show, level, use_aria2, proxies, port)
