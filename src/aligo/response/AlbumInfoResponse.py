"""..."""
from dataclasses import dataclass

from datclass import DatClass


@dataclass
class AlbumInfoResponse(DatClass):
    """..."""
    driveId: str = None
    driveName: str = None
