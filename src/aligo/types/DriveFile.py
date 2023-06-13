"""..."""
from dataclasses import dataclass

from aligo.types import DataClass


@dataclass
class DriveFile(DataClass):
    drive_id: str = None
    file_id: str = None
