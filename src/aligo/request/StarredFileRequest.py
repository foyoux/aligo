"""..."""
from dataclasses import dataclass

from aligo.types import DataClass


@dataclass
class StarredFileRequest(DataClass):
    """..."""
    drive_id: str = None
    file_id: str = None
    starred: bool = True
    custom_index_key: str = None

    def __post_init__(self):
        if self.starred:
            self.custom_index_key = 'starred_yes'
        else:
            self.custom_index_key = ''
        super().__post_init__()
