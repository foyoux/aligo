"""..."""
from dataclasses import dataclass

from aligo.types import *


@dataclass
class RenameFileRequest(DataClass):
    """..."""
    name: str
    file_id: str
    check_name_mode: CheckNameMode = 'refuse'
    drive_id: str = None
