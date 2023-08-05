"""..."""
from dataclasses import dataclass

from .Type import DatClass


@dataclass
class DriveFile(DatClass):
    drive_id: str = None
    file_id: str = None
