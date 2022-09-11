from aligo import Aligo

share_msg1 = ('「心灵奇旅 4K 原盘 REMUX」https://www.aliyundrive.com/s/FYoddEbsSwV '
              '点击链接保存，或者复制本段内容，打开「阿里云盘」APP ，无需下载极速在线查看，视频原画倍速播放')
share_msg2 = 'https://www.aliyundrive.com/s/LkUS6BrconT/folder/62074d95b39e519f60be4f73b68ac493e9977a90'
if __name__ == '__main__':
    ali = Aligo()
    r = ali.share_link_extract_code(share_msg1)
    print(r.share_id, r.share_pwd)
    r = ali.share_link_extract_code(share_msg2)
    print(r.share_id, r.share_pwd)
