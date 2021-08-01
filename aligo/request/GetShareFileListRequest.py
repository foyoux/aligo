"""获取分享文件列表"""
from dataclasses import dataclass, field

from aligo.types import *
from aligo.types.Enum import *


@dataclass
class GetShareFileListRequest(DataClass):
    """..."""
    share_id: str = None
    starred: bool = None
    all: bool = None
    category: BaseFileCategory = None
    fields: str = None
    image_thumbnail_process: str = None
    image_url_process: str = field(default='image/resize,w_1920/format,jpeg', repr=False)
    limit: int = None
    marker: str = None
    order_by: GetShareFileListOrderBy = 'name'
    order_direction: OrderDirection = 'DESC'
    parent_file_id: str = 'root'
    status: str = None
    type: BaseFileType = None
    url_expire_sec: int = field(default=14400, repr=False)
    video_thumbnail_process: str = field(default='video/snapshot,t_0,f_jpg,ar_auto,w_800', repr=False)
