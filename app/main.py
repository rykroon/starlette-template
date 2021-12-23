from motor.motor_asyncio import AsyncIOMotorClient as MotorClient
import aioredis
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
