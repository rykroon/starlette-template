import redis
from cachelib import RedisCache
from starlette.middleware.base import BaseHTTPMiddleware


class RedisCacheMiddleware(BaseHTTPMiddleware):

    def __init__(self, app, key_prefix=None, default_timeout=300):
        super().__init__(app)
        self.key_prefix = key_prefix
        self.default_timeout = default_timeout

    async def dispatch(self, request, call_next):
        request.state.redis_client = redis.Redis(
            connection_pool=request.app.state.redis_connection_pool
        )
        request.state.cache = RedisCache(
            request.state.redis_client,
            key_prefix=self.key_prefix,
            default_timeout=self.default_timeout
        )
        response = await call_next(request)
        request.state.redis_client.close()
        return response

