"""..."""
from dataclasses import dataclass

from datclass import DatClass

from aligo.types.Enum import *


@dataclass
class RenameFileRequest(DatClass):
    """..."""
    name: str
    file_id: str
    check_name_mode: CheckNameMode = 'refuse'
    drive_id: str = None
