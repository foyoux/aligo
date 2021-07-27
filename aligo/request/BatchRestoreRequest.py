"""..."""
from dataclasses import dataclass, field
from typing import List

from aligo.types import DataClass


@dataclass
class BatchRestoreRequest(DataClass):
    """..."""
    drive_id: str = None
    file_id_list: List[str] = field(default_factory=list)
