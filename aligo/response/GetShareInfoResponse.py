"""..."""
from dataclasses import dataclass, field
from typing import List

from aligo.types import DataClass
from .ShareItemInfo import ShareItemInfo


@dataclass
class GetShareInfoResponse(DataClass):
    """..."""
    avatar: str = None
    creator_id: str = None
    creator_name: str = None
    creator_phone: str = None
    expiration: str = None
    file_count: int = None
    file_infos: List[ShareItemInfo] = field(default_factory=list)
    share_name: str = None
    updated_at: str = None
    vip: str = None
    display_name: str = field(default=None, repr=False)
    is_following_creator: bool = False
