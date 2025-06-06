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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                                                                            | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       504.69 |            43 |          2 | 03. Landstraße   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/2-zimmer-gemeindewohnung-wien-f.-vormerkscheinbesitzer-1588414219/)                                                                                  | Jun 05, 22:07      |
|       850    |            38 |          2 | 03. Landstraße   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/2-room-apartment-and-rooftop-terrace-925652543/)                                                                                                     | Jun 05, 19:42      |
|       408    |            56 |          3 | 03. Landstraße   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/wiener-wohnen-direktvergabe-vormerkschein-29.04.2024-3-zimmer-1962386555/)                                                                           | Jun 05, 18:02      |
|       820.5  |            37 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/all-in-warm-miete-ab-september-2050373692/)                                                                                                             | Jun 05, 17:59      |
|       648    |            48 |          2 | 05. Margareten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/provisionsfrei-f%C3%BCr-den-mieter%21-vogelsanggasse-zentrumsnahe-48m%C2%B2-altbauhauptmiete-3.-stock-%28kein-lift%29-studenten-bevorzugt%21-1737958667/) | Jun 05, 15:19      |
|       895    |            63 |          3 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/charmante-altbau-hauptmietwohnung-in-bester-lage---n%C3%A4he-u1-nestroyplatz-1478206211/)                                                               | Jun 05, 14:26      |
|       819.87 |            45 |          2 | 03. Landstraße   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/1030-wien:-perfekt-f%C3%BCr-einzelpersonen%3B-m%C3%B6blierte-2-zimmer-wohnung-ca.-45m%C2%B2-ab-juli-zu-vermieten%3B-eur-820--2118131786/)            | Jun 05, 12:09      |
|       810    |            49 |          2 | 09. Alsergrund   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/2-zi-im-herzen-des-9.-bezirks-zahlreiche-restaurants-und-gesch%C3%A4fte-%C3%B6ffis-direkt-in-der-innen-stadt-931272053/)                                  | Jun 05, 12:07      |
|       780    |            60 |          2 | 03. Landstraße   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/charmante-2-zimmer-altbauwohnung-in-toplage---61-m%C2%B2-in-1030-wien-kundmanngasse-7%28offene-besichtigung-10.06.2025-um-15:00%29-1072760404/)      | Jun 05, 11:24      |
|       713.63 |            41 |          2 | 09. Alsergrund   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/liechtensteinstra%C3%9Fe-114:-2-zimmer-wohnung-mit-kfz-stellplatz-988402127/)                                                                             | Jun 05, 11:22      |
