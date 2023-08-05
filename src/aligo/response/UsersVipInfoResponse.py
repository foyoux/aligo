"""..."""
from dataclasses import dataclass, field
from typing import List

from aligo.types import DatClass


@dataclass
class VipInfo(DatClass):
    name: str = None
    code: str = None
    promotedAt: int = None
    expire: int = None


@dataclass
class UsersVipInfoResponse(DatClass):
    """..."""
    identity: str = None
    icon: str = None
    mediumIcon: str = None
    status: str = None
    vipList: List[VipInfo] = field(default_factory=list)
