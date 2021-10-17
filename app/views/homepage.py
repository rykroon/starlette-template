from starlette.endpoints import HTTPEndpoint
from starlette.responses import PlainTextResponse


class Homepage(HTTPEndpoint):

    async def get(self, request):
        return PlainTextResponse('Hello World!')

