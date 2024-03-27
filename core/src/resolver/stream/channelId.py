from schema.mysql import Stream


def channelId(obj, info):
    return obj[Stream.ID_CHANNEL]
