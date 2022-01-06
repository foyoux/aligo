"""多用户登录"""

from aligo import Aligo

if __name__ == '__main__':
    """
    注意：老版本，多用户登录用的是 Auth 对象，新版本已将 Auth 参数全部移至 Aligo
    注意：老版本，多用户登录用的是 Auth 对象，新版本已将 Auth 参数全部移至 Aligo
    注意：老版本，多用户登录用的是 Auth 对象，新版本已将 Auth 参数全部移至 Aligo
    """
    # 用户1
    ali1 = Aligo(name='user1')
    print(ali1.user_name, ali1.nick_name)
    # 用户2
    ali2 = Aligo(name='user2')
    print(ali2.user_name, ali2.nick_name)
