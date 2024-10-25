import os
import requests
from datetime import datetime, timedelta

api_token = os.getenv('BOT_API_KEY')
channel_id = os.getenv('CHANNEL_ID')
get_chat_history_url = f'https://api.telegram.org/bot{api_token}/getChatHistory'
delete_message_url = f'https://api.telegram.org/bot{api_token}/deleteMessage'

cutoff_date = datetime.now() - timedelta(minutes=5)

def delete_recent_messages():
    response = requests.get(get_chat_history_url, params={
        'chat_id': channel_id,
        'limit': 100
    })

    if response.status_code != 200:
        return

    messages = response.json().get('result', [])
    
    for message in messages:
        message_date = datetime.fromtimestamp(message['date'])
        
        if message_date > cutoff_date:
            message_id = message['message_id']
            delete_response = requests.post(delete_message_url, data={
                'chat_id': channel_id,
                'message_id': message_id
            })

delete_recent_messages()
