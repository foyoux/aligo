"""..."""

from aligo import *

test_file = '60f89ce1579e1c6622c645169cc0f1b9756ad743'


def test_Recyclebin():
    ali = Core()

    # 1. move_file_to_trash
    trash = ali.move_file_to_trash(MoveFileToTrashRequest(file_id=test_file))
    assert isinstance(trash, MoveFileToTrashResponse)
    # assert trash.file_id == test_file

    # 2. recyclebin_list
    trash_list = ali.get_recyclebin_list(GetRecycleBinListRequest())
    for trash in trash_list:
        assert isinstance(trash, BaseFile)

    # 3. restore_file
    file = ali.restore_file(RestoreFileRequest(file_id=test_file))
    assert isinstance(file, RestoreFileResponse)

    # 4. batch_move_to_trash
    batch = ali.batch_move_to_trash(BatchMoveToTrashRequest(
        file_id_list=[test_file]
    ))
    for i in batch:
        assert isinstance(i, BatchResponse)

    # 5. batch_restore_file
    batch = ali.batch_restore_files(BatchRestoreRequest(
        file_id_list=[test_file]
    ))
    for i in batch:
        assert isinstance(i, BatchResponse)
