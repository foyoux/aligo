"""..."""
from dataclasses import field, dataclass

from aligo.types import DataClass


@dataclass
class SearchFileRequest(DataClass):
    """..."""
    query: str
    drive_id: str = None
    limit: int = field(default=100, repr=False)
    image_thumbnail_process: str = field(default='image/resize,w_160/format,jpeg', repr=False)
    image_url_process: str = field(default='image/resize,w_1920/format,jpeg', repr=False)
    marker: str = field(default=None, repr=False)
    order_by: str = field(default=None, repr=False)
    url_expire_sec: int = field(default=14400, repr=False)
    video_thumbnail_process: str = field(default='video/snapshot,t_0,f_jpg,ar_auto,w_800', repr=False)
