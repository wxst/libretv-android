from data import db_streams
from utils import find_value


def stream(obj, info):
    return find_value(db_streams, "tvg.id", obj["id"])
