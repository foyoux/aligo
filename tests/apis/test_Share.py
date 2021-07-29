"""..."""
import time

from aligo import *

share_file = '6102292d8344dce69ca8463084cc6022b67d2b24'
share_file2 = '6102292d902476876869429791bedf531b67e13b'


def test_share():
    ali = Aligo()

    share_request = ali.share_file(
        file_id_list=[share_file, share_file2],
        share_pwd='2021',
        description='aligo share test'
    )

    assert isinstance(share_request, CreateShareLinkResponse)
    assert isinstance(share_request.created_at, str)
    assert isinstance(share_request.creator, str)
    assert isinstance(share_request.file_id_list, list)
    assert share_request.file_id_list.__len__() == 2
    assert share_request.share_pwd == '2021'
    assert share_request.description == 'aligo share test'

    # 2.
    share_update = ali.update_share(
        share_id=share_request.share_id,
        share_pwd='6666'
    )
    assert isinstance(share_update, UpdateShareLinkResponse)
    assert share_update.share_pwd == '6666'

    # 延迟几秒, 解决无法获取新分享的问题
    time.sleep(2)

    # 3.
    share_list = ali.get_share_list()
    for i in share_list:
        assert isinstance(i, ShareLinkSchema)
        assert isinstance(i.created_at, str)
        assert isinstance(i.creator, str)
        assert isinstance(i.file_id_list, list)
        assert isinstance(i.first_file, ShareLinkBaseFile)
        # 4. 取消
        cancel_share = ali.batch_cancel_share(
            share_id_list=[i.share_id]
        )
        for j in cancel_share:
            assert isinstance(j, BatchSubResponse)
            # assert isinstance(j.body, CancelShareLinkResponse)
