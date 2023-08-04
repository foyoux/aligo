"""取消分享链接请求"""
from dataclasses import dataclass

from datclass import DatClass


@dataclass
class CancelShareLinkRequest(DatClass):
    """..."""
    share_id: str
