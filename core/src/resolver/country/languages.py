from schema.mysql import Country, Language
from db import db


def languages(obj, info):
    cursor = db.cursor()
    id_country = obj[Country.ID_COUNTRY]

    QUERY = f"SELECT "\
            f"Language.id_language, Language.name, Language.code "\
            f"FROM Country_Language "\
            f"JOIN Language using(id_language) "\
            f"WHERE id_country = {id_country}"

    cursor.execute(QUERY)
    value = cursor.fetchall()
    cursor.close()
    return value
