from schema.mysql import Channel


def id(obj, info):
    return obj[Channel.ID_CHANNEL]
