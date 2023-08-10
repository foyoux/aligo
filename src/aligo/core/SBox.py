from dataclasses import dataclass

from aligo.core import BaseAligo
from aligo.core.Config import V2_SBOX_GET
from aligo.types.Type import DatClass


@dataclass
class SBoxResponse(DatClass):
    drive_id: str = None
    insurance_enabled: bool = None
    locked: bool = None
    pin_setup: bool = None
    recommend_vip: str = None
    sbox_real_used_size: int = None
    sbox_total_size: int = None
    sbox_used_size: int = None


class SBox(BaseAligo):

    def v2_sbox_get(self) -> SBoxResponse:
        response = self.post(V2_SBOX_GET)
        return self._result(response, SBoxResponse)
