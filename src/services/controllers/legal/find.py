from litestar import Controller, get
from adapters import ExtLegalEntityInfo
import uuid
from .dto import *

class FindController(Controller):

    path = '/find'

    @get()
    # async def input(self, input: LegalEntityModel) -> str:
    async def find(self, tin: str | None = None, psrn: str | None = None) -> LegalEntityDTO:
            # dict)[str, str]:

        #   Читаем данные из бд (если есть)
        #   Если данных нет или они могли устареть
        #       загружаем данные из внешних источников
        data = ExtLegalEntityInfo(tin or psrn)
        #   Если загруженные данные более свежие по дате внешнего источника
        #       обновляем данные в объекта в БД
        if tin:
            res = str(tin)
        elif psrn:
            res = str(psrn)
        else:
            res = None
        return LegalEntityDTO(uuid.uuid4(), data.tin, data.psrn, data.shortname, data.fullname)
        # return {"find": None}
