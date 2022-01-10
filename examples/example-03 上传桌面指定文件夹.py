"""15岁网友小猪猪提出的问题：比如上传桌面上的sb文件夹该怎么写？"""
import os
import winreg

from aligo import Aligo

if __name__ == '__main__':
    ali = Aligo()

    # 获取桌面路径
    _key = winreg.OpenKey(
        winreg.HKEY_CURRENT_USER,
        r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
    desktop = winreg.QueryValueEx(_key, "Desktop")[0]
    folder_path = os.path.join(desktop, 'sb')

    ali.upload_folder(folder_path)
