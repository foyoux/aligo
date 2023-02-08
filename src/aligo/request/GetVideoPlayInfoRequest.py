"""..."""
from dataclasses import dataclass

from aligo.types import DataClass


@dataclass
class GetVideoPlayInfoRequest(DataClass):
    """..."""
    file_id: str
    drive_id: str = None
