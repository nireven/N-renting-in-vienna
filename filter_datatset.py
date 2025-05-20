import pandas as pd

path_to_data = 'listings/rental_data.csv'
df = pd.read_csv(path_to_data)

df['Price'] = pd.to_numeric(df['Price'], errors='coerce')
df['Numeric District'] = df['Location'].str.extract(r'(\d{1,2})\. Bezirk').astype(float)
df['Published Date'] = pd.to_datetime(df['Published Date'], errors='coerce')

# ---------- FILTERING ---------- #

now = pd.Timestamp.now()
one_day_ago = now.tz_localize('UTC') - pd.Timedelta(days=1)

# Change the districts that you care about here
allowed_districts = {1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 14, 15, 16, 17,18,19,20,21,22,23}

filtered_df = df[(df.State == 'Wien') & 
                 (df.Price < 900) &
                 (df.Price > 400) &
                 (df.Rooms > 1) &
                 (df['Property Type'] == 'Wohnung') &
                 (df['Published Date'] >= one_day_ago) &
                 (df['Numeric District'].isin(allowed_districts))]

print(f'There are {filtered_df.shape[0]} listings that match your requirements.')

# ---------- LINKS ---------- #

# Generate the links so that I can check the pictures and stuff
def generate_links(df):
    base_url = "https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/"
    
    def build_url(row):
        district = str(row['District']).replace(" ", "-").lower() if not pd.isna(row['District']) else 'unknown-district'
        postcode = int(row['Postcode']) if not pd.isna(row['Postcode']) else 'unknown-postcode'
        location = str(row['Location']).split(",")[-1].strip().replace(" ", "-").lower() if not pd.isna(row['Location']) else 'unknown-location'
        description = str(row['Description']).replace(" ", "-").replace(",", "").lower() if not pd.isna(row['Description']) else 'no-description'
        ad_id = row['Ad ID']
        
        return f"{base_url}{district}-{postcode}-{location}/{description}-{ad_id}/"
    
    return df.apply(build_url, axis=1)


filtered_df['Link'] = generate_links(df)
filtered_df.to_csv('check_these.csv', index=False)
