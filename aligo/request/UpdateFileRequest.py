"""..."""
from dataclasses import dataclass, field
from typing import List

from aligo.types import *
from aligo.types.Enum import *


@dataclass
class UpdateFileRequest(DataClass):
    """...."""
    name: str = None
    file_id: str = None
    drive_id: str = None
    check_name_mode: CheckNameMode = field(default='refuse', repr=False)
    custom_index_key: str = field(default=None, repr=False)
    description: str = field(default=None, repr=False)
    encrypt_mode: str = field(default=None, repr=False)
    hidden: str = field(default=None, repr=False)
    labels: List[str] = field(default=None, repr=False)
    meta: str = field(default=None, repr=False)
    starred: bool = field(default=None, repr=False)
    user_meta: str = field(default=None, repr=False)
