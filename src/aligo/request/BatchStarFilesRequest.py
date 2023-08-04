"""..."""
from dataclasses import dataclass
from typing import List

from datclass import DatClass


@dataclass
class BatchStarFilesRequest(DatClass):
    """..."""
    drive_id: str = None
    file_id_list: List[str] = None
    starred: bool = True
