from db import db
if __name__ == "__main__":
    cursor = db.cursor()
    cursor.execute('SHOW TABLES')
    print(cursor.fetchall())
    cursor.close()
