from data import db_streams


def streams(*_, length):
    db = db_streams.head(length)
    return db.T.to_dict().values()
