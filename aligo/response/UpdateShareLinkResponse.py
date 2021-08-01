"""更新分享链接响应"""

from dataclasses import dataclass, field
from typing import List

from aligo.types import ShareLinkSchema


@dataclass
class UpdateShareLinkResponse(ShareLinkSchema):
    """更新分享链接响应"""
    file_path_list: List[str] = field(default_factory=list)
