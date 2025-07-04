from litestar import Controller, get


class LegalEntityModel:
    #   (BaseModel):
    foo: str
    bar: str


class InfoController(Controller):

    path = '/{id:uuid}'

    @get()
    # async def input(self, input: LegalEntityModel) -> str:
    async def info(self) -> str:

        #   Читаем данные из бд (если есть)
        #   Если данных нет или они могли устареть
        #       загружаем данные из внешних источников
        #   Если загруженные данные более свежие по дате внешнего источника
        #       обновляем данные в объекта в БД

        return '{"a": "111"}'
