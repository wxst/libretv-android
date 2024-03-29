from ariadne import make_executable_schema
from ariadne.asgi import GraphQL
from schema import types
from resolver import resolvers
from starlette.middleware.cors import CORSMiddleware

schema = make_executable_schema(types, resolvers)
app = CORSMiddleware(
    GraphQL(schema, debug=True),
    allow_origins=['*'],
    allow_methods=("GET", "POST", "OPTIONS", ),
    allow_headers=['access-control-allow-origin',
                   'authorization', 'content-type']
)
