from starlette.middleware import Middleware
from starlette.middleware.authentication import AuthenticationMiddleware

from utils.authentication import BasicAuth
from middleware.redis import RedisCacheMiddleware


middleware = [
    Middleware(RedisCacheMiddleware),
    Middleware(AuthenticationMiddleware, backend=BasicAuth())
]