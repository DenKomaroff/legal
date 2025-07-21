from itsoft import ItSoftRu


class ExtLegalEntityInfo:

    def __init__(self, number):

        data = ItSoftRu(number=number)

        self._tin = data.tin
        self._psrn = data.psrn
        self._shortname = data.shortname
        self._fullname = data.fullname
        self._created = data.created
        self._liquidated = data.liquidated
        self._json = data.info

    @property
    def tin(self):
        return self._tin
    @property
    def psrn(self):
        return self._psrn
    @property
    def shortname(self):
        return self._shortname
    @property
    def fullname(self):
        return self._fullname
    @property
    def created(self):
        return self._created
    @property
    def liquidated(self):
        return self._liquidated