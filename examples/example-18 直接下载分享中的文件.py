"""
截止 2022年12月06日 12时04分57秒 aligo 中没有提供直接下载分享中文件夹的方法，后期会考虑加上
"""
from aligo import Aligo

if __name__ == '__main__':
    ali = Aligo()
    share_token = ali.get_share_token('<share_id>')
    file_list = ali.get_share_file_list(share_token)
    tmp = ali.get_share_link_download_url('<分享中某个文件的 file_id>', share_token)
    ali.download_file(file_path='xxx', url=tmp.download_url or file.url)
