class TaxpayerIdentificationNumber:

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
        number = number.strip()
        if len(number) != 10:
            raise ValueError('ИНН должен состоять из 10 цифр')
        if not number.isdigit():
            raise ValueError('ИНН должен состоять из 10 цифр')
        k = (2, 4, 10, 3, 5, 9, 4, 6, 8)
        s = 0
        for i in range(len(number) - 1):
            s += int(number[i]) * k[i]
        s = s % 11
        if s != int(number[len(number) - 1]):
            raise ValueError('ИНН не валидный')
        # print(s)
        return number


class TaxRegistrationReasonCode:

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
        err_str1 = 'КПП должен состоять из 9 символов'
        number = number.strip()
        if len(number) != 9:
            raise ValueError(err_str1)
