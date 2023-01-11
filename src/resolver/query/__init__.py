from ariadne import ObjectType
from resolver.query.version import version

query = ObjectType("Query")

# loading schema fields
query.set_field("version", version)
