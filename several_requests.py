import requests
import csv
import time
import random
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm

# Function to fetch data from a single page with retry mechanism for 429, timeout, and other errors
def fetch_page_data(page, retries=3, timeout=1):
    url = "https://www.willhaben.at/webapi/iad/search/atz/seo/immobilien/mietwohnungen/mietwohnung-angebote"
    querystring = {"page": str(page), "rows": "1000"}
    headers = {
        "accept": "application/json",
        "x-wh-client": "api@willhaben.at;responsive_web;server;1.0.0;desktop"
    }
    
    try:
        response = requests.get(url, headers=headers, params=querystring, timeout=timeout)
        if response.status_code == 429:
            print(f"Rate limited on page {page}. Waiting 5 seconds before retrying...")
            time.sleep(5)
            if retries > 0:
                return fetch_page_data(page, retries - 1, timeout)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4XX, 5XX)
        return response.json()
    except requests.Timeout:
        print(f"Timeout on page {page}. Retrying ({retries} attempts left)...")
        if retries > 0:
            return fetch_page_data(page, retries - 1, timeout)
        else:
            print(f"Failed to fetch page {page} after retries.")
            return None
    except requests.exceptions.RequestException as e:
        if retries > 0:
            print(f"Error fetching page {page}: {e}. Retrying ({retries} attempts left)...")
            time.sleep(1)  # Small delay before retrying
            return fetch_page_data(page, retries - 1, timeout)
        else:
            print(f"Failed to fetch page {page} after retries.")
            return None

# Function to parse useful information from a page's data
def parse_data(data):
    ads = []
    if data and "advertSummaryList" in data and "advertSummary" in data["advertSummaryList"]:
        for advert in data['advertSummaryList']['advertSummary']:
            ad_id = advert.get('id', 'N/A')
            description = advert.get('description', 'N/A')
            location = 'N/A'
            postcode = 'N/A'
            price = 'N/A'
            rooms = 'N/A'
            size = 'N/A'
            state = 'N/A'
            district = 'N/A'
            location_quality = 'N/A'
            floor = 'N/A'
            property_type = 'N/A'
            published_date = 'N/A'
            rent = 'N/A'
            address = 'N/A'
            
            for attribute in advert.get('attributes', {}).get('attribute', []):
                if attribute['name'] == 'LOCATION':
                    location = ', '.join(attribute.get('values', []))
                elif attribute['name'] == 'POSTCODE':
                    postcode = ', '.join(attribute.get('values', []))
                elif attribute['name'] == 'PRICE':
                    price = ', '.join(attribute.get('values', []))
                elif attribute['name'] == 'NUMBER_OF_ROOMS':
                    rooms = ', '.join(attribute.get('values', []))
                elif attribute['name'] == 'ESTATE_SIZE':
                    size = ', '.join(attribute.get('values', []))
                elif attribute['name'] == 'STATE':
                    state = ', '.join(attribute.get('values', []))
                elif attribute['name'] == 'DISTRICT':
                    district = ', '.join(attribute.get('values', []))
                elif attribute['name'] == 'LOCATION_QUALITY':
                    location_quality = ', '.join(attribute.get('values', []))
                elif attribute['name'] == 'FLOOR':
                    floor = ', '.join(attribute.get('values', []))
                elif attribute['name'] == 'PROPERTY_TYPE':
                    property_type = ', '.join(attribute.get('values', []))
                elif attribute['name'] == 'PUBLISHED_String':
                    published_date = ', '.join(attribute.get('values', []))
                elif attribute['name'] == 'RENT/PER_MONTH_LETTINGS':
                    rent = ', '.join(attribute.get('values', []))
                elif attribute['name'] == 'ADDRESS':
                    address = ', '.join(attribute.get('values', []))
            
            ads.append([ad_id, description, location, postcode, price, rooms, size, state, district, location_quality, floor, property_type, published_date, rent, address])
    return ads

# Function to save data to CSV
def save_to_csv(ads_data):
    with open('listings/rental_data.csv', mode='a', newline='', encoding='utf-8') as file:  # 'a' mode for appending data
        writer = csv.writer(file)
        writer.writerows(ads_data)

# Function to fetch data for all pages and save to CSV with batching to introduce delays and save at each break
def fetch_all_data_and_save_to_csv(total_pages, batch_size=50, timeout=2):
    # Write headers to CSV before the main scraping loop (if the file doesn't exist)
    with open('listings/rental_data.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Ad ID', 'Description', 'Location', 'Postcode', 'Price', 'Rooms', 'Size (m²)', 'State', 'District', 'Location Quality', 'Floor', 'Property Type', 'Published Date', 'Rent (€)', 'Address'])
    
    page_count = 0

    for batch_start in range(1, total_pages + 1, batch_size):
        ads_data = []  # Reset for each batch
        with ThreadPoolExecutor(max_workers=10) as executor:
            futures = [executor.submit(fetch_page_data, page, timeout=timeout) for page in range(batch_start, min(batch_start + batch_size, total_pages + 1))]
            
            with tqdm(total=min(batch_size, total_pages - batch_start + 1), desc=f"Scraping Pages {batch_start}-{min(batch_start + batch_size - 1, total_pages)}") as progress_bar:
                for future in as_completed(futures):
                    data = future.result()
                    if data:
                        ads_data.extend(parse_data(data))
                    progress_bar.update(1)
        
        page_count += batch_size

        # Save the current batch to CSV
        save_to_csv(ads_data)

        # Take a break
        wait_time = random.randint(10, 20)
        print(f"Scraped {min(page_count, total_pages)} pages. Taking a break for {wait_time} seconds.")
        time.sleep(wait_time)

# Start the fetching process
if __name__ == "__main__":
    total_pages = 100 # I have to make it so it checks how many rows the database has
    fetch_all_data_and_save_to_csv(total_pages, timeout=5)
