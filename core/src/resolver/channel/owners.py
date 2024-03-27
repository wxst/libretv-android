from schema.mysql import Channel


def owners(obj, info):
    value = obj[Channel.OWNERS]
    if value:
        return value.split(";")
    return None
