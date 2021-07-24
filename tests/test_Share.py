"""..."""
import time

from aligo import *

share_file = '60f8970585be42d7b6b5466db2f033f161361fe9'
share_file2 = '60f898a1e1538782abe84b2c8bcc89cb09017b40'

def test_share():
    ali = AligoCore()

    share_request = ali.share_file(CreateShareLinkRequest(
        file_id_list=[share_file, share_file2],
        share_pwd='2021',
        description='aligo share test'
    ))

    assert isinstance(share_request, CreateShareLinkResponse)
    assert isinstance(share_request.created_at, str)
    assert isinstance(share_request.creator, str)
    assert isinstance(share_request.file_id_list, list)
    assert share_request.file_id_list.__len__() == 2
    assert isinstance(share_request.first_file, ShareLinkBaseFile)
    assert share_request.share_pwd == '2021'
    assert share_request.description == 'aligo share test'

    # 2.
    share_update = ali.update_share(UpdateShareLinkRequest(
        share_id=share_request.share_id,
        share_pwd='6666'
    ))
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
        cancel_share = ali.cancel_share(CancelShareLinkRequest(
            share_id=i.share_id
        ))
        assert isinstance(cancel_share, CancelShareLinkResponse)
