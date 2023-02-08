"""..."""

from dataclasses import dataclass, field

from .DataClass import DataClass


# 1. 只 REPR 能理解的数据
# 2. 尽可能的少
# 3. 不知道的不处理, 默认


@dataclass
class BaseUser(DataClass):
    """..."""
    user_name: str = None
    user_id: str = None
    default_drive_id: str = None
    description: str = field(default=None, repr=False)
    nick_name: str = field(default=None, repr=False)
    email: str = field(default=None, repr=False)
    phone: str = field(default=None, repr=False)
    role: str = field(default=None, repr=False)
    status: str = field(default=None, repr=False)
    created_at: int = field(default=None, repr=False)
    domain_id: str = field(default=None, repr=False)
    updated_at: int = field(default=None, repr=False)
    avatar: str = field(default=None, repr=False)
    user_data: dict = field(default=None, repr=False)
    deny_change_password_by_self: bool = field(default=False, repr=False)
    need_change_password_next_login: bool = field(default=False, repr=False)
    permission: str = field(default=None, repr=False)
    creator: str = None
    expired_at: int = 0
    default_location: str = ''
