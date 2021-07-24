"""..."""
from dataclasses import dataclass, field
from typing import List, Dict

from aligo.types import DataClass, UploadPartInfo
from aligo.config import BaseFileStatus, BaseFileType


@dataclass
class CreateFileResponse(DataClass):
    """..."""
    file_name: str = None
    file_id: str = None
    parent_file_id: str = None
    domain_id: str = field(default=None, repr=False)
    drive_id: str = field(default=None, repr=False)
    encrypt_mode: str = field(default=None, repr=False)
    part_info_list: List[UploadPartInfo] = field(default=None, repr=False)
    rapid_upload: bool = field(default=None, repr=False)
    status: BaseFileStatus = field(default=None, repr=False)
    streams_upload_info: Dict = field(default=None, repr=False)
    type: BaseFileType = field(default=None, repr=False)
    upload_id: str = field(default=None, repr=False)
    exist: bool = field(default=None, repr=False)
    location: str = field(default=None, repr=False)

    # pre_hash
    pre_hash: str = None
    code: str = None
    message: str = None

    # def __post_init__(self):
    #     self.part_info_list = _null_list(UploadPartInfo, self.part_info_list)
