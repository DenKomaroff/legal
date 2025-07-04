from dataclasses import dataclass
from datetime import date
from pydantic import BaseModel
from ...ports import ILegalEntity


class STaskAdd(BaseModel):
    name: str
    description: str | None = None


@dataclass
class LegalEntityData:
    id: str
    status: int = 0
    tin: str | None = None
    create_date: date | None = None
    liquidation_date: date | None = None
    name: str | None = None
    shortname: str | None = None


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
