import requests

endpoint = "http://localhost:8000/api/"
resp = requests.get(endpoint)
print(resp.content)

# resp = requests.post(endpoint, data={"content":"test_content", "title":"test_title", "price":80.04})
# print(resp.content)