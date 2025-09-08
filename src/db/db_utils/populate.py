import pandas as pd
from src.db.models.default import DefaultDatabase
from src.db.dao.default_dao import DefaultDatabaseDAO
from src.db.db import get_db

def populate_from_dataframe(df: pd.DataFrame, dao: DefaultDatabaseDAO):
    records = []
    for _, row in df.iterrows():
        record = DefaultDatabase(
            user_msg=row.get("user_msg"),
            expected_intent=row.get("expected_intent"),
            expected_class=row.get("expected_class"),
            expected_attributes=row.get("expected_attributes"),
            expected_filter_attributes=row.get("expected_filter_attributes"),
            expected_key_quantity=row.get("expected_key_quantity"),
            dataset=row.get("dataset")
        )
        records.append(record)
    dao.add_many(records)

def main():
    df = pd.read_csv('dataset/final_treated_dataset.csv')
    
    dao = DefaultDatabaseDAO(next(get_db()))
    
    populate_from_dataframe(df, dao)

if __name__ == "__main__":
    main()
