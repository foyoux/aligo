"""..."""
from dataclasses import dataclass, field
from typing import List

from aligo.config import BaseFileContentHashName
from aligo.config import BaseFileType
from aligo.config import CheckNameMode
from aligo.types import DataClass
from aligo.types import UploadPartInfo


@dataclass
class CreateFileRequest(DataClass):
    """..."""
    name: str
    file_id: str = None
    type: BaseFileType = 'folder'
    parent_file_id: str = 'root'
    size: int = field(default=None, repr=False)
    check_name_mode: CheckNameMode = field(default=None, repr=False)
    content_hash: str = field(default=None, repr=False)
    content_hash_name: BaseFileContentHashName = field(default=None, repr=False)
    content_md5: str = field(default=None, repr=False)
    content_type: str = field(default=None, repr=False)
    description: str = field(default=None, repr=False)
    drive_id: str = field(default=None, repr=False)
    encrypt_mode: str = field(default=None, repr=False)
    hidden: str = field(default=None, repr=False)
    labels: List[str] = field(default=None, repr=False)
    last_updated_at: str = field(default=None, repr=False)
    meta: str = field(default=None, repr=False)
    part_info_list: List[UploadPartInfo] = field(default=None, repr=False)
    pre_hash: str = field(default=None, repr=False)
    user_meta: str = field(default=None, repr=False)

    # def __post_init__(self):
    #     self.part_info_list = _null_list(UploadPartInfo, self.part_info_list)
