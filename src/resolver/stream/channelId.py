import pandas as pd


def channelId(obj, info):
    value = obj["tvg.id"] 
    if value == "":
        return None

    if not pd.isnull(value):
        return value

    return None
