import uuid

from litestar import Controller, get, delete
from .dto import *
# from adapters import DataBaseAdapter

class EntityController(Controller):

    path = '/{entity_id:uuid}'
    return_dto = LegalEntityReadDTO

    @get()
    async def entity_info(self, entity_id:uuid.UUID) -> LegalEntityDTO:
        # DataBaseAdapter().get_info()

        #   Читаем данные из бд (по ID)
        #   Если данных нет или они могли устареть
        #       загружаем данные из внешних источников
        #   Если загруженные данные более свежие по дате внешнего источника
        #       обновляем данные в объекта в БД
        return LegalEntityDTO(uuid.uuid4(), '0000000000', '0000000000000', 'abcd', 'ABCD', None, None)

    @delete()
    async def entity_delete(self) -> None: ...
