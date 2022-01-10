"""上传文件到指定网盘位置2"""

from aligo import Aligo

if __name__ == '__main__':
    ali = Aligo()
    # 本地目录假定 D:/迅雷下载
    # 假如你已经知道 网盘文件夹的 file_id, 比如是 61021f2e841b7566d37349d2bd5f42ec56885d68
    ali.upload_folder('D:/迅雷下载', parent_file_id='61021f2e841b7566d37349d2bd5f42ec56885d68')
    # 或者 ali.upload_folder('D:/迅雷下载', '61021f2e841b7566d37349d2bd5f42ec56885d68')
