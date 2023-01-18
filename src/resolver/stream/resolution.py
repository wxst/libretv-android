from schema.mysql import Stream


def resolution(obj, info):
    return obj[Stream.RESOLUTION]
