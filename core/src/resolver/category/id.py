from schema.mysql import Category


def id(obj, info):
    return obj[Category.ID_CATEGORY]
