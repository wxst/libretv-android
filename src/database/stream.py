from data import db_channels, db_streams
from db import db
from utils import find_value
import pandas as pd
import re


def parse_name(item):
    resolution_pattern = re.compile(r"\(([0-9)]+p)\)")
    label_pattern = re.compile(r"\[[A-Za-z\-/0-9 ]+\]")
    resolution = resolution_pattern.findall(item)
    label = label_pattern.findall(item)
    name = item

    if resolution:
        resolution = resolution[0]
        name = name.replace(f"({resolution})", "")
        resolution = repr(resolution.strip())
    else:
        resolution = "NULL"

    if label:
        label = label[0]
        name = name.replace(f"{label}", "")
        label = repr(label[1:-1].strip())
    else:
        label = "NULL"

    name = repr(name.strip())
    return (name, resolution, label)


def load():
    cursor = db.cursor()
    STREAM_INSERT = """
        INSERT INTO Stream(
                id_stream,
                id_channel,
                name,
                resolution,
                label,
                url
                ) VALUES
    """
    stream_data = ""
    for index, serie in db_streams.iterrows():
        channel = find_value(db_channels, "id", serie["tvg.id"])

        if pd.isnull(channel):
            continue

        (name, resolution, label) = parse_name(serie["name"])

        stream_data +=\
            f'(NULL,'\
            f'{channel["indexes"][0]+1},'\
            f'{name},'\
            f'{resolution},'\
            f'{label},'\
            f'"{serie["url"]}"),'

    stream = STREAM_INSERT + stream_data[:-1]

    cursor.execute(stream)
    db.commit()

    cursor.close()
