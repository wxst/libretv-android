from constants import (IPTV_DATABASE_CHANNELS,
                       IPTV_DATABASE_COUNTRIES,
                       IPTV_DATABASE_BLOCKLIST,
                       IPTV_DATABASE_CATEGORIES,
                       IPTV_DATABASE_REGIONS,
                       IPTV_DATABASE_SUBDIVISIONS,
                       IPTV_DATABASE_LANGUAGES
                       )
import pandas as pd

db_channels = pd.read_csv(IPTV_DATABASE_CHANNELS)
db_countries = pd.read_csv(IPTV_DATABASE_COUNTRIES)
db_blocklist = pd.read_csv(IPTV_DATABASE_BLOCKLIST)
db_categories = pd.read_csv(IPTV_DATABASE_CATEGORIES)
db_regions = pd.read_csv(IPTV_DATABASE_REGIONS)
db_subdivisions = pd.read_csv(IPTV_DATABASE_SUBDIVISIONS)
db_languages = pd.read_csv(IPTV_DATABASE_LANGUAGES)
