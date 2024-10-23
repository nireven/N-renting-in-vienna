import pandas as pd

df = pd.read_csv('check_these.csv')

df['Published Date'] = pd.to_datetime(df['Published Date'])
df = df.sort_values(by='Published Date', ascending=False)

recent_listings = df.head(20)
recent_listings = recent_listings[['Rent (€)', 'Size (m²)', 'Rooms', 'Location', 'Link']]

# Extract district number and name in the format '14. Penzing'
recent_listings['Location'] = recent_listings['Location'].apply(lambda x: f"{x.split(',')[1].split('.')[0]}. {x.split(',')[-1].strip()}")

recent_listings = recent_listings.rename(columns={'Rent (€)': '💰 Rent (€)', 'Size (m²)': '📏 Size (m²)', 'Rooms': '🛏️ Rooms', 'Location': '🏙️ District'})

recent_listings['Link'] = recent_listings['Link'].apply(lambda x: f'[🔗]({x})')

markdown_table = recent_listings.to_markdown(index=False)

with open('README.md', 'r') as readme_file:
    readme_contents = readme_file.readlines()

start_marker = "## Recent Listings\n"
if start_marker in readme_contents:
    start_index = readme_contents.index(start_marker) + 1
else:
    start_index = len(readme_contents)
    readme_contents.append("\n## Recent Listings\n")

readme_contents[start_index:] = [markdown_table + "\n"]

with open('README.md', 'w') as readme_file:
    readme_file.writelines(readme_contents)
    readme_file.flush()

print("README.md updated with the 20 most recent listings.")
