import asyncio
from hypercorn.config import Config
from hypercorn.logging import Logger as HypercornLogger
from hypercorn.asyncio import serve
from .app import app
from .logger import patch_logger

app_config = Config()
app_config.bind = '0.0.0.0:9045'


async def main():
    await serve(app, app_config)


class CustomLogger(HypercornLogger):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        if self.error_logger:
            patch_logger(self.error_logger)
        if self.access_logger:
            patch_logger(self.access_logger)


app_config.logger_class = CustomLogger


def init(name):
    if __name__ == 'services':
        # loop = asyncio.get_running_loop()
        # loop.run_until_complete(main())

        asyncio.run(serve(app, app_config), debug=True)





# if __name__ == '__main__':
#     client.loop.set_debug(True)
#     client.loop.run_until_complete(main())