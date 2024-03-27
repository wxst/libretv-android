from schema.mysql import Channel, Language
from db import connect as db_connect


def languages(obj, info):
    db = db_connect()
    cursor = db.cursor()
    id_channel = obj[Channel.ID_CHANNEL]

    QUERY = f"SELECT "\
            f"Language.id_language, Language.name, Language.code "\
            f"FROM Channel_Language "\
            f"JOIN Language using(id_language) "\
            f"WHERE id_channel = {id_channel}"

    cursor.execute(QUERY)
    value = cursor.fetchall()
    cursor.close()
    return value
