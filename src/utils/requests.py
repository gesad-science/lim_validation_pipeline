import pandas as pd
import requests
from src.db.dao.bronze_dao import BronzeDAO
from src.utils.conversor import convert_to_instance

def run_model_requests(dao:BronzeDAO, config: str = "treatment_mode", model:str = "llama3", table=None):
    request_url = "http://host.docker.internal:5000/new_lim/message"
    df = pd.read_csv('src/db/db_utils/dataset/final_treated_dataset.csv')
    all = dao.get_all()  
    all_messages = [record.user_msg for record in all]
    for index, rows in df.iterrows():
        message = rows['user_msg']
        if message in all_messages:
            print(f"Message already processed: {message}")
            continue
        data = {
            "message": message,
            "context": {
                "chat_id": 1,
                "config": config,
                "model": model
            }
        }
        print("Sending message:", message)
        answer = requests.post(request_url, json=data).json()
        print("Received answer:", answer)
        mixin = convert_to_instance(answer, rows, table)
        print("Adding to database:", mixin)
        dao.add(mixin)
