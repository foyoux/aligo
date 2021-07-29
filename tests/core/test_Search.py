"""..."""

from aligo import *

ali = Core()


def test_search():
    file_list = ali.search_file(SearchFileRequest(
        query='name match "png"'
    ))
    for file in file_list:
        assert isinstance(file, BaseFile)


def xxx():
    file_list = ali.search_file(SearchFileRequest(
        query='name match "png"'
    ))
    i = 1
    for file in file_list:
        assert isinstance(file, BaseFile)
        print('%04d. ' % i, file.name)
        i += 1
