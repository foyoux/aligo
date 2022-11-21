"""导出分享中所有文件信息"""
import json
from dataclasses import asdict
from pathlib import Path

from aligo import Aligo


def tree_share(share_id, share_token, parent_file_id='root'):
    file_list = ali.get_share_file_list(share_id, share_token, parent_file_id=parent_file_id)
    for file in file_list:
        print(file.name)
        all_files.append(file)
        if file.type == 'folder':
            tree_share(share_id, share_token, file.file_id)


def to_file():
    Path('aliyun.json5').write_text(
        json.dumps([asdict(f) for f in all_files], ensure_ascii=False),
        encoding='utf8'
    )


def main():
    # 修改这里
    share_id = '<填写 share_id>'
    share_token = ali.get_share_token(share_id)
    tree_share(share_id, share_token)
    to_file()


if __name__ == '__main__':
    ali = Aligo()
    all_files = []
    main()
    print('finish ~')
