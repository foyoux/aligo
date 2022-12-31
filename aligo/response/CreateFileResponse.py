"""..."""
from dataclasses import dataclass, field
from typing import List, Dict

from aligo.types import *
from aligo.types.Enum import *


@dataclass
class CreateFileResponse(DataClass):
    """..."""
    file_name: str = None
    type: BaseFileType = None
    file_id: str = None
    parent_file_id: str = None
    domain_id: str = field(default=None, repr=False)
    drive_id: str = field(default=None, repr=False)
    encrypt_mode: str = field(default=None, repr=False)
    part_info_list: List[UploadPartInfo] = field(default_factory=list, repr=False)
    rapid_upload: bool = field(default=None, repr=False)
    status: BaseFileStatus = field(default=None, repr=False)
    streams_upload_info: Dict = field(default=None, repr=False)
    upload_id: str = field(default=None, repr=False)
    exist: bool = field(default=None, repr=False)
    location: str = field(default=None, repr=False)

    # pre_hash
    pre_hash: str = field(default=None, repr=False)
    # 与批量操作中的错误不同, 此处code为是否命中秒传的结果
    code: str = field(default=None, repr=False)
    message: str = field(default=None, repr=False)
    revision_id: str = field(default=None, repr=False)
