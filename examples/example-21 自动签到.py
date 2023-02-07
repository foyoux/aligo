import json

from aligo import Aligo


# 方法1
# if __name__ == '__main__':
#     ali = Aligo()
#     r = ali._post('/v1/activity/sign_in_list', host='https://member.aliyundrive.com', body={})
#     print(r.status_code)

# 方法2
class CAligo(Aligo):
    def sign_in_list(self):
        return self._post('/v1/activity/sign_in_list', host='https://member.aliyundrive.com', body={})


if __name__ == '__main__':
    ali = CAligo()
    r = ali.sign_in_list()
    result = json.loads(r.text)['result']
    signInCount = result['signInCount']
    signInLog = ""
    for i in result['signInLogs']:
        if i['day'] == signInCount:
            signInLog = i
            break
    if not signInLog == "":
        print("今日签到奖励:" + signInLog['reward']['name'] + signInLog['reward']['description'] + "本月签到次数:" + str(signInCount))
    else:
        print("签到失败")
