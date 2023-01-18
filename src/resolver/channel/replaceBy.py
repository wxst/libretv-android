from schema.mysql import Channel


def replaceBy(obj, info):
    return obj[Channel.REPLACED_BY]
