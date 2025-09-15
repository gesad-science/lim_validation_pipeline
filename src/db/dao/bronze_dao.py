from typing import Type, TypeVar
from sqlalchemy.orm import Session
from src.db.models.mixins import DefaultRunMixin

T = TypeVar("T", bound=DefaultRunMixin)

class BronzeDAO:
    def __init__(self, session: Session, model: Type[T]):
        self.session = session
        self.model = model

    def add(self, record: T) -> T:
        self.session.add(record)
        self.session.commit()
        self.session.refresh(record)
        return record

    def add_many(self, records: list[T]):
        self.session.add_all(records)
        self.session.commit()

    def get_all(self) -> list[T]:
        return self.session.query(self.model).all()
