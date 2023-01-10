import os
import importlib


# Global variables
RESOLVER_FILENAME = "resolver"
RESOLVER_PATH = os.path.join(os.getcwd(), RESOLVER_FILENAME)


resolvers = []

for dir in os.listdir(RESOLVER_PATH):
    dir_path = os.path.join(RESOLVER_PATH, dir)
    if (dir.isalpha() and os.path.isdir(dir_path)):
        module = importlib.import_module(f"{RESOLVER_FILENAME}.{dir}")
        resolvers.append(module.objectType)
