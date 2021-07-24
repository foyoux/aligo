"""..."""
from dataclasses import dataclass

from aligo.types import DataClass


@dataclass(unsafe_hash=True)
class GetDriveRequest(DataClass):
    """..."""
    drive_id: str = None
