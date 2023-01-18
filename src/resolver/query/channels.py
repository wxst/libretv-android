from db import db


def channels(*_, length=None, search=None, stream=False):
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

    if length:
        QUERY += f'LIMIT {length} '

    print(QUERY)
    cursor = db.cursor()
    cursor.execute(QUERY)
    values = cursor.fetchall()
    cursor.close()
    return values
