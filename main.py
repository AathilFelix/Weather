#main.py

import requests as rq
import json
import city_api
import weather_api
import telegram_api
import time


while True:
    data = telegram_api.get_updates(offset=-1)
    message_text = telegram_api.get_the_message(data)
    
    if city_api.get_valid(message_text) == True:
        print(weather_api.get_weather_data(message_text))
    else:
        print("Invalid City Name/City Not enlisted in our database")