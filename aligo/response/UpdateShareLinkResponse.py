"""更新分享链接响应"""

from dataclasses import dataclass, field
from typing import List

from aligo.types import DataClass
from aligo.types.Enum import *
from aligo.types.ShareLinkBaseFile import ShareLinkBaseFile


@dataclass
class UpdateShareLinkResponse(DataClass):
    """更新分享链接响应"""

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
    file_path_list: List[str] = field(default_factory=list)
    drive_file_list: List[str] = None
    report_count: int = 0
    video_preview_count: int = 0
    category: str = None
    enable_file_changed_notify: bool = False
    disable_preview: bool = False
    disable_save: bool = False
    disable_download: bool = False
    preview_limit: int = 0
    save_download_limit: int = 0
    require_login: bool = False
    enable_upload: bool = False
