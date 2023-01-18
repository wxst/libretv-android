from data import db_countries, db_subdivisions
from db import db
from utils import find_value


def load():
    cursor = db.cursor()
    SUBDIVISION_COUNTRY_INSERT = """
        INSERT INTO Subdivision_Country(id_subdivision,id_country) VALUES
    """
    subdivision_country_data = ""
    for index, serie in db_subdivisions.iterrows():
        country = serie["country"]
        subdivision_country = find_value(db_countries, "code", country)
        if country and subdivision_country:
            subdivision_country_data += f'("{index+1}",'\
                f'"{subdivision_country["indexes"][0]+1}"),'

    subdivision_country = SUBDIVISION_COUNTRY_INSERT + \
        subdivision_country_data[:-1]
    cursor.execute(subdivision_country)
    db.commit()

    cursor.close()
