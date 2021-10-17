from starlette.middleware import Middleware
from starlette.middleware.authentication import AuthenticationMiddleware
from utils.authentication import BasicAuth


middleware = [
    Middleware(AuthenticationMiddleware, backend=BasicAuth())
]

