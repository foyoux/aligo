"""..."""
from dataclasses import dataclass

from aligo.types import DataClass


@dataclass
class MoveFileToTrashRequest(DataClass):
    """..."""
    file_id: str
    drive_id: str = None
