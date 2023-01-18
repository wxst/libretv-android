from data import (db_channels, db_countries, db_subdivisions,
                  db_languages, db_categories)
from utils import find_value
from db import db
import pandas as pd


def _null(input):
    if pd.isnull(input):
        return "NULL"
    return repr(input)


def load():
    cursor = db.cursor()
    CHANNEL_INSERT = """
        INSERT INTO Channel(
            id_channel,
            name,
            alt_names,
            network,
            owners,
            broadcast_area,
            city,
            is_nsfw,
            launched,
            closed,
            replaced_by,
            website,
            logo
        ) VALUES
    """

    channel_data = ""
    for index, serie in db_channels.iterrows():
        channel_data += f'({index+1},'\
                        f'"{serie["name"]}",'\
                        f'{_null(serie["alt_names"])},'\
                        f'{_null(serie["network"])},'\
                        f'{_null(serie["owners"])},'\
                        f'"{serie["broadcast_area"]}",'\
                        f'{_null(serie["city"])},'\
                        f'{str(serie["is_nsfw"]).upper()},'\
                        f'{_null(serie["launched"])},'\
                        f'{_null(serie["closed"])},'\
                        f'{_null(serie["replaced_by"])},'\
                        f'{_null(serie["website"])},'\
                        f'"{serie["logo"]}"),'

    channel_data = channel_data[:-1]
    language = CHANNEL_INSERT + channel_data
    cursor.execute(language)

    db.commit()
    cursor.close()
