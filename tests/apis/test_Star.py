"""..."""

import time

from aligo import *

ali = Aligo()

test_folder = '61022bb9920e19f960fd41c7bbdf33ee6ad4fbdc'
test_file = '61022bca0c0e83bf5d8e406d93bec951d818abf7'


def test_starred_file():
    # 收藏
    file = ali.starred_file(
        file_id=test_file
    )
    assert isinstance(file, BaseFile)
    time.sleep(2)

    # 取消收藏
    file = ali.starred_file(
        file_id=file.file_id,
        starred=False
    )
    assert isinstance(file, BaseFile)


def test_get_starred_list():
    file_list = ali.get_starred_list()
    for i in file_list:
        assert isinstance(i, BaseFile)


def test_batch_star_files():
    # 批量收藏
    batch = ali.batch_star_files(
        file_id_list=[test_file]
    )
    for i in batch:
        assert isinstance(i, BatchSubResponse)

        time.sleep(2)

        # 批量取消收藏
        batch2 = ali.batch_star_files(
            file_id_list=[test_file],
            starred=False
        )
        for j in batch2:
            assert isinstance(j, BatchSubResponse)
