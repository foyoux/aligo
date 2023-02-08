"""GetUploadUrlRequest"""

from dataclasses import dataclass, field
from typing import List

from aligo.types import *


@dataclass
class GetUploadUrlRequest(DataClass):
    """GetUploadUrlRequest"""
    drive_id: str = None
    file_id: str = None
    upload_id: str = None
    content_md5: str = None
    part_info_list: List[UploadPartInfo] = field(default_factory=list, repr=False)
