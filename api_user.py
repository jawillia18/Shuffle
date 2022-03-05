import requests

BASE = "http://127.0.0.1:5000"

response = requests.get(BASE + "/episode/<int:id>")
responses = requests.post(BASE + "/hello")
print(response.json())
print(responses.json())