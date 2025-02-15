import requests

endpoint = "http://localhost:8000/api/products/1/update"


data = {
    "title" : "update_title"
}
resp = requests.patch(endpoint, data=data)
print(resp.json())