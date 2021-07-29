"""..."""

from aligo import *

ali = Aligo()


def test_search():
    file_list = ali.search_file(
        name='png'
    )
    for file in file_list:
        assert isinstance(file, BaseFile)


