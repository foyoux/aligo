"""..."""

from aligo import Aligo

if __name__ == '__main__':
    ali = Aligo()
    # 获取指定文件/文件夹
    file = ali.get_file_by_path('我的资源/音乐')
    #
    local_folder = 'D:/阿里云盘'
    if file.type == 'file':
        ali.download_file(file=file, local_folder=local_folder)
    else:
        ali.download_folder(file.file_id, local_folder=local_folder)
