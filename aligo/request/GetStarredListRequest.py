"""..."""

from dataclasses import dataclass, field

from aligo.types import *


@dataclass
class GetStarredListRequest(DataClass):
    """..."""

    drive_id: str = None
    fields: GetStarredListFields = '*'
    image_thumbnail_process: str = 'image/resize,w_160/format,jpeg'
    image_url_process: str = field(default='image/resize,w_1920/format,jpeg', repr=False)
    url_expire_sec: int = field(default=14400, repr=False)
    video_thumbnail_process: str = field(default='video/snapshot,t_0,f_jpg,ar_auto,w_800', repr=False)
    order_by: GetFileListOrderBy = 'name'
    order_direction: OrderDirection = 'DESC'

    def __post_init__(self):
        super(GetStarredListRequest, self).__post_init__()
        self.custom_index_key: str = 'starred_yes'
        self.parent_file_id: str = 'root'
