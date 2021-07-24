"""..."""
from dataclasses import dataclass

from aligo.types import DataClass, PersonalRightsInfo, PersonalSpaceInfo


@dataclass
class GetPersonalInfoResponse(DataClass):
    """..."""
    personal_rights_info: PersonalRightsInfo = None
    personal_space_info: PersonalSpaceInfo = None

    # def __post_init__(self):
    #     self.personal_rights_info = _null_dict(PersonalRightsInfo, self.personal_rights_info)
    #     self.personal_space_info = _null_dict(PersonalSpaceInfo, self.personal_space_info)
