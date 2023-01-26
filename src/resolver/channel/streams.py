from schema.mysql import Channel
from db import connect as db_connect


def streams(obj, info):
    db = db_connect()
    cursor = db.cursor()
    id_channel = obj[Channel.ID_CHANNEL]

    QUERY = f"SELECT "\
            f"Stream.id_stream, Stream.id_channel, Stream.name, "\
            f"Stream.resolution, Stream.label, Stream.url "\
            f"FROM Stream "\
            f"JOIN Channel using(id_channel) "\
            f"WHERE id_channel = {id_channel}"

    cursor.execute(QUERY)
    value = cursor.fetchall()
    cursor.close()

    if not value:
        return []

    return value
