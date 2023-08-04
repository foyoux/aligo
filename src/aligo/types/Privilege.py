"""..."""
from dataclasses import dataclass

from datclass import DatClass


@dataclass
class Privilege(DatClass):
    """..."""
    feature_id: str = None
    feature_attr_id: str = None
    quota: int = None
