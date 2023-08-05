"""..."""
from dataclasses import dataclass

from aligo.types import DatClass


@dataclass
class ListToCleanRequest(DatClass):
    """..."""
    drive_id: str
    album_drive_id: str
