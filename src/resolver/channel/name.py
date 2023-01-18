from schema.mysql import Channel


def name(obj, info):
    return obj[Channel.NAME]
