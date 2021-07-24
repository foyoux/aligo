"""aligo"""
from .auth import *
from .config import *
from .core import *
from .request import *
from .response import *
from .types import *

__title__ = 'aligo'
__description__ = 'apis lib for aliyundrive.'
__url__ = 'https://aligo.readthedocs.io'
__version__ = '1.0.0'
__author__ = 'foyou'
__author_email__ = 'yimi.0822@qq.com'
__license__ = 'Apache 2.0'
__copyright__ = f'Copyright 2021 {__author__}'
__ide__ = 'PyCharm - https://www.jetbrains.com/pycharm/'


class AligoCore(
    AudioInfo,
    CopyFile,
    CreateFile,
    DriveInfo,
    FileList,
    LatestClient,
    MoveFile,
    Other,
    PersonalInfo,
    Recyclebin,
    Search,
    Share,
    Update,
    User,
    VideoInfo
):
    """..."""
    pass
