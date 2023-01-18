from data import db_languages
from db import db


def load():
    cursor = db.cursor()
    LANGUAGE_INSERT = """
        INSERT INTO Language(id_language, name, code) VALUES
    """
    language_data = ""
    for index, serie in db_languages.iterrows():
        language_data += f'({index+1},"{serie["name"]}", "{serie["code"]}"),'

    language_data = language_data[:-1]
    language = LANGUAGE_INSERT + language_data
    cursor.execute(language)

    db.commit()
    cursor.close()
