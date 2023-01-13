import os


IPTV_PATH = os.path.join(os.getcwd(), "data")

IPTV_DATABASE_URL = "git@github.com:iptv-org/database.git"
IPTV_DATABASE_PATH = os.path.join(IPTV_PATH, "database")

IPTV_STREAM_URL = "git@github.com:iptv-org/iptv.git"
IPTV_STREAM_PATH = os.path.join(IPTV_PATH, "stream")

IPTV_EPG_URL = "git@github.com:iptv-org/epg.git"
IPTV_EPG_PATH = os.path.join(IPTV_PATH, "epg")

IPTV_DATABASE_CSV_PATH = os.path.join(IPTV_DATABASE_PATH, "data")
IPTV_DATABASE_CHANNELS = os.path.join(IPTV_DATABASE_CSV_PATH, "channels.csv")
IPTV_DATABASE_LANGUAGES = os.path.join(IPTV_DATABASE_CSV_PATH, "languages.csv")
IPTV_DATABASE_COUNTRIES = os.path.join(IPTV_DATABASE_CSV_PATH, "countries.csv")
IPTV_DATABASE_CATEGORIES = os.path.join(
    IPTV_DATABASE_CSV_PATH, "categories.csv")
IPTV_DATABASE_BLOCKLIST = os.path.join(IPTV_DATABASE_CSV_PATH, "blocklist.csv")
IPTV_DATABASE_REGIONS = os.path.join(IPTV_DATABASE_CSV_PATH, "regions.csv")
IPTV_DATABASE_SUBDIVISIONS = os.path.join(
    IPTV_DATABASE_CSV_PATH, "subdivisions.csv")

IPTV_STREAM_M3U = os.path.join(IPTV_STREAM_PATH, "streams")
