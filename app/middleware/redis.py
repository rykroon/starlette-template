import redis
from cachelib import RedisCache
from starlette.middleware.base import BaseHTTPMiddleware


class RedisMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request, call_next):
        request.state.redis_client = redis.Redis(
            connection_pool=request.app.state.redis_connection_pool
        )
        request.state.cache = RedisCache(request.state.redis_client)
        return await call_next(request)

