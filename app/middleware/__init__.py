from starlette.middleware import Middleware
from starlette.middleware.authentication import AuthenticationMiddleware

from utils.authentication import BasicAuth
from .redis import RedisMiddleware


middleware = [
    Middleware(RedisMiddleware),
    Middleware(AuthenticationMiddleware, backend=BasicAuth())
]