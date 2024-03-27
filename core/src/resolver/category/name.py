from schema.mysql import Category


def name(obj, info):
    return obj[Category.NAME]
