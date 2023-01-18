from db import db


def channels(*_, length):
    cursor = db.cursor()
    QUERY = f"SELECT * from Channel LIMIT {length}"
    cursor.execute(QUERY)
    values = cursor.fetchall()
    cursor.close()
    return values
