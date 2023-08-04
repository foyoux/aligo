"""..."""
from dataclasses import dataclass

from datclass import DatClass


@dataclass
class MoveFileToTrashRequest(DatClass):
    """..."""
    file_id: str
    drive_id: str = None
