"""分享链接下载链接请求体"""
from dataclasses import dataclass

from aligo.types import *


@dataclass
class GetShareLinkDownloadUrlRequest(DataClass):
    """..."""
    share_id: str
    file_id: str
    # {"code":"InvalidParameter.ExpireSec","message":"The input parameter expire_sec is not valid. expire_sec should be less or equal than 600"}
    # expire_sec: int = 14400
    expire_sec: int = 600
    image_thumbnail_process: str = None
    image_url_process: str = None
    video_thumbnail_process: str = None
    get_video_play_info: bool = None
    get_audio_play_info: bool = None
