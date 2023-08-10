"""多用户登录"""

from aligo import Aligo

if __name__ == '__main__':
    # 用户1
    ali1 = Aligo(name='user1')
    print(ali1.user_name, ali1.nick_name)
    # 用户2
    ali2 = Aligo(name='user2')
    print(ali2.user_name, ali2.nick_name)
