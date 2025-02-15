import requests

endpoint = "http://localhost:8000/api/products/"

resp = requests.get(endpoint)
print(resp.json())