"""测试drive"""

from aligo import *


def test_drive():
    """..."""
    ali = Aligo()

    drive = ali.get_default_drive()
    assert isinstance(drive, BaseDrive)
    drive = ali.get_drive(drive_id=drive.drive_id)
    assert isinstance(drive, BaseDrive)
