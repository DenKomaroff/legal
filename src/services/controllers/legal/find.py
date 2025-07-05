from litestar import Controller, get


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
