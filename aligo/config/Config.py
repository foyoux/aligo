"""..."""
from typing import Literal, Optional

# 主机
WEBSV_HOST = 'https://websv.aliyundrive.com'
API_HOST = 'https://api.aliyundrive.com'
AUTH_HOST = 'https://auth.aliyundrive.com'
PASSPORT_HOST = 'https://passport.aliyundrive.com'

# 路径
V2_OAUTH_AUTHORIZE = '/v2/oauth/authorize'
NEWLOGIN_LOGIN_DO = '/newlogin/login.do'
NEWLOGIN_SMS_SEND_DO = '/newlogin/sms/send.do'
NEWLOGIN_SMS_LOGIN_DO = '/newlogin/sms/login.do'
NEWLOGIN_QRCODE_GENERATE_DO = '/newlogin/qrcode/generate.do'
NEWLOGIN_QRCODE_QUERY_DO = '/newlogin/qrcode/query.do'
V2_OAUTH_TOKEN_LOGIN = '/v2/oauth/token_login'
TOKEN_GET = '/token/get'
TOKEN_REFRESH = '/token/refresh'
V2_USER_GET = '/v2/user/get'
V2_DATABOX_GET_PERSONAL_INFO = '/v2/databox/get_personal_info'
V2_DATABOX_GET_AUDIO_PLAY_INFO = '/v2/databox/get_audio_play_info'
V2_FILE_GET = '/v2/file/get'
V2_FILE_GET_DOWNLOAD_URL = '/v2/file/get_download_url'
V2_DATABOX_GET_VIDEO_PLAY_INFO = '/v2/databox/get_video_play_info'
V2_FILE_LIST = '/v2/file/list'
V2_DRIVE_GET_DEFAULT_DRIVE = '/v2/drive/get_default_drive'
V2_DRIVE_GET = '/v2/drive/get'
V2_FILE_CREATE = '/v2/file/create'
V2_FILE_COMPLETE = '/v2/file/complete'
V2_RECYCLEBIN_TRASH = '/v2/recyclebin/trash'
V2_RECYCLEBIN_LIST = '/v2/recyclebin/list'
V2_RECYCLEBIN_RESTORE = '/v2/recyclebin/restore'
V2_FILE_SEARCH = '/v2/file/search'
V2_FILE_UPDATE = '/v2/file/update'
V2_FILE_MOVE = '/v2/file/move'
V2_FILE_COPY = '/v2/file/copy'
V2_FILE_CREATE_WITH_PROOF = '/v2/file/create_with_proof'
ADRIVE_V2_FILE_CREATE = '/adrive/v2/file/create'
ADRIVE_V2_FILE_CREATEWITHFOLDERS = '/adrive/v2/file/createWithFolders'

ADRIVE_V2_SHARE_LINK_CREATE = '/adrive/v2/share_link/create'
ADRIVE_V2_SHARE_LINK_CANCEL = '/adrive/v2/share_link/cancel'
ADRIVE_V2_SHARE_LINK_LIST = '/adrive/v2/share_link/list'
ADRIVE_V2_BATCH = '/adrive/v2/batch'
V2_SHARE_LINK_UPDATE = '/v2/share_link/update'
# 参数
# USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) ????/2.1.1 Chrome/89.0.4389.82 Electron/12.0.1 Safari/537.36'
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
UNI_PARAMS = {'appName': 'aliyun_drive'}
UNI_HEADERS = {'User-Agent': USER_AGENT}
CLIENT_ID = '25dzX3vbYqktVxyX'

# Enum / Type


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
