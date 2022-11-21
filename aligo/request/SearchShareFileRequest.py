"""..."""
from dataclasses import dataclass

from aligo.types import DataClass


@dataclass
class SearchShareFileRequest(DataClass):
    """..."""
    share_id: str = None
    keyword: str = None
    order_by: str = None
    limit: int = 100
    marker: str = None
