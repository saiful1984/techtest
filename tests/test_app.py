import requests

BASE = "http://localhost:8000/api/v1.0/apiTasks/Saif"
response = requests.get(BASE)
print(response)
print(response.json())
