"""更新文件"""

import time

from aligo import *

test_file = '61022c6208aa18a07d5b4a099cfe76871ac9290b'


def test_rename():
    ali = Aligo()
    new_name = str(time.time_ns()) + '.jpg'
    new_file = ali.update_file(UpdateFileRequest(file_id=test_file, name=new_name))
    assert isinstance(new_file, BaseFile)
    assert new_file.name == new_name
