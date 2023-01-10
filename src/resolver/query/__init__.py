from ariadne import ObjectType
from resolver.query.version import version

objectType = ObjectType("Query")

# loading schema fields
objectType.set_field("version", version)
