import os
import random
import requests
from dotenv import load_dotenv

load_dotenv()
endpoint = "http://localhost:8000/api/products/"
auth_endpoint = "http://localhost:8000/api/auth/"

auth_response = requests.post(auth_endpoint,
    data = {
        "username" : os.environ.get("USERNAME"),
        "password": os.environ.get("PASSWORD")
    }
)
if auth_response.status_code == 200:
    token = auth_response.json()["token"]


    resp = requests.post(endpoint,
            headers = {"Authorization":f"Token {token}"},
        data = {
            "title" : "create_title",
            "price" : random.randint(0, 100) + round(random.randint(1, 99) / 100, 2)
        }
    )
    print(resp.json())