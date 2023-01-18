from data import db_channels, db_categories
from db import db
from utils import find_value
import pandas as pd


def load():
    cursor = db.cursor()
    CHANNEL_CATEGORY_INSERT = """
        INSERT INTO Channel_Category(id_channel,id_category) VALUES
    """
    channel_category_data = ""
    for index, serie in db_channels.iterrows():
        if pd.isnull(serie["categories"]):
            continue
        for category in serie["categories"].split(";"):
            channel_category = find_value(db_categories, "id", category)
            channel_category_data += f'("{index+1}",'\
                f'"{channel_category["indexes"][0]+1}"),'

    channel_category = CHANNEL_CATEGORY_INSERT + channel_category_data[:-1]
    cursor.execute(channel_category)
    db.commit()

    cursor.close()
