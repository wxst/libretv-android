from schema.mysql import Channel
from db import db


def subdivision(obj, info):
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
