"""..."""

from dataclasses import dataclass

from aligo.types import *


@dataclass
class GetStarredListRequest(DataClass):
    """..."""

    drive_id: str = None
    fields: GetStarredListFields = '*'
    image_thumbnail_process: str = 'image/resize,w_160/format,jpeg'
    image_url_process: str = 'image/resize,w_1920/format,jpeg'
    url_expire_sec: int = None
    video_thumbnail_process: str = 'video/snapshot,t_0,f_jpg,ar_auto,w_300'
    order_by: GetFileListOrderBy = 'name'
    order_direction: OrderDirection = 'DESC'

    def __post_init__(self):
        super(GetStarredListRequest, self).__post_init__()
        self.custom_index_key: str = 'starred_yes'
        self.parent_file_id: str = 'root'
