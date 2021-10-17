from starlette.applications import Starlette
from views import routes
from utils.exception_handlers import exception_handlers
from utils.middleware import middleware


def startup():
    ...

app = Starlette(
    debug=False,
    exception_handlers=exception_handlers,
    middleware=middleware,
    routes=routes,
    on_startup=[startup]
)