"""..."""
from dataclasses import dataclass, field
from typing import List

from aligo.types import DataClass


@dataclass
class BatchCancelShareRequest(DataClass):
    """..."""
    share_id_list: List[str] = field(default_factory=list)
