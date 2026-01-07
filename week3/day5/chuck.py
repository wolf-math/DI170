import requests

url = "https://api.chucknorris.io/jokes/random?category=career"

response = requests.get(url)
data = response.json()
print(data['value'])
