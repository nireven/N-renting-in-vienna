import pandas as pd
import os
import requests
import re

"""
Update README.md with the 20 most recent listings.
"""

# Read and sort the data
df = pd.read_csv('check_these.csv')
df['Published Date'] = pd.to_datetime(df['Published Date'])
df = df.sort_values(by='Published Date', ascending=False)

# Select the top 20 listings
recent_listings = df.head(20)
recent_listings = recent_listings[['Rent (€)', 'Size (m²)', 'Rooms', 'Location', 'Link']]

# Transform 'Location' column
recent_listings['Location'] = recent_listings['Location'].apply(
    lambda x: f"{x.split(',')[1].split('.')[0]}. {x.split(',')[-1].strip()}"
)

# Apply transformations for display
recent_listings = recent_listings.rename(columns={
    'Rent (€)': '💰 Rent (€)',
    'Size (m²)': '📏 Size (m²)',
    'Rooms': '🛏️ Rooms',
    'Location': '🏙️ District'
})

recent_listings['Link'] = recent_listings['Link'].apply(lambda x: f'[🔗]({x})')

current_listings = recent_listings.copy()

# Read the old README.md and extract existing listings
try:
    with open('README.md', 'r') as readme_file:
        readme_contents = readme_file.read()
    # Extract the markdown table from README.md
    table_pattern = r'\|.*\|\n(\|.*\|\n)+'
    match = re.search(table_pattern, readme_contents)
    if match:
        table_text = match.group(0)
        old_listings = pd.read_csv(pd.compat.StringIO(table_text), sep='|', engine='python')
        # Clean up DataFrame (remove empty columns and rows)
        old_listings = old_listings.dropna(axis=1, how='all')
        old_listings = old_listings.dropna(axis=0, how='all')
        # Remove leading and trailing whitespace from column names
        old_listings.columns = [col.strip() for col in old_listings.columns]
        # Remove unnecessary index column if present
        if '' in old_listings.columns:
            old_listings = old_listings.drop(columns=[''])
        # Remove leading and trailing whitespace from data
        for col in old_listings.columns:
            old_listings[col] = old_listings[col].str.strip()
        # Remove the header separator row (the second row)
        old_listings = old_listings.iloc[1:].reset_index(drop=True)
    else:
        old_listings = pd.DataFrame()
except FileNotFoundError:
    old_listings = pd.DataFrame()

# Identify new listings by comparing 'Link' columns
if not old_listings.empty:
    # Extract the raw link from the markdown link
    old_listings['Link'] = old_listings['Link'].apply(lambda x: re.search(r'\((.*?)\)', x).group(1))
    current_listings_raw = current_listings.copy()
    current_listings_raw['Link'] = current_listings_raw['Link'].apply(lambda x: re.search(r'\((.*?)\)', x).group(1))
    new_listings = current_listings_raw[~current_listings_raw['Link'].isin(old_listings['Link'])]
else:
    # If no old listings, all current listings are new
    current_listings_raw = current_listings.copy()
    current_listings_raw['Link'] = current_listings_raw['Link'].apply(lambda x: re.search(r'\((.*?)\)', x).group(1))
    new_listings = current_listings_raw.copy()

# Update README.md
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

# Send new listings to Telegram
for _, row in new_listings.iterrows():
    message = (
        f"**District**: {row['🏙️ District']}\n"
        f"**Rent**: {row['💰 Rent (€)']} €\n"
        f"**Size**: {row['📏 Size (m²)']} m²\n"
        f"**Rooms**: {row['🛏️ Rooms']} rooms\n"
        f"[Link]({row['Link']})"
    )
    message_data = {
        'chat_id': channel_id,
        'text': message,
        'parse_mode': 'Markdown'
    }
    response = requests.post(telegram_url, data=message_data)