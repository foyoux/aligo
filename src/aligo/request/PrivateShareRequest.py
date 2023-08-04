"""..."""
from dataclasses import dataclass, field
from typing import List

from datclass import DatClass

from aligo.types import DriveFile


@dataclass
class PrivateShareRequest(DatClass):
    drive_file_list: List[DriveFile] = field(default_factory=list)
