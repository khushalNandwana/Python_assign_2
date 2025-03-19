import requests

url = "https://api.chucknorris.io/jokes/random"

response = requests.get(url)

if response.status_code == 200:
    joke = response.json()
    print("Chuck Norris Joke:", joke["value"])
else:
    print("Failed")
