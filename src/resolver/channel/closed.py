from schema.mysql import Channel


def closed(obj, info):
    return obj[Channel.CLOSED]
