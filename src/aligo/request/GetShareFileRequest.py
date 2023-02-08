"""..."""
from dataclasses import dataclass

from aligo.types import *
from aligo.types.Enum import *


@dataclass
class GetShareFileRequest(DataClass):
    """..."""
    share_id: str = None
    fields: GetFileFields = '*'
    file_id: str = None
    image_thumbnail_process: str = 'image/resize,w_1920/format,jpeg'
    image_url_process: str = 'image/resize,w_375/format,jpeg'
    url_expire_sec: int = 14400
    video_thumbnail_process: str = 'video/snapshot,t_1000,f_jpg,ar_auto,w_375'
