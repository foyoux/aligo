"""..."""
from aligo import *


def test_LatestClient():
    """..."""
    ali = AligoCore()

    win = ali.get_latest_win32_client()

    assert isinstance(win, ClientInfo)

