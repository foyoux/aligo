"""..."""
from dataclasses import dataclass

from datclass import DatClass


@dataclass
class DriveFile(DatClass):
    drive_id: str = None
    file_id: str = None
