"""..."""
from dataclasses import dataclass

from aligo.types import DataClass
from aligo.types.Enum import AlbumFileListType, OrderDirection


@dataclass
class AlbumListFilesRequest(DataClass):
    """..."""
    album_id: str = None
    fields: str = "*"
    filter: str = ""
    image_thumbnail_process: str = "image/resize,w_400/format,jpeg"
    image_url_process: str = "image/resize,w_1920/format,jpeg"
    limit: int = 100
    order_by: AlbumFileListType = "joined_at"
    order_direction: OrderDirection = "DESC"
    video_thumbnail_process: str = "video/snapshot,t_0,f_jpg,ar_auto,w_1000"
