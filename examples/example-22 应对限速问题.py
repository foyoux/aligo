import logging
import os
import re
import subprocess
from pathlib import Path

import psutil

from aligo import Aligo, BaseFile, Null


def del_special_symbol(s: str) -> str:
    """删除Windows文件名中不允许的字符"""
    return re.sub(r'[:*?"<>|]', '_', s)


def download_by_idm(parent_file_id: str, drive_id: str = None, download_path: str = None):
    """使用 IDM 下载文件（夹）

    :param parent_file_id: 阿里云盘文件（夹）ID
    :param drive_id: drive_id, 默认 备份盘，res 为资源盘
    :param download_path: 下载路径，默认用户下载目录下 AliyunDrive 文件夹
    :return:
    """
    a = [i.exe() for i in psutil.process_iter() if i.name() == 'IDMan.exe']
    if a:
        idm: str = a[0]
    else:
        print('IDM 未运行')
        exit(1)

    if download_path is None:
        download_path = Path.home() / 'Downloads/AliyunDrive/'
    else:
        download_path = Path(download_path)

    ali = Aligo(level=logging.ERROR)

    # 处理 drive_id
    if drive_id == 'res':
        drive_id = ali.v2_user_get().resource_drive_id

    # 创建 parent_file_id 文件夹
    file_or_folder = ali.get_file(file_id=parent_file_id, drive_id=drive_id)
    if isinstance(file_or_folder, Null):
        print('获取文件失败', file_or_folder.message)
        exit(1)

    def callback(file_path: str, file: BaseFile):
        file.name = del_special_symbol(file.name)
        file_path = del_special_symbol(file_path)
        (download_path / file_path).mkdir(parents=True, exist_ok=True)
        if file.type == 'folder':
            return
        url = file.download_url or file.url
        if not url:
            dd = ali.get_download_url(file_id=file.file_id, drive_id=file.drive_id)
            if not dd.url:
                print('无法下载', file.name, file.file_id, file.drive_id, dd)
                return
            else:
                url = dd.url
        cmd = [idm, '/a', '/n', '/d', url, '/p', download_path / file_path, '/f', file.name]
        _f = download_path / file_path / file.name
        if _f.exists():
            print(f'{_f} 已存在, 跳过下载')
            return
        print(cmd)
        if os.path.exists(idm.replace('"', '')):
            subprocess.run(cmd)
            subprocess.run([idm, '/s'])

    if file_or_folder.type == 'file':
        callback('', file_or_folder)
        exit(0)

    download_path = download_path / del_special_symbol(file_or_folder.name)
    os.system('chcp 65001')
    ali.walk_files(callback, parent_file_id=parent_file_id, drive_id=drive_id)

    return 'Done!'


if __name__ == '__main__':
    download_by_idm('folder-xxx')
