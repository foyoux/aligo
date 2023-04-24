from aligo import Aligo


class CAligo(Aligo):
    def sign_in_list(self):
        return self._post(
            '/v1/activity/sign_in_list',
            host='https://member.aliyundrive.com',
            body={'isReward': True},
            params={'_rx-s': 'mobile'}
        )

    def sign_in_reward(self, day):
        return self._post(
            '/v1/activity/sign_in_reward',
            host='https://member.aliyundrive.com',
            body={'signInDay': day},
            params={'_rx-s': 'mobile'}
        )

    def sign_in_festival(self):
        return self._post(
            '/v1/activity/sign_in_list',
            host='https://member.aliyundrive.com',
            body={},
            params={'_rx-s': 'mobile'}
        )


if __name__ == '__main__':
    ali = CAligo()
    # noinspection PyProtectedMember
    log = ali._auth.log

    # 获取签到列表
    resp = ali.sign_in_list()
    result = resp.json()['result']
    signInCount = result['signInCount']
    log.info("本月签到次数: %d", signInCount)

    # 签到
    resp = ali.sign_in_reward(signInCount)
    log.info(resp.json()['result']['notice'])
