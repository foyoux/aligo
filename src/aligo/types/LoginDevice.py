"""..."""
from dataclasses import dataclass

from .Type import DatClass


@dataclass
class LoginDevice(DatClass):
    """..."""
    deviceId: str = None
    deviceName: str = None
    modelName: str = None
    city: str = None
    login_time: str = None
