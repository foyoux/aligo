"""..."""
from dataclasses import dataclass, field

from aligo.types import DataClass


@dataclass
class MoveFileRequest(DataClass):
    """..."""
    file_id: str
    drive_id: str = None
    to_drive_id: str = None
    to_parent_file_id: str = 'root'
    new_name: str = None
    auto_rename: bool = field(default=False, repr=False)
    overwrite: bool = field(default=False, repr=False)
