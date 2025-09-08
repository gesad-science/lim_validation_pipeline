from src.db.models.mixins import DefaultRunMixin
from src.db.base import Base

def create_bronze_model(tablename: str = "database_bronze"):
    class DatabaseBronze(Base, DefaultRunMixin):
        __tablename__ = tablename

    return DatabaseBronze
