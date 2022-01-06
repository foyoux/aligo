"""快速入门"""
from aligo import Aligo

if __name__ == '__main__':
    ali = Aligo()
    ll = ali.get_file_list()
    for f in ll:
        print(f.file_id, f.type, f.size, f.parent_file_id, f.name)
