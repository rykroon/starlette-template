from starlette.middleware import Middleware
from starlette.middleware.authentication import AuthenticationMiddleware

from utils.auth.authentication import BasicAuth


middleware = [
    Middleware(AuthenticationMiddleware, backend=BasicAuth())
]
