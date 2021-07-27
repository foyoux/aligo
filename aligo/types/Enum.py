"""一些枚举类型"""
from typing import Optional, Literal

MediaTranscodeStatus = Optional[
    Literal['running', 'finished', 'failed']
]

GetFileListOrderBy = Optional[
    Literal['name', 'created_at', 'updated_at', 'size']
]

SearchFileOrderBy = Optional[
    Literal['name', 'created_at', 'updated_at', 'size']
]

GetFileListFields = Optional[
    Literal['*', 'thumbnail']
]

GetFileFields = GetFileListFields

BaseFileCategory = Optional[
    Literal['others', 'doc', 'image', 'audio', 'video']
]

OrderDirection = Optional[
    Literal['ASC', 'DESC']
]

BaseFileType = Optional[
    Literal['file', 'folder']
]

CheckNameMode = Optional[
    Literal['auto_rename', 'refuse']
]

BaseFileContentHashName = Optional[
    Literal['sha1']
]

BaseFileStatus = Optional[
    Literal['uploading', 'available']
]

GetRecycleBinListOrderBy = Optional[
    Literal['name']
]

SharePolicy = Optional[
    Literal['url', 'msg']
]

GetShareFileListOrderBy = Optional[
    Literal['name', 'updated_at']
]

SearchCategory = Optional[
    Literal['image', 'video', 'audio', 'app', 'doc', 'others']
]

GetShareLinkListOrderBy = Optional[
    Literal['share_name', 'created_at', 'description', 'updated_at']
]

GetStarredListFields = Optional[
    Literal['*', 'thumbnail']
]
