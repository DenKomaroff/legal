from abc import ABC

from ..domain import LegalEntity




class ILegalEntity(ABC):

    def __init__(self):
        self.legal = LegalEntity()

    def get_info(self):
        pass

    def create(self):
        pass

    def delete(self):
        pass
