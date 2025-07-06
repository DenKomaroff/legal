from .itsoft_ru import ItSoftRu


class ExtLegalEntityInfo:

    def __init__(self, number):

        data = ItSoftRu(number=number)

        self._tin = data.tin
        self._psrn = data.psrn
        self._shortname = data.shortname
        self._fullname = data.fullname
        self._created = data.created
        self._liquidated = data.liquidated
