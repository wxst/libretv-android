import pandas as pd


def replaceBy(obj, info):
    value = obj["replaced_by"]
    if not pd.isnull(value):
        return value
    return None
