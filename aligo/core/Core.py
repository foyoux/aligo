"""..."""
from .Audio import Audio
from .Client import Client
from .Copy import Copy
from .Create import Create
from .Drive import Drive
from .File import File
from .Move import Move
from .Download import Download
from .Recyclebin import Recyclebin
from .Search import Search
from .Share import Share
from .Star import Star
from .User import User
from .Video import Video


class Core(
    Audio,
    Copy,
    Create,
    Drive,
    File,
    Client,
    Move,
    Download,
    Recyclebin,
    Search,
    Share,
    User,
    Video,
    Star
):
    """..."""
