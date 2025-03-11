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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                       | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       680    |            31 |          2 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/zweitwohnung-%7C-studentenwohnung-mit-terrasse-1925081955/)                                                             | Mar 11, 16:19      |
|       785    |            42 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/wundervolle-2-zimmer-wohnung-in-toller-lage---einbauk%C3%BCche-inklusive---ab-01.05.2025-verf%C3%BCgbar%21-878246672/) | Mar 11, 13:28      |
|       530    |            48 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-gemeindewohnung-in-favoriten---direktvergabe-mit-abl%C3%B6se-1826919497/)                                    | Mar 11, 11:57      |
|       733.92 |            56 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/sanierte-2-zimmer-wohnung-im-15.-n%C3%A4he-westbahnhof-1239337781/)                                   | Mar 11, 11:47      |
|       480    |            44 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/gemeindebau-2-zimmer-direktvergabe-%28nur-mit-g%C3%BCltigem-wiener-wohn-ticket%29-1111326443/)                         | Mar 11, 11:39      |
|       619.01 |            58 |          2 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/wg-geeignet---n%C3%A4he-elterleinplatz-1365044654/)                                                                     | Mar 11, 11:18      |
|       789    |            57 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/%22panorama-city-living%22-inkl.-%22gemeinschafts-dachterrasse%22-u6-2108360611/)                                     | Mar 11, 10:57      |
|       569    |            51 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/top-altbau-beim-brunnenmarkt-921292906/)                                                                              | Mar 11, 10:57      |
|       742    |            50 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/2-zimmer-wohnung-im-15.-bezirk-1201818780/)                                                           | Mar 11, 09:31      |
|       500    |            31 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/singlewohnung-wien-landstra%C3%9Fe-1991389751/)                                                                 | Mar 11, 06:51      |
|       799.66 |            41 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/zu-vermieten%21-helle-2-zimmer-wohnung-mit-balkon_t22-buchengasse-1232369813/)                                        | Mar 11, 06:47      |
|       580    |            46 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/%28reserviert%29-perfekt-aufgeteilte-helle-wohnung-1429830033/)                                       | Mar 10, 22:35      |
|       799    |            53 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/sonnwend---living%21-erstbezug---k%C3%BCche---klima---beschattung---u1-n%C3%A4he%21-1940698360/)                      | Mar 10, 20:38      |
|       799    |            45 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/sonnwend---living%21-erstbezug---k%C3%BCche---klima---beschattung---u1-n%C3%A4he%21-1661379415/)                      | Mar 10, 20:38      |
|       799    |            36 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/hofseitige-2-zimmer-neubauwohnung-mit-idealer-aufteilung-1313787120/)                                                   | Mar 10, 18:35      |
|       700    |            42 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/hofruhelage-nach-komplettsanierung-im-herzen-des-3.-bezirks-1042598031/)                                        | Mar 10, 18:35      |
|       526.43 |            51 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/%28reserviert%29-gemeindewohnung-1500893406/)                                                                         | Mar 10, 18:33      |
|       547.51 |            34 |          2 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/hofseitiger-neubau-beim-yppenmarkt-1404740837/)                                                                         | Mar 10, 18:25      |
