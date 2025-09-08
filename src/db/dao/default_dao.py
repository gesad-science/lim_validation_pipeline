from sqlalchemy.orm import Session
from src.db.models.default import DefaultDatabase

class DefaultDatabaseDAO:
    def __init__(self, session: Session):
        self.session = session

    def add(self, record: DefaultDatabase):
        self.session.add(record)
        self.session.commit()
        self.session.refresh(record)
        return record

    def add_many(self, records: list[DefaultDatabase]):
        self.session.add_all(records)
        self.session.commit()

    def get_all(self):
        return self.session.query(DefaultDatabase).all()

    def get_by_id(self, record_id):
        return self.session.query(DefaultDatabase).filter_by(id=record_id).first()

    def delete(self, record_id):
        obj = self.get_by_id(record_id)
        if obj:
            self.session.delete(obj)
            self.session.commit()
            return True
        return False
