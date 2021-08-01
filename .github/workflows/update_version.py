import os
import re

if __name__ == '__main__':
    tag: os.DirEntry
    tmp_mtime = 0
    latest_name: str = None
    for tag in os.scandir('.git/refs/tags'):
        print(f'tag {tag.name}')
        tag_stat = os.stat(tag)
        # 最近修改时间
        mtime = tag_stat.st_mtime
        if mtime > tmp_mtime:
            latest_name = tag.name
            tmp_mtime = mtime
    print(f'最新tag是: {latest_name}')
    version = latest_name[1:]
    print(f'最新version是: {version}')

    # 读取文件
    init_py = 'aligo/__init__.py'
    init = open(init_py, encoding='utf-8').read()
    new_init = re.sub('\n__version__.*\n', f"\n__version__ = '{version}'\n", init)
    open(init_py, 'w', encoding='utf-8').write(new_init)
