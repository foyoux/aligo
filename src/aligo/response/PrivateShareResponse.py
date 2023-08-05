"""..."""
from dataclasses import dataclass, field
from typing import List

from aligo.types import DatClass, DriveFile


@dataclass
class PrivateShareResponse(DatClass):
    drive_file_list: List[DriveFile] = field(default_factory=list)
    expiration: str = None
    expired: bool = None
    full_share_msg: str = None
    share_id: str = None
    share_name: str = None
    share_subtitle: str = None
    share_title: str = None
    share_url: str = None
    thumbnail: str = None
