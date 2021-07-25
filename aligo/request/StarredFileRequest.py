"""..."""
from dataclasses import dataclass

from aligo.types import DataClass


@dataclass
class StarredFileRequest(DataClass):
    """..."""
    drive_id: str = None
    file_id: str = None
    starred: bool = True

    def __post_init__(self):
        super(StarredFileRequest, self).__post_init__()
        if self.starred:
            self.custom_index_key = 'starred_yes'
        else:
            self.custom_index_key = ''
