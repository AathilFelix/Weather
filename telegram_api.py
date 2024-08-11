# telegram api

import requests
import config

bot_token = config.bot_token
highest_update_id = None  # Store the highest update ID
last_update_id = None

url = f"https://api.telegram.org/bot{bot_token}/getUpdates"


def get_updates(offset=None, limit=None, timeout=None):
    global highest_update_id, last_update_id
    url = f"https://api.telegram.org/bot{bot_token}/getUpdates"
    payload = {"offset": offset, "limit": limit, "timeout": timeout}
    response = requests.get(url, params=payload)
    data = response.json()
    if "result" in data:
        for update in data["result"]:
            update_id = update["update_id"]
            last_update_id = update_id
            if highest_update_id is None or update_id > highest_update_id:
                highest_update_id = update_id
            elif last_update_id == update_id:
                continue
        return data


def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    response = requests.post(url, data=payload)
    if response.json()['ok'] == True:
        return True
    else:
        return False


def get_the_message(data):
    message_text = None
    if "result" in data:
        for update in data["result"]:
            message_text = update["message"]["text"]
        return message_text


def get_the_chatid(data):
    chatid = None
    if "result" in data:
        for update in data["result"]:
            chatid = update["message"]["chat"]["id"]
        return chatid

def get_the_updateid(data):
    if "result" in data:
        for updateid in data["result"]:
            id = updateid['update_id']
        return id

print(get_updates())