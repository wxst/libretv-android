import os


IPTV_PATH = os.path.join(os.getcwd(), "data")

IPTV_DATABASE_URL = "git@github.com:iptv-org/database.git"
IPTV_DATABASE_PATH = os.path.join(IPTV_PATH, "database")

IPTV_STREAM_URL = "git@github.com:iptv-org/iptv.git"
IPTV_STREAM_PATH = os.path.join(IPTV_PATH, "stream")

IPTV_EPG_URL = "git@github.com:iptv-org/epg.git"
IPTV_EPG_PATH = os.path.join(IPTV_PATH, "epg")
