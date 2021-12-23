from beanie import Document
from starlette.authentication import BaseUser


class Client(Document, BaseUser):
    name: str
    secret_key: str

    class Collection:
        name = 'clients'
