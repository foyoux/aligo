"""
有没有按路径查看一个路径或文件存不存在的方法?

没有直接的方法，只能通过 get_file_list 遍历
"""

from aligo import Aligo

if __name__ == '__main__':
    ali = Aligo()
    file = ali.get_file_by_path('音乐/flac/example.mp3')
    if file is None:
        print('文件不存在')
    else:
        print('文件存在')
