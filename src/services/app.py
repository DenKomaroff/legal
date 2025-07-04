from litestar import Litestar
from .controllers import controllers


app = Litestar(route_handlers=[controllers])
