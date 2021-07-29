"""更新文件"""

import time

from aligo import *

test_file = '60f89d6fdf584a2949844f88bd652194ff0d6721'


def test_rename():
    ali = Core()
    new_name = str(time.time_ns()) + '.jpg'
    new_file = ali.update_file(UpdateFileRequest(file_id=test_file, name=new_name))
    assert isinstance(new_file, BaseFile)
    assert new_file.name == new_name
