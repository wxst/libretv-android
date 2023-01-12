import pandas as pd


def closed(obj, info):
    value = obj["closed"]
    if not pd.isnull(value):
        return value
    return None
