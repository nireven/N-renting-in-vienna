![Scraping Pipeline](https://github.com/AthomsG/renting-in-vienna/actions/workflows/run_pipeline.yml/badge.svg)


# Renting in Vienna

This repo fetches every **5 minutes** (Actually it's less than 30 minutes because github is a bit unreliable with the cron functionality) the latest apartments from [willhaben](https://www.willhaben.at/).
It then filters the listings according to my preferences and stores them in `check_these.csv` - You can change filter settings in the `filter_dataset.py` script.

```python
filtered_df = df[(df.State == 'Wien') & 
                 (df.Price < 800) &
                 (df.Price > 400) &
                 (df.Rooms > 1) &
                 (df['Property Type'] == 'Wohnung') &
                 (df['Published Date'] >= one_day_ago)]
```

The 20 latest listings according to my preferences are printed in this README for you conviniece! Press the link to see the listing post.
The table is sorted by publish times in ascending order, with the closest publish time to the current time listed first.

If you want to get notifications in real time for when new apartments pop up, you can join the telegram channel synced to this repo [here](https://t.me/+1HPAYOf5BSsyNTlk).

## Recent Active Listings

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                                                                    | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       895    |            60 |          2 | 07. Neubau       | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1070-neubau/n%C3%A4he-mariahilfer-strasse-charmante-2-zimmerwohnung-in-1070-wien-895787135/)                                                                      | Jun 18, 19:31      |
|       469    |            45 |          2 | 05. Margareten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/wienerwohnen-wohnung-m%C3%B6biliert%21-voraussetzung:-nur-mit-g%C3%BCltigem-wiener-wohnticket%21-857848577/)                                      | Jun 18, 17:16      |
|       883.63 |            58 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/grossz%C3%BCgige-sehr-helle-58%E2%80%AFm%C2%B2-zwei-zimmer-wohnung-in-u-bahn-n%C3%A4he---provisionsfrei-&-unbefristet-zu-mieten%21-1088191635/) | Jun 18, 16:27      |
|       795    |            54 |          2 | 03. Landstraße   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/3.erdbergstrasse---provisionsfreie-charmante-2-zimmer-neubaumiete-direkt-beim-kardinal-naglplatz-2105617351/)                                | Jun 18, 15:32      |
|       599    |            40 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/termine-bitte-online-buchen-1167023954/)                                                                                                        | Jun 18, 14:27      |
|       830    |            77 |          3 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/3-zimmer-gemeindewohnung-%2877-m%C2%B2%29-n%C3%A4he-nordbahnviertel-%7C-direktvergabe-nur-mit-vormerkschein-vor-30.04.2024-1067744152/)         | Jun 17, 23:13      |
|       895    |            40 |          2 | 03. Landstraße   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/charmante-wohnung-mit-landstrasse-hauptstrasse-n%C3%A4he-2115758901/)                                                                        | Jun 17, 21:09      |
