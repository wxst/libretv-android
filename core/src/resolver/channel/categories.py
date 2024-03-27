from schema.mysql import Channel
from db import connect as db_connect


def categories(obj, info):
    db = db_connect()
    cursor = db.cursor()
    id_channel = obj[Channel.ID_CHANNEL]

    QUERY = f"SELECT "\
            f"Category.id_category, Category.name "\
            f"FROM Channel_Category "\
            f"JOIN Category using(id_category) "\
            f"WHERE id_channel = {id_channel}"

    cursor.execute(QUERY)
    value = cursor.fetchall()
    cursor.close()
    return value
