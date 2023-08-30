import requests
import json
import city_api
import weather_api
import telegram_api
import time

update_id = None  # Store the update id processed
last_update_id = None
user_messaged = False
while True:
    data = telegram_api.get_updates(offset=update_id+1 if update_id else None,limit=1) #type:ignore
    message_text = telegram_api.get_the_message(data)
    user_messaged = True

    if message_text is not None and telegram_api.last_update_id != last_update_id:
        last_update_id = telegram_api.last_update_id
        if city_api.get_valid(message_text):
            weather_data = weather_api.get_weather_data(message_text)
            chat_id = telegram_api.get_the_chatid(data)
            telegram_api.send_message(chat_id, weather_data)
            last_city = message_text
            user_messaged = True
        else:
            print("Invalid City Name/City Not enlisted in our database")
    else:
        print("No Message Received")
        user_messaged = False
        
    time.sleep(5)  # Delay to avoid overwhelming the APIs and the loop
