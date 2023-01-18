from schema.mysql import Language


def name(obj, info):
    return obj[Language.NAME]
