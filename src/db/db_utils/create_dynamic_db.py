from src.db.base import Base
from src.db.db import engine
from src.db.models.dynamic_table import create_bronze_model

def create_bronze_table(tablename: str):

    BronzeModel = create_bronze_model(tablename)

    Base.metadata.create_all(bind=engine, tables=[BronzeModel.__table__])

    return BronzeModel
