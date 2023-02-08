"""..."""

from dataclasses import dataclass, field
from typing import List

from aligo.types import DataClass


@dataclass
class BatchCopyFilesRequest(DataClass):
    """..."""
    drive_id: str = None
    file_id_list: List[str] = field(default_factory=list)
    to_parent_file_id: str = 'root'
    overwrite: bool = False
    auto_rename: bool = True
