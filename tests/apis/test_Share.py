"""..."""
import time

from aligo import *

test_share_file = '6102292d8344dce69ca8463084cc6022b67d2b24'
test_share_file2 = '6102292d902476876869429791bedf531b67e13b'
share_folder = '610227e8754759f1555645e79fba1f89771043fb'

share_id = 'kGyJ5u3GmKy'
share_id2 = 'nDtTamX9vTP'
share_pwd2 = 'w652'

ali = Aligo()


def test_share():
    share_request = ali.share_files(
        file_id_list=[test_share_file, test_share_file2],
        share_pwd='2021',
        description='aligo share test'
    )

    assert isinstance(share_request, CreateShareLinkResponse)
    assert isinstance(share_request.created_at, str)
    assert isinstance(share_request.creator, str)
    assert isinstance(share_request.file_id_list, list)
    assert len(share_request.file_id_list) == 2
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
        # assert isinstance(i.first_file, ShareLinkBaseFile)
        # 4. 取消
        cancel_share = ali.batch_cancel_share(
            share_id_list=[i.share_id]
        )
        for j in cancel_share:
            assert isinstance(j, BatchSubResponse)
            # assert isinstance(j.body, CancelShareLinkResponse)


def test_other_share():
    """..."""
    share_info = ali.get_share_info(share_id=share_id)
    assert isinstance(share_info, GetShareInfoResponse)

    share_info = ali.get_share_info(share_id=share_id2)
    assert isinstance(share_info, GetShareInfoResponse)

    share_token = ali.get_share_token(share_id=share_id2, share_pwd=share_pwd2)
    assert isinstance(share_token, GetShareTokenResponse)

    share_list = ali.get_share_file_list(share_id=share_id2, share_token=share_token)
    file_list = []
    for i in share_list:
        file_list.append(i.file_id)
        assert isinstance(i, BaseShareFile)
        share_file = ali.get_share_file(share_token=share_token,
                                        share_id=share_id2, file_id=i.file_id)
        assert isinstance(share_file, BaseShareFile)
        url = ali.get_share_link_download_url(
            share_id=share_id2, file_id=i.file_id,
            share_token=share_token
        )
        assert isinstance(url, GetShareLinkDownloadUrlResponse)
        x = ali.share_file_saveto_drive(share_id=share_id2, file_id=i.file_id, to_parent_file_id=share_folder,
                                        share_token=share_token)
        assert isinstance(x, ShareFileSaveToDriveResponse)
        assert isinstance(x.file_id, str)
        assert len(x.file_id) > 10
        y = ali.move_file_to_trash(file_id=x.file_id)
        assert isinstance(y, MoveFileToTrashResponse)

    x = ali.batch_share_file_saveto_drive(share_id=share_id2, file_id_list=file_list,
                                          share_token=share_token)
    for i in x:
        assert isinstance(i, BatchSubResponse)
        assert isinstance(i.body, BatchShareFileSaveToDriveResponse)
        y = ali.move_file_to_trash(file_id=i.body.file_id)
        assert isinstance(y, MoveFileToTrashResponse)
