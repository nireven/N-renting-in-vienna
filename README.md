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
|       648    |            48 |          2 | 05. Margareten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/provisionsfrei-f%C3%BCr-den-mieter%21-vogelsanggasse-zentrumsnahe-48m%C2%B2-altbauhauptmiete-3.-stock-%28kein-lift%29-studenten-bevorzugt%21-1737958667/) | Jun 05, 15:19      |
|       895    |            63 |          3 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/charmante-altbau-hauptmietwohnung-in-bester-lage---n%C3%A4he-u1-nestroyplatz-1478206211/)                                                               | Jun 05, 14:26      |
|       819.87 |            45 |          2 | 03. Landstraße   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/1030-wien:-perfekt-f%C3%BCr-einzelpersonen%3B-m%C3%B6blierte-2-zimmer-wohnung-ca.-45m%C2%B2-ab-juli-zu-vermieten%3B-eur-820--2118131786/)            | Jun 05, 12:09      |
|       810    |            49 |          2 | 09. Alsergrund   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/2-zi-im-herzen-des-9.-bezirks-zahlreiche-restaurants-und-gesch%C3%A4fte-%C3%B6ffis-direkt-in-der-innen-stadt-931272053/)                                  | Jun 05, 12:07      |
|       780    |            60 |          2 | 03. Landstraße   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/charmante-2-zimmer-altbauwohnung-in-toplage---61-m%C2%B2-in-1030-wien-kundmanngasse-7-1072760404/)                                                   | Jun 05, 11:24      |
|       713.63 |            41 |          2 | 09. Alsergrund   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/liechtensteinstra%C3%9Fe-114:-2-zimmer-wohnung-mit-kfz-stellplatz-988402127/)                                                                             | Jun 05, 11:22      |
|       899    |            61 |          2 | 03. Landstraße   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/perfekte-stadtwohnung:-direkt-bei-der-urania-mit-donaublick%21-1335060887/)                                                                          | Jun 05, 08:05      |
|       871    |            60 |          2 | 03. Landstraße   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/suche-nachmieter-1006144120/)                                                                                                                        | Jun 05, 06:58      |
|       879    |            48 |          2 | 06. Mariahilf    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1060-mariahilf/vollm%C3%B6blierte-2-zimmer-wohnung-beim-westbahnhof---sofort-beziehbar%21-1390685220/)                                                                    | Jun 05, 01:04      |
|       890    |            55 |          2 | 03. Landstraße   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/nette-p%C3%A4rchenwohnung-oder-auch-singles--2-zimmer---35-stock---privat-1259103339/)                                                               | Jun 04, 21:38      |
|       897.65 |            46 |          2 | 04. Wieden       | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1040-wieden/zentral-4.-bezirk-ruhelage-parkn%C3%A4he-1677144256/)                                                                                                         | Jun 04, 19:01      |
|       520.25 |            47 |          2 | 05. Margareten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/gemeindewohnung-nahe-matzleinsdorfer-pl.-nur-mit-g%C3%BCltigem-wiener-wohn-ticket-1980287901/)                                                            | Jun 04, 15:44      |
