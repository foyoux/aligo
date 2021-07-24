"""..."""
import json
import random
import re

import requests

from aligo.config import *

if __name__ == '__main__':
    session = requests.session()

    session.get(
        'https://auth.aliyundrive.com' + '/v2/oauth/authorize',
        params={
            'login_type': 'custom',
            'response_type': 'code',
            'redirect_uri': 'https://www.aliyundrive.com/sign/callback',
            'client_id': CLIENT_ID,
            # 'state': r'{"origin":"file://"}',
            'state': '{"origin":"https://www.aliyundrive.com"}',
        }, stream=True).close()

    rnd = random.random()
    response = session.get('https://passport.aliyundrive.com/mini_login.htm', params={
        'lang': 'zh_cn',
        'appName': 'aliyun_drive',
        'appEntrance': 'web',
        'styleType': 'auto',
        'bizParams': '',
        'notLoadSsoView': 'false',
        'notKeepLogin': 'false',
        'isMobile': 'false',
        'hidePhoneCode': 'true',
        'rnd': rnd,
    })

    body = {
        'phoneCode': '86',
        'loginId': '15549727151',
        'countryCode': 'CN',
        'navUserAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
    }

    rt = re.findall('"loginFormData":({[^}]+})', response.text)
    body.update(json.loads(rt[0]))

    response = session.post(
        'https://passport.aliyundrive.com/newlogin/sms/send.do',
        headers={
            'referer':	response.url
        },
        params={
            'appName': 'aliyun_drive',
            'fromSite': 52,
            '_bx-v': '2.0.47',
        },
        data=body
    )

    print(response)
