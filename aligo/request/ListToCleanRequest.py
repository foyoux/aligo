"""..."""
from dataclasses import dataclass

from aligo.types import DataClass


@dataclass
class ListToCleanRequest(DataClass):
    """..."""
    drive_id: str
    album_drive_id: str
