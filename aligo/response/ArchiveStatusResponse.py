"""..."""
from dataclasses import dataclass, field
from typing import List

from aligo.types import DataClass


@dataclass
class ArchiveStatusResponse(DataClass):
    """..."""
    file_list: List[str] = field(default_factory=list)
    progress: int = None
    state: str = None
    task_id: str = None
