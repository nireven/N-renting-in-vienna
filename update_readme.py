import pandas as pd
import os
import requests
import re
from urllib.parse import quote

"""
Update README.md with the 20 most recent listings.
"""

df = pd.read_csv('check_these.csv')
df['Published Date'] = pd.to_datetime(df['Published Date'])
df = df.sort_values(by='Published Date', ascending=False)

recent_listings = df.head(20)
recent_listings = recent_listings[['Rent (€)', 'Size (m²)', 'Rooms', 'Location', 'Link']]

recent_listings['Location'] = recent_listings['Location'].apply(
    lambda x: f"{x.split(',')[1].split('.')[0]}. {x.split(',')[-1].strip()}"
)

# Encode URLs to handle special characters like '|'
recent_listings['Link'] = recent_listings['Link'].apply(lambda x: quote(x, safe='/:?=&%'))

current_listings = recent_listings.rename(columns={
    'Rent (€)': '💰 Rent (€)',
    'Size (m²)': '📏 Size (m²)',
    'Rooms': '🛏️ Rooms',
    'Location': '🏙️ District'
})

current_listings['Link'] = current_listings['Link'].apply(lambda x: f'[🔗]({x})')

# Read old README.md and extract old links
try:
    with open('README.md', 'r') as readme_file:
        readme_contents = readme_file.read()
    old_links = re.findall(r'\[🔗\]\((.*?)\)', readme_contents)
except FileNotFoundError:
    old_links = []

# Update README.md
markdown_table = current_listings.to_markdown(index=False)

with open('README.md', 'r') as readme_file:
    readme_contents = readme_file.read()

start_marker = "## Recent Listings\n"
if start_marker in readme_contents:
    before_table = readme_contents.split(start_marker)[0] + start_marker
else:
    before_table = readme_contents + "\n" + start_marker

with open('README.md', 'w') as readme_file:
    readme_file.write(before_table + "\n" + markdown_table + "\n")

"""
Send new listings to Telegram channel.
"""

# Extract current encoded links
current_links = recent_listings['Link'].tolist()

# Identify new listings
new_links = [link for link in current_links if link not in old_links]

new_listings = recent_listings[recent_listings['Link'].isin(new_links)]

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
