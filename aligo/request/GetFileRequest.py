"""..."""

from dataclasses import dataclass, field

from aligo.types import DataClass
from aligo.config import GetFileFields


@dataclass
class GetFileRequest(DataClass):
    # @dataclass(unsafe_hash=True)
    """..."""
    file_id: str
    drive_id: str = None
    url_expire_sec: int = field(default=None, repr=False)
    fields: GetFileFields = field(default='*', repr=False)
    image_thumbnail_process: str = field(default='image/resize,w_160/format,jpeg', repr=False)
    image_url_process: str = field(default='image/resize,w_1920/format,jpeg', repr=False)
    video_thumbnail_process: int = field(default='video/snapshot,t_0,f_jpg,ar_auto,w_300', repr=False)

    def __hash__(self):
        return self.__dict__.__str__().__hash__()
