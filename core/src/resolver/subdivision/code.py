from schema.mysql import Subdivision


def code(obj, info):
    return obj[Subdivision.CODE]
