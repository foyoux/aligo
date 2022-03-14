"""..."""

from dataclasses import dataclass

from aligo.types import *
from aligo.types.Enum import *


@dataclass
class CreateFolderRequest(DataClass):
    """..."""
    name: str
    parent_file_id: str = 'root'
    drive_id: str = None
    check_name_mode: CheckNameMode = 'auto_rename'
    type: BaseFileType = None

    def __post_init__(self):
        self.type: BaseFileType = 'folder'
        super().__post_init__()
