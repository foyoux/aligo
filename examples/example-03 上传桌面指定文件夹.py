"""15岁网友小猪猪提出的问题：比如上传桌面上的sb文件夹该怎么写？"""
import os
import winreg
from pathlib import Path

from aligo import Aligo


def get_desktop_path():
    """获取桌面路径"""
    key = winreg.OpenKey(
        winreg.HKEY_CURRENT_USER,
        r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
    desktop = winreg.QueryValueEx(key, "Desktop")[0]
    return desktop


def get_desktop_path2():
    """获取桌面路径

    Note: 这种方式不一定对，因为有可能用户修改了默认桌面路径
    """
    return Path.home() / 'Desktop'


def main():
    """主函数"""
    ali = Aligo()
    desktop_path = get_desktop_path()
    folder_path = os.path.join(desktop_path, 'sb')
    ali.upload_folder(folder_path)


if __name__ == '__main__':
    main()
