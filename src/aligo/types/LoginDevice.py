"""..."""
from dataclasses import dataclass

from .DataClass import DataClass


@dataclass
class LoginDevice(DataClass):
    """..."""
    deviceId: str = None
    deviceName: str = None
    modelName: str = None
    city: str = None
    login_time: str = None
