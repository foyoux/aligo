"""..."""
# 主机
API_HOST = 'https://api.aliyundrive.com'
AUTH_HOST = 'https://auth.aliyundrive.com'
WEBSV_HOST = 'https://websv.aliyundrive.com'
PASSPORT_HOST = 'https://passport.aliyundrive.com'
MEMBER_HOST = 'https://member.aliyundrive.com'

# 登录相关
NEWLOGIN_LOGIN_DO = '/newlogin/login.do'
NEWLOGIN_SMS_SEND_DO = '/newlogin/sms/send.do'
NEWLOGIN_SMS_LOGIN_DO = '/newlogin/sms/login.do'
NEWLOGIN_QRCODE_QUERY_DO = '/newlogin/qrcode/query.do'
NEWLOGIN_QRCODE_GENERATE_DO = '/newlogin/qrcode/generate.do'
V2_OAUTH_TOKEN_LOGIN = '/v2/oauth/token_login'
V2_OAUTH_AUTHORIZE = '/v2/oauth/authorize'
V2_ACCOUNT_TOKEN = '/v2/account/token'
TOKEN_REFRESH = '/token/refresh'
TOKEN_GET = '/token/get'
USERS_V1_USERS_DEVICE_RENEW_SESSION = '/users/v1/users/device/renew_session'
USERS_V1_USERS_DEVICE_LOGOUT = '/users/v1/users/device_logout'
USERS_V1_USERS_DEVICE_CREATE_SESSION = '/users/v1/users/device/create_session'
USERS_V2_USERS_DEVICE_LIST = '/users/v2/users/device_list'

# 基本信息
V2_USER_GET = '/v2/user/get'
ADRIVE_V1_USER_CONFIG_GET = '/adrive/v1/user_config/get'
V2_DRIVE_GET = '/v2/drive/get'
V2_DRIVE_GET_DEFAULT_DRIVE = '/v2/drive/get_default_drive'
V2_DRIVE_LIST_MY_DRIVES = '/v2/drive/list_my_drives'
V2_DATABOX_GET_PERSONAL_INFO = '/v2/databox/get_personal_info'
V2_DATABOX_GET_AUDIO_PLAY_INFO = '/v2/databox/get_audio_play_info'
V2_DATABOX_GET_VIDEO_PLAY_INFO = '/v2/databox/get_video_play_info'
BUSINESS_V1_USERS_VIP_INFO = '/business/v1.0/users/vip/info'
ADRIVE_V1_USER_DRIVECAPACITY_DETAILS = '/adrive/v1/user/driveCapacityDetails'

#  文件操作
V2_FILE_GET = '/v2/file/get'
V2_FILE_LIST = '/v2/file/list'
ADRIVE_V3_FILE_LIST = '/adrive/v3/file/list'
V3_FILE_UPDATE = '/v3/file/update'
V2_FILE_MOVE = '/v2/file/move'
V2_FILE_COPY = '/v2/file/copy'
V2_FILE_SEARCH = '/v2/file/search'
V2_FILE_CREATE = '/v2/file/create'
V2_FILE_COMPLETE = '/v2/file/complete'
ADRIVE_V2_FILE_CREATE = '/adrive/v2/file/create'
V2_FILE_CREATE_WITH_PROOF = '/v2/file/create_with_proof'
ADRIVE_V2_FILE_CREATEWITHFOLDERS = '/adrive/v2/file/createWithFolders'
V2_FILE_GET_UPLOAD_URL = '/v2/file/get_upload_url'
ADRIVE_V1_FILE_DUPLICATE_LIST = '/adrive/v1/file/duplicateList'
ADRIVE_V1_FILE_LISTTOCLEAN = '/adrive/v1/file/listToClean'
V2_FILE_GET_OFFICE_PREVIEW_URL = '/v2/file/get_office_preview_url'
ADRIVE_V1_FILE_GET_FOLDER_SIZE_INFO = '/adrive/v1/file/get_folder_size_info'

