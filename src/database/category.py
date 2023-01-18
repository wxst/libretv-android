from db import db
from data import db_categories
import time


def load():
    """ Load to database Category table """
    cursor = db.cursor()
    CATEGORY_INSERT = """
    INSERT INTO Category(id_category, name) VALUES
    """
    category_data = ""
    for index, serie in db_categories.iterrows():
        category_data += f'({index+1}, "{serie["name"]}"),'

    # Delete the last comma
    category_data = category_data[:-1]

    category = CATEGORY_INSERT + category_data
    cursor.execute(category)
    db.commit()

    time.sleep(1)
    cursor.close()
