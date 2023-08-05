"""..."""
from dataclasses import dataclass

from aligo.types import DatClass


@dataclass
class GetDriveRequest(DatClass):
    """..."""
    drive_id: str = None
