from dataclasses import dataclass, field
from typing import List, Dict

from datclass import DatClass

from aligo import Aligo
from aligo.core import Config


@dataclass
class Reward(DatClass):
    action: str = None
    background: str = None
    bottleId: str = None
    bottleName: str = None
    bottleShareId: str = None
    color: str = None
    description: str = None
    detailAction: str = None
    goodsId: int = None
    name: str = None
    notice: str = None
    subNotice: str = None


@dataclass
class Signinlogs(DatClass):
    calendarChinese: str = None
    calendarDay: str = None
    calendarMonth: str = None
    day: int = None
    icon: str = None
    isReward: bool = None
    notice: str = None
    pcAndWebIcon: str = None
    poster: str = None
    reward: Reward = None
    rewardAmount: int = None
    status: str = None
    themes: str = None
    type: str = None


@dataclass
class Result(DatClass):
    blessing: str = None
    description: str = None
    isReward: bool = None
    pcAndWebRewardCover: str = None
    rewardCover: str = None
    signInCount: int = None
    signInCover: str = None
    signInLogs: List[Signinlogs] = field(default_factory=list)
    signInRemindCover: str = None
    subject: str = None
    title: str = None


@dataclass
class SignInList(DatClass):
    arguments: str = None
    code: str = None
    maxResults: str = None
    message: str = None
    nextToken: str = None
    result: Result = None
    success: bool = None
    totalCount: str = None


@dataclass
class SignInReward(DatClass):
    arguments: str = None
    code: str = None
    maxResults: str = None
    message: str = None
    nextToken: str = None
    result: Reward = None
    success: bool = None
    totalCount: str = None


class CAligo(Aligo):
    V1_ACTIVITY_SIGN_IN_LIST = '/v1/activity/sign_in_list'
    V1_ACTIVITY_SIGN_IN_REWARD = '/v1/activity/sign_in_reward'

    def _sign_in(self, body: Dict = None):
        return self.post(
            CAligo.V1_ACTIVITY_SIGN_IN_LIST,
            host=Config.MEMBER_HOST,
            body=body, params={'_rx-s': 'mobile'}
        )

    def sign_in_list(self) -> SignInList:
        resp = self._sign_in({'isReward': True})
        return SignInList.from_str(resp.text)

    def sign_in_festival(self):
        return self._sign_in()

    def sign_in_reward(self, day) -> SignInReward:
        resp = self.post(
            CAligo.V1_ACTIVITY_SIGN_IN_REWARD,
            host=Config.MEMBER_HOST,
            body={'signInDay': day},
            params={'_rx-s': 'mobile'}
        )
        return SignInReward.from_str(resp.text)


if __name__ == '__main__':
    ali = CAligo()
    # noinspection PyProtectedMember
    log = ali._auth.log

    # 获取签到列表
    sign_in_list = ali.sign_in_list()
    log.info('本月签到次数: %d', sign_in_list.result.signInCount)

    # 签到
    for i in sign_in_list.result.signInLogs:
        if i.isReward:
            continue
        if i.status == 'normal':
            sign_in_reward = ali.sign_in_reward(i.day)
            log.info('签到成功: %s', sign_in_reward.result.notice)
