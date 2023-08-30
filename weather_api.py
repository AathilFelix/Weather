#weather

import requests as rq
import json
import config
def get_weather_data(city):
    api = config.api_key

    weather = rq.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}&units=metric")
    
    data = weather.json()
    city_name = data['name']
    temp = data['main']['temp']
    humidity = data['main']['humidity']
    overall = data['weather'][0]['main']
    description = data['weather'][0]['description']
    max_temp = data['main']['temp_max']
    min_temp = data['main']['temp_min']

    output = "The weather data for {} is\n\nTemperature(Expected): {}°C\nMaximum Temperature: {}°C\nMinimum Temperature: {}°C\nHumidity: {} %\nOverall Weather: {}\nDescription: {}".format(city_name,temp,max_temp,min_temp,humidity,overall,description)
    return output