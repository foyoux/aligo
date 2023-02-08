"""..."""

from dataclasses import dataclass, field

from aligo.types import *
from aligo.types.Enum import *


@dataclass
class GetFileListRequest(DataClass):
    """..."""
    parent_file_id: str = 'root'
    drive_id: str = None
    starred: bool = field(default=None, repr=False)
    all: bool = field(default=False, repr=False)
    category: BaseFileCategory = field(default=None, repr=False)
    fields: GetFileListFields = field(default='*', repr=False)
    image_thumbnail_process: str = field(default='image/resize,w_400/format,jpeg', repr=False)
    image_url_process: str = field(default='image/resize,w_1920/format,jpeg', repr=False)
    limit: int = field(default=200, repr=False)
    marker: str = field(default=None, repr=False)
    order_by: GetFileListOrderBy = field(default='updated_at', repr=False)
    order_direction: OrderDirection = field(default='DESC', repr=False)
    status: str = field(default=None, repr=False)
    type: BaseFileType = field(default=None, repr=False)
    url_expire_sec: int = field(default=14400, repr=False)
    video_thumbnail_process: str = field(default='video/snapshot,t_0,f_jpg,ar_auto,w_800', repr=False)
