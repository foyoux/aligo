"""Other"""
from dataclasses import dataclass, field
from typing import List

from aligo.request import GetFilePathRequest
from aligo.response import GetFilePathResponse
from aligo.types.Type import DatClass
from .BaseAligo import BaseAligo
from .Config import ADRIVE_V1_FILE_GET_PATH, ADRIVE_V1_SYSTEM_CONFIG


@dataclass
class SizeConditions(DatClass):
    blacklist: List[str] = field(default_factory=list)
    field: str = None
    max_size: int = None


@dataclass
class Share(DatClass):
    album_allowed: bool = None
    create_share_file_id_list_max_size: int = None
    extension_mode: str = None
    extension_whitelist: List[str] = field(default_factory=list)
    folder_allowed: bool = None
    mime_type_whitelist: List[str] = field(default_factory=list)
    photo_collection_allowed: bool = None
    size_conditions: List[SizeConditions] = field(default_factory=list)


@dataclass
class SystemConfig(DatClass):
    restrict_registration: bool = None
    share: Share = None


class Other(BaseAligo):
    """Other"""

    def _core_get_path(self, body: GetFilePathRequest) -> GetFilePathResponse:
        """get_path 获取当前文件的路径, 父级目录"""
        response = self.post(ADRIVE_V1_FILE_GET_PATH, body=body)
        return self._result(response, GetFilePathResponse)

    def get_system_config(self) -> SystemConfig:
        response = self.post(ADRIVE_V1_SYSTEM_CONFIG)
        return self._result(response, SystemConfig)
