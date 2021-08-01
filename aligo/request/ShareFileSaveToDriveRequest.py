"""..."""
from dataclasses import dataclass, field

from aligo.types import *


@dataclass
class ShareFileSaveToDriveRequest(DataClass):
    """..."""
    share_id: str
    file_id: str
    to_parent_file_id: str = 'root'
    new_name: str = None
    auto_rename: bool = field(default=True, repr=False)
    overwrite: bool = field(default=False, repr=False)
    to_drive_id: str = None
