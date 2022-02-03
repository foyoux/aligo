"""..."""
from dataclasses import dataclass, field
from typing import List

from aligo.types import *
from aligo.types.Enum import *


@dataclass
class CreateShareLinkResponse(DataClass):
    """
    分享链接结构对象, 类似 BaseShareFile 的含义
    Attributes:
        created_at (str): 分享创建时间
        updated_at (str): 分享更新时间
        creator (str): 分享创建者
        description (str): 描述
        download_count (int):
        preview_count (int):
        save_count (int):
        drive_id (str):
        expiration (str): 分享过期时间
        expired (str): 分享是否过期
        file_id (str): 如果create时候是单个文件，那么file_id字段也有效，表示分享的一个文件的 id
        file_id_list (List[str]): 分享的一组文件或者文件加的列表
        share_id (str):
        share_msg (str): 分享口令
        share_name (str): 分享名
        share_policy (SharePolicy):
        share_pwd (str):
        share_url (str):
        status (str):
        first_file (ShareLinkBaseFile): 分享中首个文件的信息
    """
    created_at: str = None
    creator: str = None
    description: str = None
    download_count: int = 0
    drive_id: str = None
    expiration: str = None
    expired: bool = False
    file_id: str = None
    file_id_list: List[str] = field(default_factory=list)
    preview_count: int = 0
    save_count: int = 0
    share_id: str = None
    share_msg: str = None
    share_name: str = None
    share_policy: SharePolicy = None
    share_pwd: str = ''
    share_url: str = None
    status: str = None
    updated_at: str = None
    popularity: int = None
    is_photo_collection: bool = False
    sync_to_homepage: bool = False
    full_share_msg: str = None
    popularity_str: str = None
    display_name: str = None
    first_file: ShareLinkBaseFile = None
