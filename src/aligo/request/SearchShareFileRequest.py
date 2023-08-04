"""..."""
from dataclasses import dataclass

from datclass import DatClass


@dataclass
class SearchShareFileRequest(DatClass):
    """..."""
    share_id: str = None
    keyword: str = None
    order_by: str = None
    limit: int = 100
    marker: str = None
