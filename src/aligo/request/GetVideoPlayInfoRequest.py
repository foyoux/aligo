"""..."""
from dataclasses import dataclass

from datclass import DatClass


@dataclass
class GetVideoPlayInfoRequest(DatClass):
    """..."""
    file_id: str
    drive_id: str = None
