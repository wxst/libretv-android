from data import db_channels


def channels(*_, length):
    # Get all the channels data and pass to each field resolver
    db = db_channels.head(length)
    return db.T.to_dict().values()
