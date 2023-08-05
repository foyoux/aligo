"""..."""
from dataclasses import dataclass

from aligo.types import DatClass


@dataclass
class GetAudioPlayInfoRequest(DatClass):
    """..."""
    file_id: str
    drive_id: str = None
