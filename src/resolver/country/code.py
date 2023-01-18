from schema.mysql import Country


def code(obj, info):
    return obj[Country.CODE]
