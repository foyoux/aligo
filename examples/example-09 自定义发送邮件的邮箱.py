from aligo import Aligo, Auth

if __name__ == '__main__':
    # 自己修改
    Auth._EMAIL_USER = 'xxxx@163.com'
    Auth._EMAIL_PASSWORD = '<授权码>'
    Auth._EMAIL_HOST = 'smtp.163.com'
    Auth._EMAIL_PORT = 465
    ali = Aligo()
