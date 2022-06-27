from starlette.authentication import BaseUser


class Client(BaseUser):
    name: str
    secret_key: str
