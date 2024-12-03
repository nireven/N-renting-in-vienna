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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District     | Link                                                                                                                                                                                                     | 📅 Published Date   |
|-------------:|--------------:|-----------:|:----------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       502.69 |            46 |          2 | 19. Döbling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1190-d%C3%B6bling/gut-aufgeteilte-zwei-zimmer-wohnung-in-grinzing-2039666508/)                                                     | Dec 03, 15:34      |
|       765.05 |            40 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/%5B06476%5D-einziehen-und-wohlf%C3%BChlen%21-gepflegte-wohnung-im-21.-bezirk.-1623348057/)                        | Dec 03, 14:36      |
|       760    |            53 |          2 | 10. Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/sehr-sch%C3%B6ne-2-zimmerwohnung-im-10.-bezirk%21%21-1413329736/)                                                   | Dec 03, 14:28      |
|       799.43 |            45 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/%7C-2-zimmer-%7C-leopoldauer-strasse-%7C-3.-obergeschoss-%7C-zweitbezug-%7C-ab-sofort-verf%C3%BCgbar-1710522099/) | Dec 03, 13:58      |
|       765    |            48 |          2 | 09. Alsergrund  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/ideale-2-zimmer-wohnung---top-lage--wg-geeignet-1913947941/)                                                       | Dec 03, 13:55      |
|       764.72 |            52 |          2 | 09. Alsergrund  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/herrliche-2-zimmer-wohnung-mit-top-anbindung-1949537520/)                                                          | Dec 03, 13:55      |
|       799.01 |            47 |          2 | 10. Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-dachgeschoss-wohnung-in-top-lage---10.bezirk.---wohntraum-1706949546/)                                     | Dec 03, 13:49      |
|       799    |            49 |          2 | 11. Simmering   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/moderner-und-urbaner-neubau-in-absoluter-ruhelage-mit-exzellenter-anbindung-und-garagenplatz-932350929/)            | Dec 03, 13:17      |
|       799    |            40 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/moderne-2-zimmerwohnung-mit-balkon%21-1155042286/)                                                                | Dec 03, 12:57      |
|       754.86 |            43 |          2 | 11. Simmering   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/ina---wohnanlage-am-leberberg-:-top-a3-13-1170112708/)                                                              | Dec 03, 12:38      |
|       798.34 |            47 |          2 | 11. Simmering   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/ina---wohnanlage-am-leberberg-:-top-a2-29-1500197418/)                                                              | Dec 03, 12:27      |
|       755.72 |            43 |          2 | 11. Simmering   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/ina---wohnanlage-am-leberberg-:-top-a2-05-2146745975/)                                                              | Dec 03, 12:08      |
|       748.62 |            40 |          2 | 11. Simmering   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/ina---wohnanlage-am-leberberg-:-top-a2-18-1851487966/)                                                              | Dec 03, 12:08      |
|       770    |            47 |          2 | 10. Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-wohnung-mit-balkon-im-viola-park-1841570745/)                                                              | Dec 03, 12:00      |
|       560    |            78 |          3 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/direkvergabe-wiener-wohnen-1234967533/)                                                                            | Dec 03, 11:37      |
|       740    |            52 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/hell-freundlich-zwei-zentral-begehbare-zimmer-n%C3%A4he-alte-donau%21-1001974147/)                                | Dec 03, 10:08      |
|       798    |            61 |          2 | 16. Ottakring   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/sch%C3%B6ne-2-zimmer-altbauwohnung-1659725876/)                                                                     | Dec 03, 10:06      |
|       630    |            36 |          2 | 17. Hernals     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/sch%C3%B6ne-2-zimmer-wohnung-in-1170-ab-sofort-1994971285/)                                                           | Dec 03, 09:29      |
|       580    |            55 |          2 | 10. Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/%28reserviert%29-wiener-wohnen-gemeinde-1442608621/)                                                                | Dec 03, 08:13      |
|       799    |            65 |          2 | 10. Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/%22einfach-zum-wohlf%C3%BChlen%21%22-1077371613/)                                                                   | Dec 03, 07:13      |
