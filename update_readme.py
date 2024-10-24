import pandas as pd
import os
import requests

"""
Update README.md with the 20 most recent listings.
"""

df = pd.read_csv('check_these.csv')
df['Published Date'] = pd.to_datetime(df['Published Date'])
df = df.sort_values(by='Published Date', ascending=False)

current_listings = df.head(20).copy()

try:
    previous_listings = pd.read_csv('previous_listings.csv')
except FileNotFoundError:
    previous_listings = pd.DataFrame()

if not previous_listings.empty:
    new_listings = current_listings[~current_listings['Link'].isin(previous_listings['Link'])]
else:
    new_listings = current_listings.copy()

current_listings.to_csv('previous_listings.csv', index=False)

current_listings['Location'] = current_listings['Location'].apply(
    lambda x: f"{x.split(',')[1].split('.')[0]}. {x.split(',')[-1].strip()}"
)

current_listings = current_listings.rename(columns={
    'Rent (€)': '💰 Rent (€)',
    'Size (m²)': '📏 Size (m²)',
    'Rooms': '🛏️ Rooms',
    'Location': '🏙️ District'
})

current_listings['Link'] = current_listings['Link'].apply(lambda x: f'[🔗]({x})')

current_listings = current_listings[['💰 Rent (€)', '📏 Size (m²)', '🛏️ Rooms', '🏙️ District', 'Link']]

markdown_table = current_listings.to_markdown(index=False)

with open('README.md', 'r') as readme_file:
    readme_contents = readme_file.readlines()

start_marker = "## Recent Listings\n"
start_index = (
    readme_contents.index(start_marker) + 1
    if start_marker in readme_contents
    else len(readme_contents)
)
readme_contents[start_index:] = [markdown_table + "\n"]

with open('README.md', 'w') as readme_file:
    readme_file.writelines(readme_contents)

"""
Send new listings to Telegram channel.
"""

api_token = os.getenv('BOT_API_KEY')
channel_id = os.getenv('CHANNEL_ID')

if not api_token or not channel_id:
    print("ERROR: API token or channel ID not found!")
    exit()

telegram_url = f'https://api.telegram.org/bot{api_token}/sendMessage'

for _, row in new_listings.iterrows():
    message = (
        f"**District**: {row['Location']}\n"
        f"**Rent**: {row['Rent (€)']} €\n"
        f"**Size**: {row['Size (m²)']} m²\n"
        f"**Rooms**: {row['Rooms']} rooms\n"
        f"[Link]({row['Link']})"
    )
    message_data = {
        'chat_id': channel_id,
        'text': message,
        'parse_mode': 'Markdown'
    }

    response = requests.post(telegram_url, data=message_data)

    if response.status_code != 200:
        print(f"Failed to send message for listing: {row['Link']}. Response: {response.text}")
    else:
        print(f"Message sent successfully for listing: {row['Link']}")