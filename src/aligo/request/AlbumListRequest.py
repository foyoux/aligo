"""..."""
from dataclasses import dataclass

from datclass import DatClass

from aligo.types.Enum import *


@dataclass
class AlbumListRequest(DatClass):
    """..."""
    album_drive_id: str = None
    drive_id: str = None
    order_by: GetShareLinkListOrderBy = 'created_at'
    order_direction: OrderDirection = 'DESC'
