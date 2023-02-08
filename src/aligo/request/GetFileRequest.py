"""..."""

from dataclasses import dataclass, field

from aligo.types import *
from aligo.types.Enum import *


@dataclass
class GetFileRequest(DataClass):
    """..."""
    file_id: str
    drive_id: str = None
    url_expire_sec: int = field(default=14400, repr=False)
    fields: GetFileFields = field(default='*', repr=False)
    image_thumbnail_process: str = field(default='image/resize,w_160/format,jpeg', repr=False)
    image_url_process: str = field(default='image/resize,w_1920/format,jpeg', repr=False)
    video_thumbnail_process: str = field(default='video/snapshot,t_0,f_jpg,ar_auto,w_800', repr=False)
