"""..."""
from dataclasses import dataclass, field
from typing import List

from aligo.types import DataClass


@dataclass
class BatchGetFileRequest(DataClass):
    """..."""
    file_id_list: List[str] = field(default_factory=list)
    drive_id: str = None
