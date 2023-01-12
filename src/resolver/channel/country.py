from data import db_countries


def country(obj, info):
    code = obj["country"]
    # Find the item in the df
    db = db_countries.loc[db_countries["code"] == code]
    # Because to_dict return a dict_values cast to list and get the values
    db = list(db.T.to_dict().values())[0]
    return db
