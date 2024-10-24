import pandas as pd
import os
import requests

"""
Update README.md with the 20 most recent listings.
"""

df = pd.read_csv('check_these.csv')
df['Published Date'] = pd.to_datetime(df['Published Date'])
df = df.sort_values(by='Published Date', ascending=False)

recent_listings = df.head(20)
recent_listings = recent_listings[['Rent (€)', 'Size (m²)', 'Rooms', 'Location', 'Link']]

recent_listings['Location'] = recent_listings['Location'].apply(lambda x: f"{x.split(',')[1].split('.')[0]}. {x.split(',')[-1].strip()}")

recent_listings = recent_listings.rename(columns={'Rent (€)': '💰 Rent (€)', 'Size (m²)': '📏 Size (m²)', 'Rooms': '🛏️ Rooms', 'Location': '🏙️ District'})

# Keep the Markdown link for the README
recent_listings['Link'] = recent_listings['Link'].apply(lambda x: f'[🔗]({x})')

current_listings = recent_listings.copy()

try:
    previous_listings = pd.read_csv('previous_listings.csv')
except FileNotFoundError:
    previous_listings = pd.DataFrame()

recent_listings.to_csv('previous_listings.csv', index=False)

new_listings = pd.concat([current_listings, previous_listings]).drop_duplicates(keep=False) if not previous_listings.empty else current_listings

if not new_listings.empty:
    markdown_table = current_listings.to_markdown(index=False)

    with open('README.md', 'r') as readme_file:
        readme_contents = readme_file.readlines()

    start_marker = "## Recent Listings\n"
    start_index = readme_contents.index(start_marker) + 1 if start_marker in readme_contents else len(readme_contents)
    readme_contents[start_index:] = [markdown_table + "\n"]

    with open('README.md', 'w') as readme_file:
        readme_file.writelines(readme_contents)
        readme_file.flush()

"""
Send new listings to Telegram channel.
"""

api_token = os.getenv('BOT_API_KEY')
channel_id = os.getenv('CHANNEL_ID')

# Debugging: Check if API keys are loaded correctly
if not api_token or not channel_id:
    print("ERROR: API token or channel ID not found!")
else:
    print(f"API Token: {api_token[:5]}**** (truncated for security)")
    print(f"Channel ID: {channel_id}")

telegram_url = f'https://api.telegram.org/bot{api_token}/sendMessage'

for index, row in new_listings.iterrows():
    # Extract the raw URL from the Markdown link
    raw_url = row['Link'].replace('[🔗](', '').replace(')', '')
    
    # Use MarkdownV2 and escape special characters
    message = (
        f"🏙️ {row['🏙️ District']}\n"
        f"💰 {row['💰 Rent (€)']} €\n"
        f"📏 {row['📏 Size (m²)']} m²\n"
        f"🛏️ {row['🛏️ Rooms']} rooms\n"
        f"🔗 [Link]({raw_url.replace('.', '\\.').replace('-', '\\-')})"
    )
    
    message_data = {
        'chat_id': channel_id,
        'text': message,
        'parse_mode': 'MarkdownV2'  # Use MarkdownV2 for better escaping
    }
    
    # Debugging: Print the message data being sent to Telegram
    print(f"Sending message data to Telegram: {message_data}")
    
    response = requests.post(telegram_url, data=message_data)
    
    if response.status_code != 200:
        print(f"Failed to send message for listing: {raw_url}. Response: {response.text}")
    else:
        print(f"Message sent successfully for listing: {raw_url}")
