
from utils import find_value
from data import db_languages


def languages(obj, info):
    values = obj["languages"].split(";")
    _languages = []
    for value in values:
        _languages.append(find_value(db_languages, "code", value))
    return _languages
