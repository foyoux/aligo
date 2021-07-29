"""测试上传文件"""

from aligo import *

test_folder = '610221762cbc9455e5fb4eac8b7a7ac217285cbb'


def test_create_folder():
    ali = Aligo()
    folder = ali.create_folder(name='test_create_folder', parent_file_id=test_folder)
    assert isinstance(folder, CreateFileResponse)
    assert folder.type == 'folder'
    ali.move_file_to_trash(file_id=folder.file_id)
