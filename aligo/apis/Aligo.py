"""Aligo class"""
import logging
from typing import Callable, Dict

from typing_extensions import NoReturn

from .Audio import Audio
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
            loglog: bool = False,
            use_aria2: bool = False,
            proxies: Dict = None
    ):
        """
        Aligo
        :param name: (可选, 默认: aligo) 配置文件名称, 便于使用不同配置文件进行身份验证
        :param refresh_token:
        :param show: (可选) 显示二维码的函数
        :param level: (可选) 控制控制台输出
        :param loglog: (可选) 控制文件输出
        :param use_aria2: [bool] 是否使用 aria2 下载
        :param proxies: (可选) 自定义代理 [proxies={"https":"localhost:10809"}],支持 http 和 socks5（具体参考requests库的用法）
        """
        super().__init__(name, refresh_token, show, level, loglog, use_aria2, proxies)
