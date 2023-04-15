import requests as rq
import json
import config
def get_weather_data(city):
    api = config.api_key

    weather = rq.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}&units=metric")
    print(weather.json())