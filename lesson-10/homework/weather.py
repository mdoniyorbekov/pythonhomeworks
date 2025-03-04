import requests  

API_KEY = "116338b7691496b657eeaa8989857a02"
CITY = "Rome"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

params = {
    "q": CITY,
    "appid": API_KEY,
    "units": "metric"
}

response = requests.get(BASE_URL, params=params)

if response.status_code == 200:
    data = response.json()

    
    temperature = data["main"]["temp"]  
    humidity = data["main"]["humidity"]  
    weather_description = data["weather"][0]["description"]

    print(f"Weather in {CITY}:")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Condition: {weather_description.capitalize()}") 

else:
    print("Oops! Couldn't fetch weather data.")
    print("Check if the city name is correct or if your API key is valid.")