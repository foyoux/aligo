"""..."""
from dataclasses import dataclass, field
from typing import List

from aligo.types import DataClass, DriveFile


@dataclass
class PrivateShareRequest(DataClass):
    drive_file_list: List[DriveFile] = field(default_factory=list)
