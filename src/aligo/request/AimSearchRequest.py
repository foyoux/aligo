"""..."""
from dataclasses import dataclass

from aligo.types import DatClass


@dataclass
class AimSearchRequest(DatClass):
    """..."""
    query: str
    marker: str = ''
    return_total_count: bool = True
    order_by: str = 'image_time DESC,last_access_at DESC,updated_at DESC'
    limit: int = 100
    drive_id: str = None
