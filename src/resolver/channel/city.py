import pandas as pd


def city(obj, info):
    value = obj["city"]
    if not pd.isnull(value):
        return value
    return None
