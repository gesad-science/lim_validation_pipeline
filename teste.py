import pandas as pd
import requests
from src.db.dao.bronze_dao import BronzeDAO

def run_model_requests(config: str, dao:BronzeDAO):
    request_url = "http://127.0.0.1:5000/new_lim/message"
    df = pd.read_csv('src/db/db_utils/dataset/final_treated_dataset.csv')
    user_messages = df['user_msg'].tolist()
    awnsers = []

    for message in user_messages:
        data = {
            "message": message,
            "context": {
                "chat_id": 1,
                "config": "treatment_mode",
                "model": "llama3"
            }
        }
        awnser = requests.post(request_url, json=data).json()
        print(message)
        print(awnser)
        awnsers.append(awnser)

run_model_requests("treatment_mode")