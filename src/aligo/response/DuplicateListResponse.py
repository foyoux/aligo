"""..."""
from dataclasses import dataclass, field
from typing import List

from aligo.types import DataClass


@dataclass
class DuplicateFileInfo(DataClass):
    """..."""
    name: str = None
    thumbnail: str = None
    type: str = None
    category: str = None
    size: int = None
    starred: bool = None
    parent_file_id: str = None
    drive_id: str = None
    file_id: str = None
    file_extension: str = None
    content_hash: str = None
    created_at: str = None
    updated_at: str = None
    trashed_at: str = None
    mime_type: str = None


@dataclass
class DuplicateItem(DataClass):
    """..."""
    items: List[DuplicateFileInfo] = field(default_factory=list)
    group_id: str = ''


@dataclass
class DuplicateListResponse(DataClass):
    """..."""
    items: List[DuplicateItem] = field(default_factory=list)
    next_marker: str = ''
