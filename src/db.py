import time

import mysql.connector
from mysql.connector import Error, errorcode

# Mysql Configuration
config = {
    "user": "iptv-api",
    "database": "iptv",
    "password": "iptv-api",
}

db = None

# Create mysql database ConnectionAbortedError


def create():
    """ Creates the schemas behind database """
    global db
    # Create table schemas
    cursor = db.cursor()
    with open("./database/database.sql") as f:
        schema = f.read()
    cursor.execute(schema, multi=True)

    time.sleep(1)  # Timeout to created all tables

    # loading all categories
    if not db.is_connected():
        db = mysql.connector.connect(**config)


def connect():
    """ Get connection to the database either is connected """
    global db
    if db and db.is_connected():
        return db

    """ Create database scheme """
    while True:
        try:
            db = mysql.connector.connect(**config)
            break
        except Error as err:
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
    return db


def init():
    """ Initialize the database and creates schemas """
    global db
    connect()
    create()
