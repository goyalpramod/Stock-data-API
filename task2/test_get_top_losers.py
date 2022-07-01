import requests


BASE = "http://127.0.0.1:5002/"

response = requests.get(BASE + "get_top_losers") #get becuase that is the name of the function
print(response.json())
