from schema.mysql import Subdivision


def name(obj, info):
    return obj[Subdivision.NAME]
