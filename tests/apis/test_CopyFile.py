"""测试复制文件接口"""

from aligo import *

CopyFile_folder = '61021f35ed18d5d2dc814a73a3d72943b9d1344c'
test_file = '61021fa8fe1f0fce78d64383b6095533bf669b86'


def test_copy_file():
    ali = Aligo()

    copy_file = ali.copy_file(file_id=test_file, to_parent_file_id=CopyFile_folder, new_name='copy.png')
    assert isinstance(copy_file, CopyFileResponse)
    assert copy_file.file_id != test_file
    assert copy_file.drive_id == ali.default_drive_id

    ali.move_file_to_trash(file_id=copy_file.file_id)

    # 批量
    batch_copy_file = ali.batch_copy_files(
        file_id_list=[test_file],
        to_parent_file_id=CopyFile_folder
    )
    for i in batch_copy_file:
        assert isinstance(i, BatchSubResponse)
        assert isinstance(i.body, CopyFileResponse)
        ali.move_file_to_trash(file_id=i.body.file_id)
