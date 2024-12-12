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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District     | Link                                                                                                                                                                                                                        | 📅 Published Date   |
|-------------:|--------------:|-----------:|:----------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       790    |            43 |          2 | 09. Alsergrund  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/m%C3%B6blierte-wohnung-f%C3%BCr-eine-person-in-wien-9.-bezirk-1849488992/)                                                            | Dec 12, 11:43      |
|       735    |            38 |          2 | 12. Meidling    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/%2Aneues-projekt%2A-urbanes-wohnen-im-wildgarten-ab-01.02.2025-1377855747/)                                                             | Dec 12, 11:11      |
|       614.76 |            58 |          2 | 03. Landstraße  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/rasumofskygasse-27%21-miete-inkl.-heizkosten%21-786027760/)                                                                      | Dec 12, 10:58      |
|       792.34 |            43 |          2 | 16. Ottakring   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/kleinwohnung-topsaniert-1715251189/)                                                                                                   | Dec 12, 10:52      |
|       749.97 |            43 |          2 | 14. Penzing     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/gemuetliche-2-zimmerwohnung-an-der-h%C3%BCtteldorferstra%C3%9Fe-1508438578/)                                                             | Dec 12, 10:47      |
|       790    |            54 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/charmante-2-zimmer-dachgeschosswohnung-mit-zwei-terrassen-2069008596/)                                                               | Dec 12, 10:39      |
|       656.12 |            54 |          2 | 20. Brigittenau | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1200-brigittenau/provisionsfrei%21-robert-blumgasse-1%21-1912663387/)                                                                                 | Dec 12, 10:23      |
|       790    |            42 |          2 | 14. Penzing     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/entz%C3%BCckende-2-zimmer-miete-mit-garten-n%C3%A4he-auhof-center-1992259277/)                                                           | Dec 12, 09:57      |
|       740.83 |            60 |          2 | 14. Penzing     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/heller-studentenhit-1283496078/)                                                                                                         | Dec 12, 09:52      |
|       630    |            60 |          3 | 05. Margareten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/zur-direktvergabe-nur-mit-wiener-wohnticket-vor-31.08.2024-f%C3%BCr-3-wohnr%C3%A4ume.-1875846217/)                                    | Dec 12, 09:46      |
|       789.88 |            50 |          2 | 04. Wieden      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1040-wieden/privat---altbauwohnung-mit-2-parkettzimmern-in-sehr-guter-lage-%7C-unbefristet-1329418981/)                                               | Dec 12, 09:25      |
|       428    |            43 |          2 | 20. Brigittenau | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1200-brigittenau/gemeindewohnung-direktvergabe-2-zimmer-vms-31.10.2024-1301778257/)                                                                   | Dec 12, 08:58      |
|       749    |            39 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/gut-geschnittene-2-zimmer-wohnung-mit-knapp-40m2---leo-131---ab-01.02-1026345968/)                                                   | Dec 12, 08:57      |
|       793.9  |            51 |          2 | 09. Alsergrund  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/gem%C3%BCtliche-2-zimmer-wohnung-in-der-alserstra%C3%9Fe-30-zu-vermieten%28-offenen-besichtigung-10.12.2024-um-15-uhr%29-1695822736/) | Dec 12, 08:45      |
|       750    |            52 |          3 | 03. Landstraße  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/vintage-3-zimmer-wohnung-n%C3%A4he-belvedere-zu-vermieten-1228082846/)                                                           | Dec 12, 08:25      |
|       790    |            50 |          2 | 17. Hernals     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/wundersch%C3%B6ne-2-zimmer-neubauwohnung-%28kein-makler-keine-provision%29-1974071456/)                                                  | Dec 12, 08:03      |
|       733.77 |            42 |          2 | 19. Döbling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1190-d%C3%B6bling/gem%C3%BCtliche-singlewohnung-im-19.-bezirk-1191172900/)                                                                            | Dec 12, 06:48      |
|       705.19 |            41 |          2 | 19. Döbling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1190-d%C3%B6bling/sch%C3%B6ne-2-zimmer-wohnung-im-19.-bezirk-1140179140/)                                                                             | Dec 12, 06:48      |
|       715    |            45 |          2 | 04. Wieden      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1040-wieden/wiedner-hauptstra%C3%9Fe---hofseitiger-2-zimmer-altbau-zu-vermieten-2143509124/)                                                          | Dec 12, 03:31      |
|       750    |            41 |          2 | 12. Meidling    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/provisionsfrei:-neu-sanierte-ruhige-2-zimmer-whg-bei-u6-niederhofstr.-830780841/)                                                       | Dec 11, 21:54      |
