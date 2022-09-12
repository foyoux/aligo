from aligo import Aligo

if __name__ == '__main__':
    ali = Aligo()

    for i in ali.get_file_list(drive_id='6333175'):
        print(i)

    # 获取相册列表
    for album in ali.list_albums():
        """
        6333175 None 3 default  # 注意，云盘中会有一个 默认的 album，无法删除
        6333175 None None starred
        iqbf34LjW2 标题。 3 manual
        k6R1nmadvf6 产品标题。 0 manual
        """
        print(album.album_id, album.name, album.total_count, album.type)

    # 创建相册
    album = ali.create_album('aligo', description='create by aligo')
    print(album.album_id)
    print(album.name)
    print(album.description)
    print(album.owner)
    print(album.created_at)
    print(album.updated_at)
    print(album.file_count)
    print(album.image_count)
    print(album.video_count)

    # 添加文件到相册
    # 可以从本地或云盘中添加
    # 从本地添加需要先上传
    # f = ali.upload_file(r"C:\Users\foyou\Pictures\Avatar\copilot-logo-large.png")  # 如果在云盘中删除此文件，相册中对应图片也会消失
    f = ali.upload_file(r"C:\Users\foyou\Pictures\Avatar\copilot-logo-large.png", drive_id=ali.album_info.driveId)
    # ali.add_files_to_album(album.album_id, [f])
    ali.add_file_to_album(album.album_id, f)
    # ali.add_file_to_album('LTeF1dwB3Wy', f)

    ll = ali.list_album_files(album.album_id)
    for i in ll:
        print(i)

    # 重命名相册
    r = ali.rename_album(album.album_id, '相册新名字')
    print(r)

    # 删除相册
    # ali.delete_album(album.album_id)
