from sqlalchemy.orm import Session
from src.db.models.default_run import DefaultRun

class BronzeDAO:
    def __init__(self, session: Session, model: type[DefaultRun]):
        if not issubclass(model, DefaultRun):
            raise TypeError("O modelo precisa herdar de DefaultRun")
        self.session = session
        self.model = model

    def add(self, record: DefaultRun):
        self.session.add(record)
        self.session.commit()
        self.session.refresh(record)
        return record

    def add_many(self, records: list[DefaultRun]):
        self.session.add_all(records)
        self.session.commit()

    def get_all(self):
        return self.session.query(self.model).all()

    def get_by_id(self, record_id):
        return self.session.query(self.model).filter_by(id=record_id).first()

    def delete(self, record_id):
        obj = self.get_by_id(record_id)
        if obj:
            self.session.delete(obj)
            self.session.commit()
            return True
        return False
