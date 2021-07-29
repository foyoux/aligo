"""..."""

from aligo import *

test_file = '610225d2e10290d14fd94053bb9876b2e24bdee7'


def test_Recyclebin():
    ali = Aligo()

    # 1. move_file_to_trash
    trash = ali.move_file_to_trash(file_id=test_file)
    assert isinstance(trash, MoveFileToTrashResponse)
    # assert trash.file_id == test_file

    # 2. recyclebin_list
    trash_list = ali.get_recyclebin_list(GetRecycleBinListRequest())
    for trash in trash_list:
        assert isinstance(trash, BaseFile)

    # 3. restore_file
    file = ali.restore_file(file_id=test_file)
    assert isinstance(file, RestoreFileResponse)

    # 4. batch_move_to_trash
    batch = ali.batch_move_to_trash(
        file_id_list=[test_file]
    )
    for i in batch:
        assert isinstance(i, BatchSubResponse)
        # assert isinstance(i.body, MoveFileToTrashResponse)

    # 5. batch_restore_file
    batch = ali.batch_restore_files(
        file_id_list=[test_file]
    )
    for i in batch:
        assert isinstance(i, BatchSubResponse)
        # assert isinstance(i.body, RestoreFileResponse)
