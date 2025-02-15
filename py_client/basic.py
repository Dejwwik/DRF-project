import requests

endpoint = "http://localhost:8000/api"
resp = requests.get(endpoint)
print(resp.content)