"""..."""
from dataclasses import dataclass

from aligo.types import DataClass, PersonalRightsInfo, PersonalSpaceInfo


@dataclass
class GetPersonalInfoResponse(DataClass):
    """..."""
    personal_rights_info: PersonalRightsInfo = None
    personal_space_info: PersonalSpaceInfo = None
