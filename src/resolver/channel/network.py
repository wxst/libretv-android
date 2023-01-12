import pandas as pd


def network(obj, info):
    value = obj["network"]
    if not pd.isnull(value):
        return value
    return None
