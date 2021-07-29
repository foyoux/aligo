"""..."""
import time

from aligo import *

test_share_file = '60f8970585be42d7b6b5466db2f033f161361fe9'
test_share_file2 = '60f898a1e1538782abe84b2c8bcc89cb09017b40'
share_folder = '60f896b23e38e23784b94766924266dd3b701869'

share_id = 'kGyJ5u3GmKy'
share_id2 = 'nDtTamX9vTP'
share_pwd2 = 'w652'

ali = Core()


def test_share():
    share_request = ali.share_file(CreateShareLinkRequest(
        file_id_list=[test_share_file, test_share_file2],
        share_pwd='2021',
        description='aligo share test'
    ))

    assert isinstance(share_request, CreateShareLinkResponse)
    assert isinstance(share_request.created_at, str)
    assert isinstance(share_request.creator, str)
    assert isinstance(share_request.file_id_list, list)
    assert share_request.file_id_list.__len__() == 2
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


def test_other_share():
    """..."""
    share_info = ali.get_share_info(GetShareInfoRequest(
        share_id=share_id
    ))
    assert isinstance(share_info, GetShareInfoResponse)

    share_info = ali.get_share_info(GetShareInfoRequest(
        share_id=share_id2
    ))
    assert isinstance(share_info, GetShareInfoResponse)

    share_token = ali.get_share_token(GetShareTokenRequest(
        share_id=share_id2,
        share_pwd=share_pwd2
    ))
    assert isinstance(share_token, GetShareTokenResponse)

    share_list = ali.get_share_file_list(GetShareFileListRequest(share_id=share_id2),
                                         x_share_token=share_token.share_token)
    file_list = []
    for i in share_list:
        file_list.append(i.file_id)
        assert isinstance(i, BaseShareFile)
        share_file = ali.get_share_file(x_share_token=share_token.share_token, body=GetShareFileRequest(
            share_id=share_id2,
            file_id=i.file_id
        ))
        assert isinstance(share_file, BaseShareFile)
        url = ali.get_share_link_download_url(
            GetShareLinkDownloadUrlRequest(
                share_id=share_id2,
                file_id=i.file_id
            ),
            x_share_token=share_token.share_token
        )
        assert isinstance(url, GetShareLinkDownloadUrlResponse)
        x = ali.share_file_saveto_drive(ShareFileSaveToDriveRequest(
            share_id=share_id2,
            file_id=i.file_id,
            to_parent_file_id=share_folder
        ), x_share_token=share_token.share_token)
        assert isinstance(x, ShareFileSaveToDriveResponse)
        assert isinstance(x.file_id, str)
        assert len(x.file_id) > 10
        y = ali.move_file_to_trash(MoveFileToTrashRequest(file_id=x.file_id))
        assert isinstance(y, MoveFileToTrashResponse)

    x = ali.batch_share_file_saveto_drive(BatchShareFileSaveToDriveRequest(
        share_id=share_id2,
        file_id_list=file_list
    ), x_share_token=share_token.share_token)
    for i in x:
        assert isinstance(i, BatchSubResponse)
        assert isinstance(i.body, BatchShareFileSaveToDriveResponse)
        y = ali.move_file_to_trash(MoveFileToTrashRequest(file_id=i.body.file_id))
        assert isinstance(y, MoveFileToTrashResponse)
