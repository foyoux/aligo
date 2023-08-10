"""..."""
from dataclasses import dataclass, field
from typing import Dict, List

from aligo.core import BaseAligo
from aligo.core.Config import (ADRIVE_V1_USER_CONFIG_GET, MEMBER_HOST, V1_USERS_REWARDS, V2_USER_GET,
                               BUSINESS_V1_USERS_VIP_INFO, USERS_V2_USERS_DEVICE_LIST, USER_HOST)
from aligo.response import RewardSpaceResponse, UsersVipInfoResponse
from aligo.types import BaseUser, UserConfig, LoginDevice
from aligo.types.Type import DatClass


@dataclass
class PhoneBackUp(DatClass):
    folder_id: str = None
    photo_folder_id: str = None
    sub_folder: Dict = None
    video_folder_id: str = None


@dataclass
class BackUpConfig(DatClass):
    # noinspection NonAsciiCharacters
    手机备份: PhoneBackUp = None


@dataclass
class UserData(DatClass):
    back_up_config: BackUpConfig = None


@dataclass
class UserResponse(DatClass):
    avatar: str = field(default=None, repr=False)
    backup_drive_id: str = field(default=None, repr=False)
    created_at: int = field(default=None, repr=False)
    creator: str = field(default=None, repr=False)
    creator_level: str = field(default=None, repr=False)
    default_drive_id: str = None
    default_location: str = field(default=None, repr=False)
    deny_change_password_by_self: bool = field(default=None, repr=False)
    description: str = field(default=None, repr=False)
    domain_id: str = None
    email: str = field(default=None, repr=False)
    expire_at: str = field(default=None, repr=False)
    last_login_time: int = field(default=None, repr=False)
    need_change_password_next_login: bool = field(default=None, repr=False)
    nick_name: str = None
    phone: str = field(default=None, repr=False)
    phone_region: str = field(default=None, repr=False)
    punish_flag: str = field(default=None, repr=False)
    punishments: str = field(default=None, repr=False)
    resource_drive_id: str = None
    role: str = None
    sbox_drive_id: str = field(default=None, repr=False)
    status: str = field(default=None, repr=False)
    updated_at: int = field(default=None, repr=False)
    user_data: UserData = field(default=None, repr=False)
    user_id: str = None
    user_name: str = None
    vip_identity: str = field(default=None, repr=False)


class User(BaseAligo):
    """..."""

    def get_user(self, f5: bool = False) -> BaseUser:
        """
        获取用户信息
        :param f5: [可选] 是否强制刷新
        :return: [BaseUser]
        """
        if self._user is None or f5:
            response = self.post(V2_USER_GET)
            # response.status_code == 200 or self._error_log_exit(response)
            # self._user = BaseUser(**response.json())
            self._user = self._result(response, BaseUser)
        return self._user

    def rewards_space(self, code: str):
        """
        获取奖励空间
        :param code: [必选] 奖励码
        :return: [RewardSpaceResponse]

        >>> from aligo import Aligo
        >>> ali = Aligo()
        >>> result = ali.rewards_space('12345678')
        >>> print(result)
        """
        response = self.post(V1_USERS_REWARDS, MEMBER_HOST, body={
            'code': code
        })
        return self._result(response, RewardSpaceResponse)

    def get_user_config(self) -> UserConfig:
        """获取用户配置信息"""
        response = self.post(ADRIVE_V1_USER_CONFIG_GET, body={})
        return self._result(response, UserConfig)

    def get_vip_info(self) -> UsersVipInfoResponse:
        """获取用户vip信息"""
        response = self.post(BUSINESS_V1_USERS_VIP_INFO, body={})
        return self._result(response, UsersVipInfoResponse)

    def list_login_device(self) -> List[LoginDevice]:
        response = self.post(USERS_V2_USERS_DEVICE_LIST)
        return self._result(response, LoginDevice, field='result.devices')

    def v2_user_get(self) -> UserResponse:
        response = self.post(V2_USER_GET, host=USER_HOST)
        return self._result(response, UserResponse)