# 相册
ADRIVE_V1_USER_ALBUMS_INFO = '/adrive/v1/user/albums_info'
ADRIVE_V1_ALBUMHOME_ALBUMLIST = '/adrive/v1/albumHome/albumList'
ADRIVE_V1_ALBUM_DELETE = '/adrive/v1/album/delete'
ADRIVE_V1_ALBUM_GET = '/adrive/v1/album/get'
ADRIVE_V1_ALBUM_CREATE = '/adrive/v1/album/create'
ADRIVE_V1_ALBUM_LIST_FILES = '/adrive/v1/album/list_files'
ADRIVE_V1_ALBUM_UPDATE = '/adrive/v1/album/update'
ADRIVE_V1_ALBUM_ADD_FILES = '/adrive/v1/album/add_files'

V2_AIMS_SEARCH = '/v2/aims/search'

V2_FILE_GET_DOWNLOAD_URL = '/v2/file/get_download_url'

# 回收站
V2_RECYCLEBIN_TRASH = '/v2/recyclebin/trash'
V2_RECYCLEBIN_LIST = '/v2/recyclebin/list'
V2_RECYCLEBIN_RESTORE = '/v2/recyclebin/restore'

# 分享和收藏
V2_FILE_LIST_BY_CUSTOM_INDEX_KEY = '/v2/file/list_by_custom_index_key'
V2_SHARE_LINK_UPDATE = '/v2/share_link/update'
ADRIVE_V3_SHARE_LINK_LIST = '/adrive/v3/share_link/list'
ADRIVE_V2_SHARE_LINK_CREATE = '/adrive/v2/share_link/create'
ADRIVE_V2_SHARE_LINK_CANCEL = '/adrive/v2/share_link/cancel'
ADRIVE_V2_SHARE_LINK_GET_SHARE_BY_ANONYMOUS = '/adrive/v2/share_link/get_share_by_anonymous'
V2_SHARE_LINK_GET_SHARE_TOKEN = '/v2/share_link/get_share_token'
V2_FILE_GET_SHARE_LINK_DOWNLOAD_URL = '/v2/file/get_share_link_download_url'
ADRIVE_V2_SHARE_LINK_EXTRACT_CODE = '/adrive/v2/share_link/extract_code'
RECOMMEND_V1_SHARELINK_SEARCH = '/recommend/v1/shareLink/search'
ADRIVE_V2_FILE_LIST_BY_SHARE = '/adrive/v2/file/list_by_share'
ADRIVE_V2_FILE_GET_BY_SHARE = '/adrive/v2/file/get_by_share'
ADRIVE_V1_SHARE_CREATE = '/adrive/v1/share/create'

# 批量操作
V3_BATCH = '/v3/batch'
ADRIVE_V2_BATCH = '/adrive/v2/batch'

# 福利码
V1_USERS_REWARDS = '/v1/users/rewards'

# 获取路径
ADRIVE_V1_FILE_GET_PATH = '/adrive/v1/file/get_path'

# 在线解压缩相关
V2_ARCHIVE_UNCOMPRESS = '/v2/archive/uncompress'
V2_ARCHIVE_STATUS = '/v2/archive/status'

# m3u8
V2_FILE_GET_VIDEO_PREVIEW_PLAY_INFO = '/v2/file/get_video_preview_play_info'

# 模板
V2_TEMPLATE_TEST = '/v2/template/test'

# 参数
CLIENT_ID = '25dzX3vbYqktVxyX'
UNI_PARAMS = {'appName': 'aliyun_drive'}
UNI_HEADERS = {
    'Referer': 'https://aliyundrive.com',
    'User-Agent': ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                   'Chrome/91.0.4472.114 Safari/537.36'),
    # 没有此请求头，list file 获取不到 download_url 字段，url 不支持断点续传
    'x-canary': 'client=web,app=adrive,version=v4.1.0',
}
