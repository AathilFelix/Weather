# main.py

import requests as rq
import city_api
import weather_api
import telegram_api
import time


while True:
    try:
        data = telegram_api.get_updates(offset=-1, limit=1, timeout=30) # timout to reduce the stress on telegram api
        
        if data:
            chat_id = telegram_api.get_the_chatid(data)
            message_text = telegram_api.get_the_message(data)
            
            if chat_id is None or message_text is None:
                time.sleep(5)
                continue

            if city_api.get_valid(message_text) == True:
                try:
                    weather_data = weather_api.get_weather_data(message_text)
                    telegram_api.send_message(chat_id, weather_data)
                except Exception as e:
                    pass
            else:
                telegram_api.send_message(
                    chat_id, "Invalid City Name/City Not enlisted in our database"
                )
            
            time.sleep(5)

            data = telegram_api.get_updates(offset=telegram_api.highest_update_id + 1, limit=1)
            chat_id = telegram_api.get_the_chatid(data)
            message_text = telegram_api.get_the_message(data)
        else:
            print("Failed to fetch data from telegram api")
            continue
        
    except Exception as e:
        print(f"Error in main loop: {e}")
        time.sleep(5)
