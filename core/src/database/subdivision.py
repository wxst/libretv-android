from data import db_subdivisions
from db import db


def load():
    cursor = db.cursor()
    COUNTRY_INSERT = """
        INSERT INTO Subdivision(id_subdivision, name, code) VALUES
    """
    subdivision_data = ""
    for index, serie in db_subdivisions.iterrows():
        subdivision_data += f'({index+1},'\
                            f'"{serie["name"]}",'\
                            f'"{serie["code"]}"),'

    subdivision_data = subdivision_data[:-1]
    subdivision = COUNTRY_INSERT + subdivision_data
    cursor.execute(subdivision)

    db.commit()
    cursor.close()
