import pandas as pd
from data import db_categories
from utils import find_value


def categories(obj, info):
    value = obj["categories"]
    if not pd.isnull(value):
        values = value.split(";")
        _categories = []
        for category in values:
            _categories.append(find_value(db_categories, "id", category))
        return _categories
    return None
