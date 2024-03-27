from db import connect as db_connect
from constants import DATABASE_MAX_QUERY_LENGTH


def channels(*_, length=None, search=None, stream=False, nsfw=False):
    db = db_connect()
    QUERY = "SELECT Channel.* from Channel "

    if stream:
        QUERY += "JOIN Stream using (id_channel) "

    if search:
        QUERY += f'WHERE Channel.name LIKE "%{search}%" '

    if stream:
        if search:
            QUERY += 'AND '
        else:
            QUERY += 'WHERE '

        QUERY += 'Stream.url IS NOT NULL '
    if not nsfw:
        if not stream and not search:
            QUERY += "WHERE "
        else:
            QUERY += "AND "

        QUERY += "Channel.is_nsfw = 0 "

    if length < DATABASE_MAX_QUERY_LENGTH:
        QUERY += f'LIMIT {length} '
    else:
        QUERY += f'LIMIT {DATABASE_MAX_QUERY_LENGTH} '

    cursor = db.cursor()
    cursor.execute(QUERY)
    values = cursor.fetchall()
    cursor.close()
    return values
