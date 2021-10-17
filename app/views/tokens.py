from starlette.authentication import requires
from starlette.endpoints import HTTPEndpoint


class Token(HTTPEndpoint):

    @requires('authenticated')
    def post(self, request):
        ...
    