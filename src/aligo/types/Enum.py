"""字面量值"""
from typing import Optional

try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

MediaTranscodeStatus = Optional[
    # 媒体转码状态
    Literal[
        'running',  # 转码中
        'finished',  # 转码完成
        'failed',  # 转码失败
    ]
]

GetFileListOrderBy = Optional[
    # 获取文件列表排序方式
    Literal[
        'name',  # 文件名
        'created_at',  # 创建时间
        'updated_at',  # 更新时间
        'size',  # 文件大小
    ]
]

SearchFileOrderBy = Optional[
    # 搜索文件排序方式
    Literal[
        'name',  # 文件名
        'created_at',  # 创建时间
        'updated_at',  # 更新时间
        'size',  # 文件大小
    ]
]

GetFileListFields = Optional[
    # 获取文件列表字段
    Literal[
        '*',  # 全部字段
        'thumbnail',  # 缩略图
    ]
]

GetFileFields = GetFileListFields

BaseFileCategory = Optional[
    # 文件类型
    Literal[
        'others',  # 其他
        'doc',  # 文档
        'image',  # 图片
        'audio',  # 音频
        'video',  # 视频
    ]
]

OrderDirection = Optional[
    # 排序方向
    Literal[
        'ASC',  # 升序
        'DESC',  # 降序
    ]
]

BaseFileType = Optional[
    # 文件类型
    Literal[
        'file',  # 文件
        'folder',  # 文件夹
    ]
]

CheckNameMode = Optional[
    # 名称检查模式
    Literal[
        'auto_rename',  # 自动重命名
        'refuse',  # 拒绝
        'overwrite',  # 覆盖
    ]
]

BaseFileContentHashName = Optional[
    # 文件内容哈希名称
    Literal[
        'sha1'
    ]
]

BaseFileStatus = Optional[
    # 文件状态
    Literal[
        'uploading',  # 上传中
        'available',  # 可用
    ]
]

GetRecycleBinListOrderBy = Optional[
    # 获取回收站文件列表排序方式
    Literal[
        'name',  # 文件名
    ]
]

SharePolicy = Optional[
    # 分享策略
    Literal[
        'url',  # 分享链接
        'msg',  # 分享消息
    ]
]

GetShareFileListOrderBy = Optional[
    # 获取分享文件列表排序方式
    Literal[
        'name',  # 文件名
        'updated_at',  # 更新时间
    ]
]

SearchCategory = Optional[
    # 搜索类型
    Literal[
        'image',  # 图片
        'video',  # 视频
        'audio',  # 音频
        'app',  # 应用
        'doc',  # 文档
        'others',  # 其他
    ]
]

GetShareLinkListOrderBy = Optional[
    # 获取分享链接列表排序方式
    Literal[
        'share_name',  # 分享名称
        'created_at',  # 创建时间
        'description',  # 描述
        'updated_at',  # 更新时间
    ]
]

GetStarredListFields = Optional[
    # 获取收藏文件列表字段
    Literal[
        '*',  # 全部字段
        'thumbnail',  # 缩略图
    ]
]

VideoTemplateID = Optional[
    # 视频模板ID
    Literal[
        '',  # 默认模板
        'FHD',  # 全高清
        'HD',  # 高清
        'SD',  # 标清
        'LD',  # 普清
    ]
]

ArchiveType = Literal[
    "zip", "rar", "rar5", "rar4"
]

GetVideoPreviewCategory = Optional[
    # 获取视频预览类型
    Literal[
        'live_transcoding',  # 在线直播转码（m3u8）
    ]
]

# 相册文件排序方式
AlbumFileListType = Literal[
    "joined_at"
]

# 模板
TemplateType = Literal[
    1, 2, 3
]
