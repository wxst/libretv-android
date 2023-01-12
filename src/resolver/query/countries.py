from data import db_countries


def countries(*_, length):
    db = db_countries.head(length)
    return db.T.to_dict().values()
