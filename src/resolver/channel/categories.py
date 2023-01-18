from schema.mysql import Channel
from db import db


def categories(obj, info):
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
