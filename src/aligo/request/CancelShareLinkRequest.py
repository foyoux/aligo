"""取消分享链接请求"""

from dataclasses import dataclass

from aligo.types import *


@dataclass
class CancelShareLinkRequest(DataClass):
    """..."""
    share_id: str
