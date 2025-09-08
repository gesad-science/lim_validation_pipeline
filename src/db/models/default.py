from src.db.models.mixins import DefaultDatabaseMixin
from src.db.base import Base

class DefaultDatabase(Base, DefaultDatabaseMixin):
    __tablename__ = "default"