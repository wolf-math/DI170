import requests

response = requests.get("http://api.open-notify.org/astros.json")
data = response.text
print(response.request.url)
print(response.request.body)
print(data)