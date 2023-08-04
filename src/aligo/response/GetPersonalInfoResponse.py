"""..."""
from dataclasses import dataclass

from datclass import DatClass

from aligo.types import PersonalRightsInfo, PersonalSpaceInfo


@dataclass
class GetPersonalInfoResponse(DatClass):
    """..."""
    personal_rights_info: PersonalRightsInfo = None
    personal_space_info: PersonalSpaceInfo = None
