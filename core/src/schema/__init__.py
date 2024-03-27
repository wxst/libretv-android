import os
from ariadne import gql

SCHEMA_PATH = os.path.join(os.getcwd(), "schema")
SCHEMA_EXT = "gql"

type_defs = ""


paths = []

for file in os.listdir(SCHEMA_PATH):
    if (file.endswith(SCHEMA_EXT)):
        paths.append(os.path.splitext(file)[0])


for path in paths:
    path = os.path.join(SCHEMA_PATH, f"{path}.{SCHEMA_EXT}")
    with open(path) as file:
        type_defs += f"\n{file.read()}"


types = gql(type_defs)
