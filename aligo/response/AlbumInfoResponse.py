"""..."""
from dataclasses import dataclass

from aligo.types import DataClass


@dataclass
class AlbumInfoResponse(DataClass):
    """..."""
    driveId: str = None
    driveName: str = None
