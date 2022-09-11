"""..."""
from dataclasses import dataclass

from aligo.types import DataClass
from aligo.types.Enum import *


@dataclass
class AlbumListRequest(DataClass):
    """..."""
    album_drive_id: str = None
    drive_id: str = None
    order_by: GetShareLinkListOrderBy = 'created_at'
    order_direction: OrderDirection = 'DESC'
