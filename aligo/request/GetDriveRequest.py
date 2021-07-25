"""..."""
from dataclasses import dataclass

from aligo.types import DataClass


@dataclass
class GetDriveRequest(DataClass):
    """..."""
    drive_id: str = None
