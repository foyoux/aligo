"""..."""

from dataclasses import dataclass, field
from typing import List

from .DataClass import DataClass
from .Enum import *
from .ShareLinkBaseFile import ShareLinkBaseFile


@dataclass
class ShareLinkSchema(DataClass):
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
    share_id: str
    share_name: str = None
    share_pwd: str = None
    expiration: str = None
    created_at: str = field(default=None, repr=False)
    updated_at: str = field(default=None, repr=False)
    creator: str = field(default=None, repr=False)
    description: str = field(default=None, repr=False)
    download_count: int = field(default=0, repr=False)
    preview_count: int = field(default=0, repr=False)
    save_count: int = field(default=0, repr=False)
    drive_id: str = field(default=None, repr=False)
    expired: str = field(default=None, repr=False)
    file_id: str = field(default=None, repr=False)
    file_id_list: List[str] = field(default=None, repr=False)
    share_msg: str = field(default=None, repr=False)
    share_policy: SharePolicy = field(default=None, repr=False)
    share_url: str = field(default=None, repr=False)
    status: str = field(default=None, repr=False)
    first_file: ShareLinkBaseFile = field(default=None, repr=False)
    is_subscribed: bool = field(default=False, repr=False)
    num_of_subscribers: int = field(default=0, repr=False)
    display_name: str = field(default=None)
    current_sync_status: int = field(default=None, repr=False)
    next_sync_status: int = field(default=None, repr=False)
    full_share_msg: str = field(default=None, repr=False)
    ex_status: int = field(default=None, repr=False)
    popularity: int = None
    popularity_str: str = None
