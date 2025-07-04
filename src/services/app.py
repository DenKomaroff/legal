from litestar import Litestar
from .controllers import *


app = Litestar(route_handlers=[InfoController])
