"""..."""
from dataclasses import dataclass, field
from typing import List

from aligo.types import DataClass


@dataclass
class VipInfo(DataClass):
    name: str = None
    code: str = None
    promotedAt: int = None
    expire: int = None


@dataclass
class UsersVipInfoResponse(DataClass):
    """..."""
    identity: str = None
    icon: str = None
    mediumIcon: str = None
    status: str = None
    vipList: List[VipInfo] = field(default_factory=list)
