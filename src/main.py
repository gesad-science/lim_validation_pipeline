from src.config import USED_MODELS, DOME_CONFIGURATIONS
from src.db.db_utils.create_dynamic_db import create_bronze_table
from src.db.dao.bronze_dao import BronzeDAO
from src.db.db import get_db
from src.utils.requests import run_model_requests

def iterate_model_configurations():
    for model in USED_MODELS:
        config="default"
        batch = f"{model}_{config}"
        print("Processing batch:", batch)
        table = create_bronze_table(tablename=batch)
        dao = BronzeDAO(session=next(get_db()), model=table)
        run_model_requests(dao, config, model, table=table)
            
if __name__ == "__main__":
    iterate_model_configurations()

