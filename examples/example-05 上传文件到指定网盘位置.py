"""上传文件/文件夹到指定网盘目录/位置"""
from aligo import Aligo

if __name__ == '__main__':
    ali = Aligo()
    # 比如云盘目录为 /我的资源/1080p， 打头的 / 可加可不加
    remote_folder = ali.get_folder_by_path('我的资源/1080p')
    # 比如本地目录是 D:/迅雷下载
    ali.upload_folder('D:/迅雷下载', parent_file_id=remote_folder.file_id)
