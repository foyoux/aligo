"""..."""
from dataclasses import dataclass

from aligo.types import DataClass


@dataclass
class RestoreFileRequest(DataClass):
    """..."""
    file_id: str
    drive_id: str = None
