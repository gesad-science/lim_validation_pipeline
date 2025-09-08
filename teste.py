import pandas as pd
import requests

request_url = "http://127.0.0.1:8000/new_lim/message"
df = pd.read_csv('final_treated_dataset.csv')
user_messages = df['user_msg'].tolist()
awnsers = []

for message in user_messages:
    data = {
        "message": message,
        "context": {
            "chat_id": 1
        }
    }
    awnser = requests.post(request_url, json=data).json()
    awnsers.append(awnser)