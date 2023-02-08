"""..."""
from dataclasses import dataclass, field
from typing import List

from aligo.types import DataClass
from aligo.types import UploadPartInfo


@dataclass
class CompleteFileRequest(DataClass):
    """..."""
    file_id: str = None
    drive_id: str = None
    upload_id: str = None
    part_info_list: List[UploadPartInfo] = field(default_factory=list, repr=False)
