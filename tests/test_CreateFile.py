"""测试上传文件"""

import arrow
import requests

from aligo import *

CreateFile_file = '60f8fc0b3119e2cd76bf412481426947eb97aed6'
upload_test = r'./upload_test.txt'


def test_upload():
    ali = AligoCore()
    with open(upload_test, 'wb') as f:
        f.write(requests.get('https://juejin.cn/user/817692383391879').content)
    file = ali.upload_file(upload_test, parent_file_id=CreateFile_file, name=arrow.now().__str__() + '.html')
    assert isinstance(file, BaseFile)
    print(file)
