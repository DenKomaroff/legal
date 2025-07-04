from litestar import Controller, get, delete
from uuid import UUID

class LegalEntityDto:
    #   (BaseModel):
    id: UUID
    tin: str



class EntityController(Controller):

    path = '/{id:uuid}'

    @get()
    async def entity_info(self) -> dict[str, str]:

        #   Читаем данные из бд (по ID)
        #   Если данных нет или они могли устареть
        #       загружаем данные из внешних источников
        #   Если загруженные данные более свежие по дате внешнего источника
        #       обновляем данные в объекта в БД
        return {"a": "111"}

    @delete()
    async def entity_delete(self) -> None:
        pass


class FindController(Controller):

    path = '/find'

    @get()
    # async def input(self, input: LegalEntityModel) -> str:
    async def find(self, tin: str | None = None, psrn: str | None = None) -> dict[str, str]:

        #   Читаем данные из бд (если есть)
        #   Если данных нет или они могли устареть
        #       загружаем данные из внешних источников
        #   Если загруженные данные более свежие по дате внешнего источника
        #       обновляем данные в объекта в БД
        if tin:
            res = str(tin)
        elif psrn:
            res = str(psrn)
        else:
            res = None

        return {"find": res}
