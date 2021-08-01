"""..."""
from .Audio import Audio
from .Copy import Copy
from .Create import Create
from .Download import Download
from .Drive import Drive
from .File import File
from .Move import Move
from .Recyclebin import Recyclebin
from .Search import Search
from .Share import Share
from .CustomShare import CustomShare
from .Star import Star
from .Update import Update
from .Video import Video


class Aligo(
    Audio,
    Video,
    Copy,
    Create,
    Drive,
    File,
    Move,
    Download,
    Recyclebin,
    Search,
    Share,
    CustomShare,
    Star,
    Update,
):
    """..."""
