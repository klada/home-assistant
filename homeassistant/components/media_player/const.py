"""Provides the constants needed for component."""

ATTR_APP_ID = "app_id"
ATTR_APP_NAME = "app_name"
ATTR_GROUP_CANDIDATES = "group_candidates"
ATTR_GROUP_MEMBERS = "group_members"
ATTR_INPUT_SOURCE = "source"
ATTR_INPUT_SOURCE_LIST = "source_list"
ATTR_MEDIA_ALBUM_ARTIST = "media_album_artist"
ATTR_MEDIA_ALBUM_NAME = "media_album_name"
ATTR_MEDIA_ARTIST = "media_artist"
ATTR_MEDIA_CHANNEL = "media_channel"
ATTR_MEDIA_CONTENT_ID = "media_content_id"
ATTR_MEDIA_CONTENT_TYPE = "media_content_type"
ATTR_MEDIA_DURATION = "media_duration"
ATTR_MEDIA_ENQUEUE = "enqueue"
ATTR_MEDIA_EPISODE = "media_episode"
ATTR_MEDIA_PLAYLIST = "media_playlist"
ATTR_MEDIA_POSITION = "media_position"
ATTR_MEDIA_POSITION_UPDATED_AT = "media_position_updated_at"
ATTR_MEDIA_SEASON = "media_season"
ATTR_MEDIA_SEEK_POSITION = "seek_position"
ATTR_MEDIA_SERIES_TITLE = "media_series_title"
ATTR_MEDIA_SHUFFLE = "shuffle"
ATTR_MEDIA_TITLE = "media_title"
ATTR_MEDIA_TRACK = "media_track"
ATTR_MEDIA_VOLUME_LEVEL = "volume_level"
ATTR_MEDIA_VOLUME_MUTED = "is_volume_muted"
ATTR_SOUND_MODE = "sound_mode"
ATTR_SOUND_MODE_LIST = "sound_mode_list"

DOMAIN = "media_player"

MEDIA_TYPE_MUSIC = "music"
MEDIA_TYPE_TVSHOW = "tvshow"
MEDIA_TYPE_MOVIE = "movie"
MEDIA_TYPE_VIDEO = "video"
MEDIA_TYPE_EPISODE = "episode"
MEDIA_TYPE_CHANNEL = "channel"
MEDIA_TYPE_PLAYLIST = "playlist"
MEDIA_TYPE_IMAGE = "image"
MEDIA_TYPE_URL = "url"
MEDIA_TYPE_GAME = "game"
MEDIA_TYPE_APP = "app"

SERVICE_CLEAR_PLAYLIST = "clear_playlist"
SERVICE_JOIN = "join"
SERVICE_PLAY_MEDIA = "play_media"
SERVICE_SELECT_SOUND_MODE = "select_sound_mode"
SERVICE_SELECT_SOURCE = "select_source"
SERVICE_UNJOIN = "unjoin"

SUPPORT_PAUSE = 1
SUPPORT_SEEK = 2
SUPPORT_VOLUME_SET = 4
SUPPORT_VOLUME_MUTE = 8
SUPPORT_PREVIOUS_TRACK = 16
SUPPORT_NEXT_TRACK = 32

SUPPORT_TURN_ON = 128
SUPPORT_TURN_OFF = 256
SUPPORT_PLAY_MEDIA = 512
SUPPORT_VOLUME_STEP = 1024
SUPPORT_SELECT_SOURCE = 2048
SUPPORT_STOP = 4096
SUPPORT_CLEAR_PLAYLIST = 8192
SUPPORT_PLAY = 16384
SUPPORT_SHUFFLE_SET = 32768
SUPPORT_SELECT_SOUND_MODE = 65536
SUPPORT_BROWSE_MEDIA = 131072
SUPPORT_GROUPING = 262144
