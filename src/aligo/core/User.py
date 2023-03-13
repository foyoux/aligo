"""..."""

from typing import List

from aligo.core import *
from aligo.core.Config import *
from aligo.response import RewardSpaceResponse, UsersVipInfoResponse
from aligo.types import *


class User(BaseAligo):
    """..."""

    def get_user(self, f5: bool = False) -> BaseUser:
        """
        获取用户信息
        :param f5: [可选] 是否强制刷新
        :return: [BaseUser]
        """
        if self._user is None or f5:
            response = self._post(V2_USER_GET)
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
        response = self._post(V1_USERS_REWARDS, MEMBER_HOST, body={
            'code': code
        })
        return self._result(response, RewardSpaceResponse)

    def get_user_config(self) -> UserConfig:
        """获取用户配置信息"""
        response = self._post(ADRIVE_V1_USER_CONFIG_GET, body={})
        return self._result(response, UserConfig)

    def get_vip_info(self) -> UsersVipInfoResponse:
        """获取用户vip信息"""
        response = self._post(BUSINESS_V1_USERS_VIP_INFO, body={})
        return self._result(response, UsersVipInfoResponse)

    def list_login_device(self) -> List[LoginDevice]:
        response = self._post(USERS_V2_USERS_DEVICE_LIST)
        return self._result(response, LoginDevice, field='result.devices')
