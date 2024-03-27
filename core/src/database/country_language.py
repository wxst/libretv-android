from data import db_countries, db_languages
from db import db
from utils import find_value


def load():
    cursor = db.cursor()
    COUNTRY_LANGUAGE_INSERT = """
        INSERT INTO Country_Language(id_country,id_language) VALUES
    """
    country_data = ""
    for index, serie in db_countries.iterrows():
        for language in serie["languages"].split(";"):
            country_language = find_value(db_languages, "code", language)
            country_data += f'("{index+1}",'\
                f'"{country_language["indexes"][0]+1}"),'

    country_language = COUNTRY_LANGUAGE_INSERT + country_data[:-1]
    cursor.execute(country_language)
    db.commit()

    cursor.close()
