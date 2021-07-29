"""..."""

import time

from aligo import *

ali = Core()

test_folder = '60fd508e43f9a6ced80a45b8873ee2fc8edde5aa'
test_file = '60fd50c77a0dee3fcb074070bfd86e3d43e2445a'


def test_starred_file():
    # 收藏
    file = ali.starred_file(StarredFileRequest(
        file_id=test_file
    ))
    assert isinstance(file, BaseFile)
    time.sleep(2)

    # 取消收藏
    file = ali.starred_file(StarredFileRequest(
        file_id=file.file_id,
        starred=False
    ))
    assert isinstance(file, BaseFile)


def test_get_starred_list():
    file_list = ali.get_starred_list(GetStarredListRequest())
    for i in file_list:
        assert isinstance(i, BaseFile)


def test_batch_star_files():
    # 批量收藏
    batch = ali.batch_star_files(BatchStarFilesRequest(
        file_id_list=[test_file]
    ))
    for i in batch:
        assert isinstance(i, BatchSubResponse)

        time.sleep(2)

        # 批量取消收藏
        batch2 = ali.batch_star_files(BatchStarFilesRequest(
            file_id_list=[test_file],
            starred=False
        ))
        for j in batch2:
            assert isinstance(j, BatchSubResponse)
