from data import db_countries
from db import db


def load():
    cursor = db.cursor()
    COUNTRY_INSERT = """
        INSERT INTO Country(id_country, name, code, flag) VALUES
    """
    country_data = ""
    for index, serie in db_countries.iterrows():
        country_data += f'({index+1},"{serie["name"]}", "{serie["code"]}",\
                        "{serie["flag"]}"),'

    country_data = country_data[:-1]
    country = COUNTRY_INSERT + country_data
    cursor.execute(country)

    db.commit()
    cursor.close()
