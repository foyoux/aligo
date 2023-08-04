"""..."""
from dataclasses import dataclass

from datclass import DatClass


@dataclass
class ListToCleanRequest(DatClass):
    """..."""
    drive_id: str
    album_drive_id: str
