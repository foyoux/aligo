"""..."""
from dataclasses import dataclass

from aligo.types import DataClass


@dataclass
class GetShareInfoRequest(DataClass):
    """..."""
    share_id: str
