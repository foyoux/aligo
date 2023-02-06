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
    print(r.status_code)
