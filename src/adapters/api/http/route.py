from litestar import Litestar, Controller, get
# from pydantic import BaseModel
from .legal import *
from uuid import uuid1


class LegalEntityModel:
    #   (BaseModel):
    foo: str
    bar: str


class InfoController(Controller):
    path = "/info"

    @get()
    async def input(self, input: LegalEntityModel) -> str:
        return input.foo + input.bar


@get(path='/{id:uuid}')
async def id_1(user_id: uuid1) -> LegalEntity:
    pass


app = Litestar(route_handlers=[InfoController])
