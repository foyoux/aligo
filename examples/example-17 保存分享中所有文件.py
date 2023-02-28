from aligo import Aligo

if __name__ == '__main__':
    ali = Aligo()
    share_id = '<填写 share_id>'
    share_token = ali.get_share_token(share_id)
    # 特别说明
    # 如果遇到分享文件非常多，此段代码运行完成后，不会立马看到所有文件，可能需要几个小时才能陆续保存完成
    # 在网页保存需要几个小时，用这个一下就可以了，阿里云服务器会处理，不用等待
    ali.share_file_save_all_to_drive(share_token)
