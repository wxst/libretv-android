from schema.mysql import Stream


def label(obj, info):
    return obj[Stream.LABEL]
