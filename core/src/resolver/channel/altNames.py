from schema.mysql import Channel


def altNames(obj, info):
    value = obj[Channel.ALT_NAMES]
    if value:
        return value.split(';')
    return None
