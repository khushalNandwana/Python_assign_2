import requests
def chuck_norris_joke():
    url = "https://api.chucknorris.io/jokes/random"

    response = requests.get(url)

    if response.status_code == 200:
        joke = response.json()["value"]
        print("Chuck Norris Joke:", joke)
    else:
        print("Failed")