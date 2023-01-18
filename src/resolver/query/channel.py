from data import db_channels
from utils import find_value


def channel(*_, id):
    row = find_value(db_channels, "id", id)
    return row
