import random
import requests

endpoint = "http://localhost:8000/api/products/"

# Raise validation error
resp = requests.post(endpoint)
print(resp.json())

data = {
    "title" : "create_title",
    "content" : "create_content",
    "price" : random.randint(0, 100) + round(random.randint(1, 99) / 100, 2)
}
resp = requests.post(endpoint, data=data)
print(resp.json())