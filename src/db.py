import os

import mysql.connector
from mysql.connector import Error, errorcode

# Mysql Configuration

config = {
    "user": os.environ['DB_USER'],
    "database": os.environ['DB_NAME'],
    "password": os.environ['DB_PASSWORD'],
    "host": os.environ['DB_HOST'],
    "port": os.environ['DB_PORT'],
    "autocommit": True
}


# Create mysql database ConnectionAbortedError
def create(db):
    """ Creates the schemas behind database """
    # Create table schemas
    cursor = db.cursor()
    with open("./database/database.sql") as f:
        try:
            tables = f.read().split(';')
            for table in tables:
                if table != "" and table != "\n":
                    cursor.execute(table + ";")
        except Exception as e:
            print(e)

    cursor.close()


def connect():
    """ Get connection to the database either is connected """
    db = None
    if db and db.is_connected():
        return db

    """ Create database scheme """
    while True:
        try:
            db = mysql.connector.connect(**config)
            break
        except Error as err:
            print(err)
            if err.errno == errorcode.ER_BAD_DB_ERROR:
                db = mysql.connector.connect(
                    user=config["user"],
                    password=config["user"]
                )
                try:
                    cursor = db.cursor()
                    cursor.execute(f'USE {config["database"]}')
                    cursor.close()
                    db.close()
                except Error as err:
                    if err.errno == errorcode.ER_BAD_DB_ERROR:
                        cursor.execute(f'CREATE DATABASE {config["database"]}')
                        cursor.close()
    return db


def init():
    """ Initialize the database and creates schemas """
    db = connect()
    create(db)
    return db


db = init()
