from aligo import Aligo

if __name__ == '__main__':
    ali = Aligo()
    # ali.share_file_by_aligo()
    # ali.share_files_by_aligo()

    # 返回包含 folder 中所有文件的下载信息 和 folder 的目录结构
    # 因为下载连接信息有效期之后4个小时，所以此自定义分享数据的有效期也只有4个小时
    data = ali.share_folder_by_aligo('<folder file_id>')

    # 其他用户拿到 data 之后，同样使用 aligo 进行保存
    # 默认保存到云盘根目录，可选设置 parent_file_id 参数来改变保存的位置
    # ali.save_files_by_aligo(data)
