from aligo import Aligo

if __name__ == '__main__':
    ali = Aligo()
    r = ali.get_albums_info()
    print(r.driveId, r.driveName)
