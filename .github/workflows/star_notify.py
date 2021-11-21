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
    last = data['repository']['stargazers']['edges'][0]
    yag = yagmail.SMTP(sys.argv[2], sys.argv[3], 'smtp.qq.com', 465)
    yag.send(sys.argv[4], 'aligo 项目新增 star', f"""
    <div>
        <h1>aligo 项目新增 star</h1>
        <h2>当前总 star {data['repository']['stargazerCount']}</h2>
        <h3>最新 star 用户 {last['name']}</h3>
        <h4>最新 star 用户 repo {last['url']}</h3>
        <img src="{last['avatarUrl']}" />
    </div>
    """)
