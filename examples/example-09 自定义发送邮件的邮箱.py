from aligo import Aligo, EMailConfig

if __name__ == '__main__':
    email_config = EMailConfig(
        email='<接收登录邮件的邮箱地址>',
        # 自配邮箱
        user='',
        password='',
        host='',
        port=0,
    )
    ali = Aligo(email=email_config)
