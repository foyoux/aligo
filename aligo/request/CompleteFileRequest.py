"""..."""
from dataclasses import dataclass
from typing import List

from aligo.types import DataClass
from aligo.types import UploadPartInfo


@dataclass(unsafe_hash=True)
class CompleteFileRequest(DataClass):
    """..."""
    file_id: str
    drive_id: str = None
    upload_id: str = None
    part_info_list: List[UploadPartInfo] = None
