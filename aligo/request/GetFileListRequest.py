"""..."""

from dataclasses import dataclass, field

from aligo.types import DataClass
from aligo.config import BaseFileCategory, GetFileListFields, GetFileListOrderBy, OrderDirection, BaseFileType


@dataclass
class GetFileListRequest(DataClass):
    # @dataclass(unsafe_hash=True)
    """..."""
    drive_id: str = None
    parent_file_id: str = 'root'
    starred: bool = field(default=None, repr=False)
    all: bool = field(default=False, repr=False)
    category: BaseFileCategory = field(default=None, repr=False)
    fields: GetFileListFields = field(default='*', repr=False)
    image_thumbnail_process: str = field(default='image/resize,w_160/format,jpeg', repr=False)
    image_url_process: str = field(default='image/resize,w_1920/format,jpeg', repr=False)
    limit: int = field(default=200, repr=False)
    marker: str = field(default=None, repr=False)
    order_by: GetFileListOrderBy = field(default='name', repr=False)
    order_direction: OrderDirection = field(default='ASC', repr=False)
    status: str = field(default=None, repr=False)
    type: BaseFileType = field(default=None, repr=False)
    url_expire_sec: int = field(default=None, repr=False)
    video_thumbnail_process: str = field(default='video/snapshot,t_0,f_jpg,ar_auto,w_300', repr=False)

    def __hash__(self):
        return self.__dict__.__str__().__hash__()
