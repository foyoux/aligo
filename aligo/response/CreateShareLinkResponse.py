"""..."""
from dataclasses import dataclass

from aligo.types import ShareLinkSchema


@dataclass
class CreateShareLinkResponse(ShareLinkSchema):
    """创建分享的响应
    Attributes:
        share_id (str): 分享码
        share_pwd (str): 提取码。如果没有传递，那么这里返回空串，表示不需要提取码
        share_url (str): 分享URL地址
        share_policy (str): url: 使用链接进行分享; msg: 使用口令进行分享
        description (str): 描述
        share_name (str): 分享名
        created_at (str): 分享创建时间
        expiration (str): 分享过期时间
    """
    ...
