from schema.mysql import Channel
from db import db


def country(obj, info):
    cursor = db.cursor()
    id_channel = obj[Channel.ID_CHANNEL]

    QUERY = f"SELECT "\
            f"Country.id_country, Country.name, Country.code,"\
            f"Country.flag "\
            f"FROM Country "\
            f"JOIN Channel using(id_country) "\
            f"WHERE id_channel = {id_channel}"

    cursor.execute(QUERY)
    value = cursor.fetchone()
    cursor.close()
    return value
