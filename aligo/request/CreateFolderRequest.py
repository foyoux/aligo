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

    def __post_init__(self):
        super(CreateFolderRequest, self).__post_init__()
        self.type: BaseFileType = 'folder'
