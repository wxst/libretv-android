import pandas as pd


def owners(obj, info):
    value = obj["owners"]
    if not pd.isnull(value):
        return value.split(";")
    return None
