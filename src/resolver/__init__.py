import os
import importlib


from ariadne import ObjectType


# Global variables
RESOLVER_FILENAME = "resolver"
RESOLVER_PATH = os.path.join(os.getcwd(), RESOLVER_FILENAME)


resolvers = []


def get_modules(path, is_dir=False):
    """ Get modules names from a path """
    modules = []
    for dir in os.listdir(path):
        dir_path = os.path.join(path, dir)
        filename = os.path.splitext(dir)[0]

        if not filename.isalpha():
            continue

        if is_dir and os.path.isdir(dir_path):
            modules.append(dir)

        elif dir_path.endswith("py"):
            modules.append(filename)

    print(modules)
    return modules


# Resolvers automatization sets
for dir_module in get_modules(RESOLVER_PATH, is_dir=True):
    resolver_path = os.path.join(RESOLVER_PATH, dir_module)
    obj_type = ObjectType(dir_module.title())
    for resolver in get_modules(resolver_path):
        module = importlib.import_module(
            f"{RESOLVER_FILENAME}.{dir_module}.{resolver}")
        fun = module.__getattribute__(resolver)
        obj_type.set_field(resolver, fun)

    resolvers.append(obj_type)
