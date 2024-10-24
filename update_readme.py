import pandas as pd
import os
import requests

"""
Update README.md with the 20 most recent listings.
"""

# Read the data
df = pd.read_csv('check_these.csv')
df['Published Date'] = pd.to_datetime(df['Published Date'])
df = df.sort_values(by='Published Date', ascending=False)

# Get the 20 most recent listings
recent_listings = df.head(20)
recent_listings = recent_listings[['Rent (€)', 'Size (m²)', 'Rooms', 'Location', 'Link']]

# Adjust the Location formatting
recent_listings['Location'] = recent_listings['Location'].apply(lambda x: f"{x.split(',')[1].split('.')[0]}. {x.split(',')[-1].strip()}")

# Add emojis to the column names for the Markdown table in the README
recent_listings = recent_listings.rename(columns={
    'Rent (€)': '💰 Rent (€)', 
    'Size (m²)': '📏 Size (m²)', 
    'Rooms': '🛏️ Rooms', 
    'Location': '🏙️ District'
})

# Format the links for the README
recent_listings['Link'] = recent_listings['Link'].apply(lambda x: f'[🔗 Link]({x})')

current_listings = recent_listings.copy()

# Check for previous listings and combine
try:
    previous_listings = pd.read_csv('previous_listings.csv')
except FileNotFoundError:
    previous_listings = pd.DataFrame()

# Save recent listings to 'previous_listings.csv'
recent_listings.to_csv('previous_listings.csv', index=False)

# Find new listings by comparing with previous listings
new_listings = pd.concat([current_listings, previous_listings]).drop_duplicates(keep=False) if not previous_listings.empty else current_listings

# If there are new listings, update the README
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

# Get the bot's API key and channel ID from environment variables
api_token = os.getenv('BOT_API_KEY')
channel_id = os.getenv('CHANNEL_ID')

# Check if API keys are loaded correctly
if not api_token or not channel_id:
    print("ERROR: API token or channel ID not found!")
else:
    print(f"API Token: {api_token[:5]}**** (truncated for security)")
    print(f"Channel ID: {channel_id}")

telegram_url = f'https://api.telegram.org/bot{api_token}/sendMessage'

# Send each new listing to the Telegram channel
for index, row in new_listings.iterrows():
    # Extract the raw URL from the Markdown link
    raw_url = row['Link'].replace('[🔗 Link](', '').replace(')', '')
    
    # Prepare the message with bold text and clean formatting for Telegram
    message = (
        f"**District**: {row['🏙️ District']}\n"
        f"**Rent**: {row['💰 Rent (€)']} €\n"
        f"**Size**: {row['📏 Size (m²)']} m²\n"
        f"**Rooms**: {row['🛏️ Rooms']} rooms\n"
        f"[Link]({raw_url})"
    )
    
    # Prepare the data for the Telegram request
    message_data = {
        'chat_id': channel_id,
        'text': message,
        'parse_mode': 'Markdown'  # Regular Markdown works fine here
    }
    print(f"Sending message data to Telegram: {message_data}")
    
    # Send the message to Telegram
    response = requests.post(telegram_url, data=message_data)
    
    # Check if the message was sent successfully
    if response.status_code != 200:
        print(f"Failed to send message for listing: {raw_url}. Response: {response.text}")
    else:
        print(f"Message sent successfully for listing: {raw_url}")
