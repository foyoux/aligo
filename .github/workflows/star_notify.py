"""..."""
import sys

import requests
import yagmail

if __name__ == '__main__':
    print('参数数量', len(sys.argv))
    data = requests.post(
        'https://api.github.com/graphql',
        json={
            'query': """{ repository(name: "aligo", owner: "foyoux") { stargazerCount stargazers(last: 1) { edges { node { name url avatarUrl email } } } } }"""},
        headers={
            'Authorization': 'Bearer ' + sys.argv[1],
        }
    ).json()['data']
    last_user = data['repository']['stargazers']['edges'][0]['node']
    yag = yagmail.SMTP(sys.argv[2], sys.argv[3], 'smtp.qq.com', 465)
    yag.send(sys.argv[4], 'aligo started', f"""
        <div style="text-align: center;">
            <h1>{data['repository']['stargazerCount']} 💕</h1>
            <img src="{last_user['avatarUrl']}" alt="avatar" style="width:200px; border-radius: 100px">
            <div style="margin: 10px; font-size: x-large">{last_user['name']}</div>
            <a href="{last_user['url']}" style="display: block; font-size: medium">{last_user['url']}</a>
        </div>
    """)
