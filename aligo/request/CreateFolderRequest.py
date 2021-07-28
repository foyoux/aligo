"""..."""

from dataclasses import dataclass

from aligo.types import *


@dataclass
class CreateFolderRequest(DataClass):
    """..."""
    name: str
    parent_file_id: str = 'root'
    drive_id: str = None
    check_name_mode: CheckNameMode = 'refuse'
    type: BaseFileType = None

    def __post_init__(self):
        self.type: BaseFileType = 'folder'
        super(CreateFolderRequest, self).__post_init__()
