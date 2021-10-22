from pymongo import MongoClient
import redis
from starlette.applications import Starlette
from starlette.config import Config

from views import routes
from utils.exception_handlers import exception_handlers
from middleware import middleware


def startup():
    ...


app = Starlette(
    debug=False,
    exception_handlers=exception_handlers,
    middleware=middleware,
    routes=routes,
    on_startup=[startup]
)

config = Config()


app.state.redis_connection_pool = redis.ConnectionPool(
    host=config('REDIS_HOST'),
    password=config('REDIS_PASSWORD', default=None)
)


app.state.mongodb_client = MongoClient(
    config('MONGODB_HOST')
)

