from data import db_countries
from utils import find_value


def country(obj, info):
    code = obj["country"]
    return find_value(db_countries, "code", code)
