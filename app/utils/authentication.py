import base64
from starlette.authentication import AuthenticationBackend


class SchemeAuth(AuthenticationBackend):

    scheme = None

    async def authenticate(self, request):
        auth_header = request.headers.get('Authorization')
        if auth_header is None:
            return

        scheme, _, credentials = auth_header.partition(' ')
        if scheme.lower() != self.scheme:
            return

        return self.validate_credentials(credentials)

    def validate_credentials(self, credentials):
        raise NotImplementedError


class BasicAuth(SchemeAuth):
    scheme = 'basic'

    def validate_credentials(self, credentials):
        decoded_credentials = base64.b64decode(credentials).decode()
        username, _, password = decoded_credentials.partition(':')
        return self.validate_user(username, password)

    def validate_user(self, username, password):
        raise NotImplementedError


class BearerAuth(SchemeAuth):
    scheme = 'bearer'

