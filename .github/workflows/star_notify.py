"""..."""
import os
import sys

import requests
import yagmail

if __name__ == '__main__':
    token = sys.argv[4]
    user, repo = os.getenv('GITHUB_REPOSITORY').split('/')
    data = requests.post(
        'https://api.github.com/graphql',
        json={
            'query': '{ repository(name: "' + repo + '", owner: "' + user + '") { stargazerCount stargazers(last: 1) { edges { node { name url avatarUrl email } } } } }'},
        headers={
            'Authorization': 'Bearer ' + token,
        }
    ).json()['data']
    last_user = data['repository']['stargazers']['edges'][0]['node']
    yag = yagmail.SMTP(sys.argv[1], sys.argv[2], 'smtp.qq.com', 465)
    yag.send(sys.argv[3], f'[{user}/{repo}] Started', f"""
        <div style="text-align: center;">
            <h1>{data['repository']['stargazerCount']} 💕</h1>
            <img src="{last_user['avatarUrl']}" alt="avatar" style="width:200px; border-radius: 100px">
            <div style="margin: 10px; font-size: x-large">{last_user['name']} {last_user['email']}</div>
            <a href="{last_user['url']}" style="display: block; font-size: large">{last_user['url']}</a>
        </div>
    """)
