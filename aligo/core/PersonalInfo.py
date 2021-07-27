"""..."""

from aligo.core import *
from aligo.response import *


class PersonalInfo(BaseAligo):
    """..."""

    def get_personal_info(self, f5: bool = False) -> GetPersonalInfoResponse:
        """..."""
        if self._personal_info is None or f5:
            response = self._post(V2_DATABOX_GET_PERSONAL_INFO)
            self._personal_info = self._result(response, GetPersonalInfoResponse)
        return self._personal_info
