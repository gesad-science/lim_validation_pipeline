from sqlalchemy import JSON, Column, Text, Float, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from src.db.base import Base

class DefaultDatabaseMixin:
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)   
    user_msg = Column(Text)
    expected_intent = Column(Text)
    expected_class = Column(Text)
    expected_attributes = Column(JSON)
    expected_filter_attributes = Column(JSON)
    expected_key_quantity = Column(Integer)
    dataset = Column(Text)

class DefaultRunMixin(DefaultDatabaseMixin):
    processed_intent = Column(Text)
    processed_class = Column(Text)
    processed_attributes = Column(JSON)
    processed_filter_attributes = Column(JSON)
    processed_key_quantity = Column(Integer)


