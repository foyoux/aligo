from aligo import Aligo

if __name__ == '__main__':
    ali = Aligo()
    for i in ali.list_to_clean(ali.get_albums_info().drive_id, 30):
        print(i)
