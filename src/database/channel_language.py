from data import db_channels, db_languages
from db import db
from utils import find_value
import pandas as pd


def load():
    cursor = db.cursor()
    CHANNEL_LANGUAGE_INSERT = """
        INSERT INTO Channel_Language(id_channel,id_language) VALUES
    """
    channel_language_data = ""
    for index, serie in db_channels.iterrows():
        if pd.isnull(serie["languages"]):
            continue
        for language in serie["languages"].split(";"):
            channel_language = find_value(db_languages, "code", language)
            channel_language_data += f'("{index+1}",'\
                f'"{channel_language["indexes"][0]+1}"),'

    channel_language = CHANNEL_LANGUAGE_INSERT + channel_language_data[:-1]
    cursor.execute(channel_language)
    db.commit()

    cursor.close()
