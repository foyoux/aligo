"""..."""
from .Album import Album
from .Audio import Audio
from .Compress import Compress
from .Copy import Copy
from .Create import Create
from .Download import Download
from .Drive import Drive
from .Duplicate import Duplicate
from .File import File
from .Move import Move
from .Other import Other
from .Recyclebin import Recyclebin
from .SBox import SBox
from .Search import Search
from .Share import Share
from .Star import Star
from .User import User
from .Video import Video


class Core(
    Album,
    Audio,
    Compress,
    Copy,
    Create,
    Download,
    Drive,
    Duplicate,
    File,
    Move,
    Other,
    Recyclebin,
    SBox,
    Search,
    Share,
    Star,
    User,
    Video,
):
    """..."""
