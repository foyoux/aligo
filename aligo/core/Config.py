"""..."""
# 主机
API_HOST = 'https://api.aliyundrive.com'
AUTH_HOST = 'https://auth.aliyundrive.com'
WEBSV_HOST = 'https://websv.aliyundrive.com'
PASSPORT_HOST = 'https://passport.aliyundrive.com'

# 路径
NEWLOGIN_LOGIN_DO = '/newlogin/login.do'
NEWLOGIN_SMS_SEND_DO = '/newlogin/sms/send.do'
NEWLOGIN_SMS_LOGIN_DO = '/newlogin/sms/login.do'
NEWLOGIN_QRCODE_QUERY_DO = '/newlogin/qrcode/query.do'
NEWLOGIN_QRCODE_GENERATE_DO = '/newlogin/qrcode/generate.do'

V2_OAUTH_AUTHORIZE = '/v2/oauth/authorize'
V2_OAUTH_TOKEN_LOGIN = '/v2/oauth/token_login'

TOKEN_GET = '/token/get'
TOKEN_REFRESH = '/token/refresh'

V2_USER_GET = '/v2/user/get'

V2_DRIVE_GET = '/v2/drive/get'
V2_DRIVE_GET_DEFAULT_DRIVE = '/v2/drive/get_default_drive'

V2_FILE_GET = '/v2/file/get'
V2_FILE_LIST = '/v2/file/list'
V2_FILE_UPDATE = '/v2/file/update'
V2_FILE_MOVE = '/v2/file/move'
V2_FILE_COPY = '/v2/file/copy'
V2_FILE_SEARCH = '/v2/file/search'
V2_FILE_CREATE = '/v2/file/create'
V2_FILE_COMPLETE = '/v2/file/complete'
ADRIVE_V2_FILE_CREATE = '/adrive/v2/file/create'
V2_FILE_CREATE_WITH_PROOF = '/v2/file/create_with_proof'
ADRIVE_V2_FILE_CREATEWITHFOLDERS = '/adrive/v2/file/createWithFolders'

V2_AIMS_SEARCH = '/v2/aims/search'

V2_FILE_GET_DOWNLOAD_URL = '/v2/file/get_download_url'

V2_RECYCLEBIN_TRASH = '/v2/recyclebin/trash'
V2_RECYCLEBIN_LIST = '/v2/recyclebin/list'
V2_RECYCLEBIN_RESTORE = '/v2/recyclebin/restore'

V2_DATABOX_GET_PERSONAL_INFO = '/v2/databox/get_personal_info'
V2_DATABOX_GET_AUDIO_PLAY_INFO = '/v2/databox/get_audio_play_info'
V2_DATABOX_GET_VIDEO_PLAY_INFO = '/v2/databox/get_video_play_info'

V2_FILE_LIST_BY_CUSTOM_INDEX_KEY = '/v2/file/list_by_custom_index_key'

V2_SHARE_LINK_UPDATE = '/v2/share_link/update'
ADRIVE_V2_SHARE_LINK_LIST = '/adrive/v2/share_link/list'
ADRIVE_V2_SHARE_LINK_CREATE = '/adrive/v2/share_link/create'
ADRIVE_V2_SHARE_LINK_CANCEL = '/adrive/v2/share_link/cancel'
ADRIVE_V2_SHARE_LINK_GET_SHARE_BY_ANONYMOUS = '/adrive/v2/share_link/get_share_by_anonymous'
V2_SHARE_LINK_GET_SHARE_TOKEN = '/v2/share_link/get_share_token'
V2_FILE_GET_SHARE_LINK_DOWNLOAD_URL = '/v2/file/get_share_link_download_url'

V2_BATCH = '/v2/batch'
ADRIVE_V2_BATCH = '/adrive/v2/batch'

# 参数
CLIENT_ID = '25dzX3vbYqktVxyX'
UNI_PARAMS = {'appName': 'aliyun_drive'}
UNI_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'}
