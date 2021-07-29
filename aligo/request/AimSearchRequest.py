"""..."""
from dataclasses import dataclass

from aligo.types import DataClass


@dataclass
class AimSearchRequest(DataClass):
    """..."""
    query: str
    marker: str = ''
    return_total_count: bool = True
    order_by: str = 'image_time DESC,last_access_at DESC,updated_at DESC'
    limit: int = 100
    drive_id: str = None
