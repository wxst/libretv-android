from schema.mysql import Stream


def channelName(obj, info):
    return obj[Stream.NAME]
