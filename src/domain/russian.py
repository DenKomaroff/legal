from .legal import LegalEntity
from ext.itsoft_ru import *


class PrimaryStateRegistrationNumber:

    def __init__(self, value: str = None):
        if value is not None:
            self._value = self.validate(value)

    def __str__(self):
        return self.value

    @property
    def value(self):
        return self._value

    @staticmethod
    def validate(number):
        err_str1 = 'ОГРН должен состоять из 13 символов'
        err_str2 = 'ОГРН должен состоять из цифр'
        number = number.strip()
        if len(number) != 13:
            raise ValueError(err_str1)
        if not number.isdigit():
            raise ValueError(err_str2)


class OrganizationalLegalForm:

    _code: int
    _name: str


class RussLegalEntity(LegalEntity):

    _olf: int                       # organizational and legal forms (ОКОПФ)

    def __init__(self, **kwargs):
        self._psrn = PrimaryStateRegistrationNumber(kwargs.get('psrn')) if kwargs.get('psrn') else None
        self.get_data_by_psrn()
        super().__init__(**kwargs)

    @property
    def psrn(self) -> str | None:
        return None if self._psrn is None else self._psrn.value

    @psrn.setter
    def psrn(self, value):
        self._psrn = PrimaryStateRegistrationNumber(value)

    def get_data_by_psrn(self):
        # select where self.psrn
        pass


    def sync(self):
        egrul(self.psrn)
        pass

