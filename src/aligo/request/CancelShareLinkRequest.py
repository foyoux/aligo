"""取消分享链接请求"""
from dataclasses import dataclass

from aligo.types import DatClass


@dataclass
class CancelShareLinkRequest(DatClass):
    """..."""
    share_id: str
