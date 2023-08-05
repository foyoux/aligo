"""..."""
from dataclasses import dataclass

from aligo.types import DatClass


@dataclass
class GetDefaultDriveRequest(DatClass):
    """..."""
    user_id: str
