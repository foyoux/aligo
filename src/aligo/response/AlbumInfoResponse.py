"""..."""
from dataclasses import dataclass

from aligo.types import DatClass


@dataclass
class AlbumInfoResponse(DatClass):
    """..."""
    driveId: str = None
    driveName: str = None
