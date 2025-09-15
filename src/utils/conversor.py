import pandas as pd
from src.db.models.mixins import DefaultRunMixin
def convert_to_instance(data: dict, row, table: type[DefaultRunMixin]) -> DefaultRunMixin:
    record = table()
    record.user_msg = row['user_msg']
    record.expected_intent = row['expected_intent']
    record.expected_class = row['expected_class']
    record.expected_attributes = row['expected_attributes']
    record.expected_filter_attributes = row['expected_filter_attributes']
    record.expected_key_quantity = row['expected_key_quantity']
    record.dataset = row['dataset']
    record.processed_intent = data.get('intent')
    record.processed_class = data.get('entity')
    record.processed_attributes = data.get('attributes')
    record.processed_filter_attributes = data.get('filters')
    return record