"""更新分享链接请求"""
from dataclasses import dataclass

from aligo.types import DataClass


@dataclass
class UpdateShareLinkRequest(DataClass):
    """
    更新分享链接请求

    Attributes:
        share_id (str):
        share_pwd (str): 提取码，0-64个字符。长度0表示没有提取码。
        expiration (str): 失效时间点。RFC3339格式，比如："2020-06-28T11:33:00.000+08:00"。永久有效: ""
        description (str): 描述
    """
    share_id: str
    share_pwd: str = None
    expiration: str = ''
    description: str = None
