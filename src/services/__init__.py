import asyncio
from hypercorn.config import Config
from hypercorn.asyncio import serve
from .app import app


app_config = Config()
app_config.bind = '0.0.0.0:9045'
app_config.debug = True
app_config.loglevel = 'DEBUG'


def init(name):
    if __name__ == 'services':
        asyncio.run(serve(app, app_config))
