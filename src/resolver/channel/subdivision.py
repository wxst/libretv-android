from data import db_subdivisions
from utils import find_value
import pandas as pd


def subdivision(obj, info):
    code = obj["subdivision"]
    if not pd.isnull(code):
        return find_value(db_subdivisions, "code", code)
    return None
