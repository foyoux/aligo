"""..."""
from aligo import *


def test_get_personal_info():
    ali = Core()
    info = ali.get_personal_info()
    assert isinstance(info, GetPersonalInfoResponse)

    assert isinstance(ali.get_user(), BaseUser)
