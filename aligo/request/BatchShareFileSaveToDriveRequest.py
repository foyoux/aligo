"""..."""
from dataclasses import dataclass, field
from typing import List

from aligo.types import DataClass


@dataclass
class BatchShareFileSaveToDriveRequest(DataClass):
    """..."""
    share_id: str
    file_id_list: List[str] = field(default_factory=list)
    to_parent_file_id: str = 'root'
    auto_rename: bool = True
    to_drive_id: str = None
