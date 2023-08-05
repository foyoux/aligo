"""..."""
from dataclasses import dataclass

from aligo.types import DatClass
from aligo.types.Enum import GetShareLinkListOrderBy, OrderDirection


@dataclass
class AlbumListRequest(DatClass):
    """..."""
    album_drive_id: str = None
    drive_id: str = None
    order_by: GetShareLinkListOrderBy = 'created_at'
    order_direction: OrderDirection = 'DESC'
