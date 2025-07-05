from uuid import UUID
from datetime import date
from enum import Enum
from .tax import *


class Status(Enum):
    OPEN = 0
    CLOSED = 1
    LIQUIDATION = 2
    LIQUIDATED = 3


class LegalEntity:

    _trrc: list                     # Tax Registration Reason Code (KPP)
    _created: date
    _liquidated: date
    _name: str
    _shortname: str
    _status: Status

    def __init__(self, **kwargs):
        self._id = kwargs.get('id') if kwargs.get('id') else None
        self._tin = TaxpayerIdentificationNumber(kwargs.get('tin')) if kwargs.get('tin') else None

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
    def created(self) -> date | None:
        return self._created
