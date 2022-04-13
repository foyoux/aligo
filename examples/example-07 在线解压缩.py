"""..."""
import time

from aligo import Aligo

if __name__ == '__main__':
    ali = Aligo()
    file_id = '62563020e69d0fcc62824f3996a5381ee7bbb69f'
    x = ali.archive_uncompress(file_id)
    print(x)
    while True:
        r = ali.archive_status(file_id, x.task_id)
        print(r)
        if r.progress == 100:
            break
        time.sleep(2)
