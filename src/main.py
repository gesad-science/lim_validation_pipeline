from src.config import USED_MODELS, DOME_CONFIGURATIONS
from src.db.db_utils.create_dynamic_db import create_bronze_table
from src.dao.bronze_dao import BronzeDAO
import requests
import pandas as pd

def message_dome(message: str, configuration: str):
    request_url = "http://127.0.0.1:5000/new_lim/message"
    data = {
        "message": message,
        "context": {
            "chat_id": 1
        }
    }
    answer = requests.post(request_url, json=data).json()
    return answer

def process_dataset(dataset_path: str, configuration: str, ):
    df = pd.read_csv(dataset_path)
    messasges = df['user_msg'].tolist()
    # import dao and get all
    responses = []
    for message in messasges:
        if(message):
            response = message_dome(message, configuration)
            responses.append(response)
            # save to database
    return responses

def iterate_model_configurations():
    for model in USED_MODELS:
        for config in DOME_CONFIGURATIONS:
            batch = f"{model}_{config}"
            create_bronze_table(tablename=batch)

if __name__ == "__main__":
    iterate_model_configurations()