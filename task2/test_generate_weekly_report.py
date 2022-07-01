import requests

BASE = "http://127.0.0.1:5002/"

response = requests.get(BASE + "generate_weekly_report")
print(response.json())
