"""上传文件/文件夹到指定网盘目录/位置"""
from aligo import Aligo

if __name__ == '__main__':
    ali = Aligo()
    remote_folder = ali.get_folder_by_path('电影/1080p')
    if remote_folder is None:
        raise RuntimeError('指定的文件夹不存在')
    ali.upload_folder('D:/迅雷下载', parent_file_id=remote_folder.file_id)
