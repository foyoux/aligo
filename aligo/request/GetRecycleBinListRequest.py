"""..."""
from dataclasses import dataclass, field

from aligo.types import *
from aligo.types.Enum import *


@dataclass
class GetRecycleBinListRequest(DataClass):
    """..."""
    drive_id: str = None
    fields: str = field(default=None, repr=False)
    limit: int = field(default=200, repr=False)
    marker: str = field(default=None, repr=False)
    order_direction: OrderDirection = field(default='ASC', repr=False)
    order_by: GetRecycleBinListOrderBy = field(default='name', repr=False)
    status: str = field(default=None, repr=False)
    type: BaseFileType = field(default=None, repr=False)
    url_expire_sec: int = field(default=14400, repr=False)
    image_thumbnail_process: str = field(default='image/resize,w_160/format,jpeg', repr=False)
    image_url_process: str = field(default='image/resize,w_1920/format,jpeg', repr=False)
    video_thumbnail_process: str = field(default='video/snapshot,t_0,f_jpg,ar_auto,w_800', repr=False)
