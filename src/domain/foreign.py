from .legal import LegalEntity


class ForeignOrganizationCode:

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
        return number


class ForeignLegalEntity(LegalEntity):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._fcc = ForeignOrganizationCode(kwargs.get('fcc')) if kwargs.get('fcc') else None
