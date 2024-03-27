from schema.mysql import Channel


def nsfw(obj, info):
    return obj[Channel.IS_NSFW]
