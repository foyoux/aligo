"""..."""
from dataclasses import dataclass
from typing import List

from aligo.types import DataClass


@dataclass
class CreateShareLinkRequest(DataClass):
    """创建分享链接请求

    Attributes:
        drive_id (str):
        file_id_list (List[str]):
        share_pwd (str): 提取码，0-64个字符。长度0表示没有提取码。
        expiration (str): 失效时间点。RFC3339格式，比如："2020-06-28T11:33:00.000+08:00"。永久有效: ""
        description (str): 描述
    """
    drive_id: str = None
    file_id_list: List[str] = None
    share_pwd: str = None
    expiration: str = ''
    description: str = None
