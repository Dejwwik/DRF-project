import requests

endpoint = "http://localhost:8000/api/products/5/delete/"
# Delete instance with id 1 and returns 204 (NO CONTENT)
resp = requests.delete(endpoint)
print(resp.status_code)

