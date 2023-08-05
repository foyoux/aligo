"""..."""
from dataclasses import dataclass

from aligo.types import DatClass


@dataclass
class GetShareInfoRequest(DatClass):
    """..."""
    share_id: str
