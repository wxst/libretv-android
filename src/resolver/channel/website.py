import pandas as pd


def website(obj, info):
    value = obj["website"]
    if not pd.isnull(value):
        return value
    return None
