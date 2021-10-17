from starlette.routing import Route
from views.homepage import Homepage
from views.tokens import Token

routes = [
    Route('/', Homepage),
    Route('/tokens', Token)
]