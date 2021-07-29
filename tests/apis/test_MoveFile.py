"""..."""

import time

from aligo import *

test_file = '610224132f840db7b7d44441addc1d42feacfc6d'
origin_folder = '610223ed3977087a5ca947af8a088a086393ccf1'
dest_folder = '610223e6022e7f1b724a4fcdb95b9e24221a641b'


def test_move_file():
    """..."""
    ali = Aligo()
    move = ali.move_file(file_id=test_file, to_parent_file_id=dest_folder)
    assert isinstance(move, MoveFileResponse)
    assert move.file_id == test_file

    time.sleep(1)
    batch_move = ali.batch_move_files(
        file_id_list=[test_file],
        to_parent_file_id=origin_folder
    )
    for i in batch_move:
        assert isinstance(i, BatchSubResponse)
        assert isinstance(i.body, MoveFileResponse)
        assert i.body.file_id == test_file
