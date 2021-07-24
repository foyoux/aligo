"""..."""

from aligo import *

test_file = '60f7d2f52f95ec2b00e444e2a35b9169351a6d49'
origin_folder = '60f7d2ca68ec26f0d79141f296cf3f849ab77b30'
dest_folder = '60f7d329831444ca213f4ffc801b75af50cfb8fb'


def test_move_file():
    """..."""
    ali = AligoCore()
    move = ali.move_file(MoveFileRequest(file_id=test_file, to_parent_file_id=dest_folder))
    assert isinstance(move, MoveFileResponse)
    assert move.file_id == test_file
    move = ali.move_file(MoveFileRequest(file_id=test_file, to_parent_file_id=origin_folder))
    assert isinstance(move, MoveFileResponse)
    assert move.file_id == test_file
