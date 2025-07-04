from litestar import Router
from .index import FindController, EntityController


controllers = Router(path = '', route_handlers=[FindController, EntityController])