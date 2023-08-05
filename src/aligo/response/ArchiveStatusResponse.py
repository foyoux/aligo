"""..."""
from dataclasses import dataclass, field
from typing import List

from aligo.types import DatClass


@dataclass
class ArchiveStatusResponse(DatClass):
    """..."""
    file_list: List[str] = field(default_factory=list)
    progress: int = None
    state: str = None
    task_id: str = None
