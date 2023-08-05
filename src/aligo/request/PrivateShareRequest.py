"""..."""
from dataclasses import dataclass, field
from typing import List

from aligo.types import DatClass, DriveFile


@dataclass
class PrivateShareRequest(DatClass):
    drive_file_list: List[DriveFile] = field(default_factory=list)
