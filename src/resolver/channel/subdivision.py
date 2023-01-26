from schema.mysql import Channel
from db import connect as db_connect


def subdivision(obj, info):
    db = db_connect()
    id_subdivision = obj[Channel.ID_SUBDIVISION]
    if not id_subdivision:
        return None

    cursor = db.cursor()
    QUERY = f" SELECT * FROM Subdivision "\
        f"WHERE id_subdivision = {id_subdivision}"

    cursor.execute(QUERY)
    value = cursor.fetchone()
    cursor.close()
    return value
