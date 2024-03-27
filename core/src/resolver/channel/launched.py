from schema.mysql import Channel


def launched(obj, info):
    return obj[Channel.LAUNCHED]
