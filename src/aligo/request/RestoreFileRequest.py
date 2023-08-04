"""..."""
from dataclasses import dataclass

from datclass import DatClass


@dataclass
class RestoreFileRequest(DatClass):
    """..."""
    file_id: str
    drive_id: str = None
