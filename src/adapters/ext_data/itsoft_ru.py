import requests


class ItSoftRu:

    _url = f'https://egrul.itsoft.ru/{{number}}.json'

    def __init__(self, number):
        rs = requests.get(self._url.format(number=number))
        result = rs.json() if rs.status_code == 200 else None
        self._info = result

    @property
    def info(self):
        return self._info

    @property
    def tin(self):
        if self._info:
            try:
                result = self._info['СвЮЛ']['@attributes']['ИНН']
            except Exception as e:
                print(e)
                result = None
            return result

    @property
    def psrn(self):
        if self._info:
            try:
                result = self._info['СвЮЛ']['@attributes']['ОГРН']
            except Exception as e:
                print(e)
                result = None
            return result
        else:
            return None

    @property
    def olf(self):
        if self._info:
            try:
                result = self._info['СвЮЛ']['@attributes']['КодОПФ']
            except Exception as e:
                print(e)
                result = None
            return result
        else:
            return None

    @property
    def shortname(self):
        if self._info:
            try:
                result = self._info['СвЮЛ']['СвНаимЮЛ']['СвНаимЮЛСокр']['@attributes']['НаимСокр']
            except Exception as e:
                print(e)
                result = None
            return result
        else:
            return None

    @property
    def fullname(self):
        if self._info:
            try:
                result = self._info['СвЮЛ']['СвНаимЮЛ']['@attributes']['НаимЮЛПолн']
            except Exception as e:
                print(e)
                result = None
            return result
        else:
            return None

    @property
    def created(self):
        if self._info:
            try:
                result = self._info['СвЮЛ']['@attributes']['ДатаОГРН']
            except Exception as e:
                print(e)
                result = None
            return result
        else:
            return None

    @property
    def liquidated(self):
        if self._info:
            try:
                result = self._info['СвЮЛ']['@attributes']['ДатаОГРН']
            except Exception as e:
                print(e)
                result = None
            return result
        else:
            return None
