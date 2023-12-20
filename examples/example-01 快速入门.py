"""快速入门"""
from aligo import Aligo

if __name__ == '__main__':
    ali = Aligo()
    file_list = ali.get_file_list()
    for file in file_list:
        # 注意：print(file) 默认只显示部分信息，但是实际上file有很多的属性
        print(file.file_id, file.type, file.size, file.parent_file_id, file.name)
