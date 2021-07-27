"""todo"""
from dataclasses import dataclass

from aligo.types import *


@dataclass
class GetShareFileListRequest(DataClass):
    """..."""
    share_id: str = None
    starred: bool = None
    all: bool = None
    category: BaseFileCategory = None
    fields: str = None
    image_thumbnail_process: str = None
    image_url_process: str = None
    limit: int = None
    marker: str = None
    order_by: GetShareFileListOrderBy = None
    order_direction: OrderDirection = None
    parent_file_id: str = None
    status: str = None
    type: BaseFileType = None
    url_expire_sec: int = None
    video_thumbnail_process: str = None
