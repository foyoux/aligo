"""..."""
from dataclasses import dataclass

from datclass import DatClass


@dataclass
class GetDriveRequest(DatClass):
    """..."""
    drive_id: str = None
