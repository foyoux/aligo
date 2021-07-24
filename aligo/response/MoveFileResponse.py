"""..."""
from dataclasses import dataclass, field

from aligo.types import DataClass


@dataclass
class MoveFileResponse(DataClass):
    """..."""
    file_id: int = None
    drive_id: int = None
    domain_id: int = field(default=None, repr=False)
    async_task_id: str = field(default=None, repr=False)
