from src.config import USED_MODELS, DOME_CONFIGURATIONS
from src.db.db_utils.create_dynamic_db import create_bronze_table

def iterate_model_configurations():
    for model in USED_MODELS:
        for config in DOME_CONFIGURATIONS:
            batch = f"{model}_{config}"
            create_bronze_table(tablename=batch)

if __name__ == "__main__":
    iterate_model_configurations()