"""
使用多线程下载工具可以解决限速问题，作者常用下载工具是：Internet Download Manager

对于下载单个文件，或者文件夹下的文件（不包括子目录），可以通过 get_file_list 函数获取文件列表

然后打印文件下载链接，复制（可以包含其他字符串，前后空白等，IDM 会自动提取链接）到 IDM 中，
在菜单中选择任务->从剪贴板中批量下载，然后选择下载到单独目录即可

但是对于子目录，这种方式并不适用，因为文件夹路径不同，IDM 无法自动创建子目录

这里提供一个例子，使用 IDM 命令行参数进行调用，并且会依次创建子目录
"""
import logging
import os
import re
from pathlib import Path

from aligo import Aligo, BaseFile

# 本地目录，用于存放下载的文件夹
download_path = Path.home() / 'Downloads/AliyunDrive/'

# IDM 主程序路径
idm = 'C:\\MyProgram\\IDM\\IDMan.exe'


def del_special_symbol(s: str) -> str:
    """删除Windows文件名中不允许的字符"""
    return re.sub(r'[:*?"<>|]', '_', s)


def callback(file_path: str, file: BaseFile):
    file.name = del_special_symbol(file.name)
    file_path = del_special_symbol(file_path)
    (download_path / file_path).mkdir(parents=True, exist_ok=True)
    # print(f'"{idm}" /a /n /d "{file.download_url}" /p "{download_path / file_path}" /f "{file.name}"')
    cmd = f'{idm} /a /n /d "{file.download_url or file.url}" /p "{download_path / file_path}" /f "{file.name}"'
    print(cmd)
    if os.path.exists(idm.replace('"', '')):
        os.system(cmd)
        os.system(f'{idm} /s')


def main():
    global download_path
    # noinspection SpellCheckingInspection
    os.system('chcp 65001')

    ali = Aligo(level=logging.ERROR)

    # 必须是一个文件夹
    drive_id = ali.v2_user_get().resource_drive_id
    parent_file_id = '64dcd9b5356a247012a44206a6dca0b5ab304c8e'

    # 创建 parent_file_id 文件夹
    folder = ali.get_file(file_id=parent_file_id, drive_id=drive_id)
    download_path = download_path / del_special_symbol(folder.name)

    ali.walk_files(callback, parent_file_id=parent_file_id, drive_id=drive_id)


if __name__ == '__main__':
    main()
