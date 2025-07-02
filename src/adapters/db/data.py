from dataclasses import dataclass
from datetime import date

from ...ports import ILegalEntity


@dataclass
class LegalEntityData:
    id: str
    status: int = 0
    tin: str = None
    create_date: date = None
    liquidation_date: date = None
    name: str = None
    shortname: str = None


class DataBaseAdapter(ILegalEntity):

    def __init__(self, db):
        self.db = db
        super().__init__()

    def get_info(self):
        # Просто как пример
        self.db.execute(f'select * from legal.legal_entity where id = {self.legal.id}')
        pass

    def create(self):
        #   insert or update (merge)
        pass

    def delete(self):
        # Просто как пример
        self.db.execute(f'delete from legal.legal_entity where id = {self.legal.id}')
        pass
