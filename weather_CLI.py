import requests

def get_coordinates(city):
    
    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
    geo_response = requests.get(geo_url)

    if geo_response.status_code == 200 and geo_response.json().get("results"):
        location = geo_response.json()["results"][0]
        return location["latitude"], location["longitude"]
    else:
        print("City not found.")
        return None, None

def get_weather(city):
    
    latitude, longitude = get_coordinates(city)
    
    if latitude and longitude:
        weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
        weather_response = requests.get(weather_url)

        if weather_response.status_code == 200:
            weather = weather_response.json()["current_weather"]
            print(f"\nWeather in {city}:")
            print(f"Temperature: {weather['temperature']}°C")
            print(f"Wind Speed: {weather['windspeed']} km/h")
            print(f"Condition Code: {weather['weathercode']}\n")
        else:
            print("Failed to collect data.")
    else:
        print("location not determine.")

if __name__ == "__main__":
    city = input("Enter your city: ")
    get_weather(city)