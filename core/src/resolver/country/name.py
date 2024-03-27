from schema.mysql import Country


def name(obj, info):
    return obj[Country.NAME]
