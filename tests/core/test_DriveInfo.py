"""测试drive"""

from aligo import *


def test_drive():
    """..."""
    ali = Core()

    drive = ali.get_default_drive()
    assert isinstance(drive, BaseDrive)
    drive = ali.get_drive(GetDriveRequest(drive_id=drive.drive_id))
    assert isinstance(drive, BaseDrive)
