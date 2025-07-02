from uuid import UUID
from datetime import date
from enum import Enum
from .tax import *


class Status(Enum):
    OPEN = 0
    CLOSED = 1
    LIQUIDATION = 2


class LegalEntity:

    _trrc: list                     # Tax Registration Reason Code (KPP)
    _create_date: date
    # _liquidation_date: date
    # _name: str
    # _shortname: str
    # _status: self.Status

    def __init__(self, **kwargs):
        self._id = kwargs.get('id') if kwargs.get('id') else None
        self._tin = TaxpayerIdentificationNumber(kwargs.get('tin')) if kwargs.get('tin') else None

        #   Читаем данные из бд (если есть)
        #   Если данных нет или они могли устареть
        #       загружаем данные из внешних источников
        #   Если загруженные данные более свежие по дате внешнего источника
        #       обновляем данные в объекта в БД

        # self._olf = 0
        #
        # # Код иностранной организации (КИО) ????XXXXX?
        # self._fcc = 'XXXXX' if kwargs.get('fcc') else None
        #
        # self._create_date = kwargs.get('create_date') or None
        # self._liquidation_date = kwargs.get('liquidation_date') or None
        # self._name = kwargs.get('name')
        # self._form_code = kwargs.get('form_code')
        # self._shortname = kwargs.get('shortname')
        # self._status = Status(kwargs.get('status')) or Status('OPEN')

    @property
    def id(self) -> str | None:
        return self._id

    @id.setter
    def id(self, value):
        uuid_obj = UUID(value, version=1)
        self._id = str(uuid_obj)

    @property
    def tin(self) -> str | None:
        return self._tin.value

    @tin.setter
    def tin(self, value):
        self._tin = TaxpayerIdentificationNumber(value)

    @property
    def create_date(self) -> date | None:
        return self._create_date
