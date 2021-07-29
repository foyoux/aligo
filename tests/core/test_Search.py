"""..."""

from aligo import *

ali = Core()


def test_search():
    file_list = ali.search_file(SearchFileRequest(
        query='name match "png"'
    ))
    for file in file_list:
        assert isinstance(file, BaseFile)

    aims = ali.search_aims(AimSearchRequest(
        query="keywords ='画画' and type = 'file' and category = 'image'",
    ))
    for i in aims:
        isinstance(i, BaseFile)
