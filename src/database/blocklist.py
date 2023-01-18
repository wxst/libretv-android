from data import db_channels, db_blocklist
from db import db
from utils import find_value


def load():
    cursor = db.cursor()
    BLOCKLIST_INSERT = """
        INSERT INTO BlockList(id_blocklist,id_channel, ref) VALUES
    """
    blocklist_data = ""
    for index, serie in db_blocklist.iterrows():
        channel = find_value(db_channels, "id", serie["channel"])
        blocklist_data += f'({index+1},'\
            f'{channel["indexes"][0]+1},'\
            f'"{serie["ref"]}"),'

    blocklist = BLOCKLIST_INSERT + blocklist_data[:-1]
    cursor.execute(blocklist)
    db.commit()

    cursor.close()
