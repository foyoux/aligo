"""..."""
from dataclasses import dataclass, field

from .DataClass import DataClass


@dataclass(eq=False)
class Token(DataClass):
    """..."""
    user_name: str = None
    nick_name: str = None
    user_id: str = None
    default_drive_id: str = None
    # noinspection SpellCheckingInspection
    default_sbox_drive_id: str = None
    role: str = field(default=None, repr=False)
    status: str = field(default=None, repr=False)
    access_token: str = field(default=None, repr=False)
    refresh_token: str = field(default=None, repr=False)
    expires_in: int = field(default=None, repr=False)
    token_type: str = field(default=None, repr=False)
    avatar: str = field(default=None, repr=False)
    expire_time: str = field(default=None, repr=False)
    state: str = field(default=None, repr=False)
    exist_link: list = field(default=None, repr=False)
    need_link: bool = field(default=None, repr=False)
    user_data: dict = field(default=None, repr=False)
    pin_setup: bool = field(default=None, repr=False)
    is_first_login: bool = field(default=None, repr=False)
    need_rp_verify: bool = field(default=None, repr=False)
    device_id: str = field(default=None, repr=False)
    domain_id: str = field(default=None, repr=False)
    # noinspection SpellCheckingInspection
    hlogin_url: str = field(default=None, repr=False)
    # x-signature x-device-id x-nonce
    x_device_id: str = field(default=None, repr=False)
