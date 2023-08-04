"""..."""
from dataclasses import dataclass

from datclass import DatClass


@dataclass
class GetShareInfoRequest(DatClass):
    """..."""
    share_id: str
