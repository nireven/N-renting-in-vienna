import requests
import os

api_token = os.getenv('BOT_API_KEY')
channel_id = os.getenv('CHANNEL_ID')
message = "Test message from bot"

telegram_url = f'https://api.telegram.org/bot{api_token}/sendMessage'

message_data = {
    'chat_id': channel_id,
    'text': message,
    'parse_mode': 'Markdown'
}

response = requests.post(telegram_url, data=message_data)

if response.status_code != 200:
    print(f"Failed to send message. Response: {response.text}")
else:
    print(f"Message sent successfully.")
