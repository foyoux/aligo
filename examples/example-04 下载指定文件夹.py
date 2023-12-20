from aligo import Aligo


def main():
    ali = Aligo()
    file = ali.get_folder_by_path('计算机/Python')
    if file is None:
        raise RuntimeError('指定的文件夹不存在')
    local_folder = 'D:\\阿里云盘'
    ali.download_folder(folder_file_id=file.file_id, local_folder=local_folder)


if __name__ == '__main__':
    main()
