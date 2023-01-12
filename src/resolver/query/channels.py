
from constants import (IPTV_DATABASE_CHANNELS
                       )
import pandas as pd


def channels(*_, length):
    # Get all the channels data and pass to each field resolver
    db = pd.read_csv(IPTV_DATABASE_CHANNELS).head(length)
    return db.T.to_dict().values()
