import requests
import json

url = "https://www.willhaben.at/webapi/iad/search/atz/seo/immobilien/mietwohnungen/mietwohnung-angebote"

querystring = {"page": "1",
               "rows": "1000",
               "areaId": "900",      # Wien
               "PROPERTY_TYPE": "3", # Wohnung
               "periode": "2",       # posted on the last 2 days
              }

headers = {
    "accept": "application/json",
    "x-wh-client": "api@willhaben.at;responsive_web;server;1.0.0;desktop"
}

response = requests.get(url, headers=headers, params=querystring)
print(f'response: {response}')

if response.ok: # saving to pretty json so that you can inspect payload contents
  data = response.json()
  pretty_json = json.dumps(data, indent=4)
  
  with open("response_pretty.txt", "w") as file:
      file.write(pretty_json)
