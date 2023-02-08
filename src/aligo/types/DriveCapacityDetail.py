from dataclasses import dataclass

from .DataClass import DataClass


@dataclass
class DriveCapacityDetail(DataClass):
    drive_used_size: int = None
    drive_total_size: int = None
    default_drive_used_size: int = None
    album_drive_used_size: int = None
    share_album_drive_used_size: int = None
    note_drive_used_size: int = None
    sbox_drive_used_size: int = None
