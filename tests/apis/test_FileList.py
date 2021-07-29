"""..."""
from aligo import *

FileList_folder = '60f7d1940849a9c9924e4ce8ab90a61c4623e4aa'


def test_get_file_list():
    """..."""
    ali = Aligo()

    files = ali.get_file_list(parent_file_id=FileList_folder)

    # files = [file for file in files]
    assert len(files) == 3
    for file in files:
        assert isinstance(file, BaseFile)
    assert files[0].name == '文件夹'
    assert files[1].name.startswith('image')
    assert files[2].name.startswith('image')
