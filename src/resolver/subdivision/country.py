from schema.mysql import Subdivision
from db import db


def country(obj, info):
    cursor = db.cursor()
    id_subdivision = obj[Subdivision.ID_SUBDIVISION]

    QUERY = f"SELECT "\
            f"Country.id_country, Country.name, Country.code, Country.flag "\
            f"FROM Subdivision_Country "\
            f"JOIN Country USING(id_country) "\
            f"where id_subdivision = {id_subdivision}"

    cursor.execute(QUERY)
    value = cursor.fetchone()
    cursor.close()
    return value
