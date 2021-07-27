"""测试复制文件接口"""

from aligo import *

CopyFile_folder = '60f7ce321e135ac51bd448e2a9f2d578125ba056'
test_file = '60f7ce4706a7e4c0a1624a9080194b776ead0f9e'


def test_copy_file():
    ali = Core()

    copy_file = ali.copy_file(
        CopyFileRequest(file_id=test_file, to_parent_file_id=CopyFile_folder, new_name='copy.png'))
    assert isinstance(copy_file, CopyFileResponse)
    assert copy_file.file_id != test_file
    assert copy_file.drive_id == ali.default_drive_id

    ali.move_file_to_trash(MoveFileToTrashRequest(file_id=copy_file.file_id))

    # 批量
    batch_copy_file = ali.batch_copy_files(BatchCopyFilesRequest(
        file_id_list=[test_file],
        to_parent_file_id=CopyFile_folder
    ))
    for i in batch_copy_file:
        assert isinstance(i, BatchResponse)
        ali.move_file_to_trash(MoveFileToTrashRequest(file_id=i.body.file_id))
