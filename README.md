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

## Recent Listings

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                                                                       |
|-------------:|--------------:|-----------:|:-------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|       599    |            57 |          3 | 20. Brigittenau          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1200-brigittenau/gemeinde-wohnung-1204539861/)                                                                                                                                                       |
|       780    |            39 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/top-gepflegte-helle-2-zimmer-wohnung-mit-balkon-in-ruhiger-lage-1654625958/)                                                                                                        |
|       770    |            76 |          3 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/gemeindewohnung---nachmieter-1755544890/)                                                                                                                                               |
|       770.78 |            48 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/erstbezug---ruhige-und-zentral-begehbare-2-zimmerwohnung-gleich-bei-der-u1-troststra%C3%9Fe%21-1226234220/)                                                                           |
|       460    |            43 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeinde-wohnung-zu-vergeben-1100-wien-1948576845/)                                                                                                                                   |
|       745    |            43 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/sch%C3%B6ne-2-zimmer-wohnung-im-12.-bezirk-924315819/)                                                                                                                                 |
|       795    |            42 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/dachterrassenwohnung-neubau-2-zimmer-inkl.-komplettk%C3%BCche-und-kellerabteil-/-k2-61-1165590027/)                                                                                  |
|       485    |            46 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/gemeinde-wohnung-direktvergabe-vmd-bis-31.10.2024-1281673265/)                                                                                                        |
|       760.99 |            49 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/ruhig-gelegene-2-zimmer-neubauwohnung-inkl-balkon-au%C3%9Fenfl%C3%A4che-komplettk%C3%BCche-und-kellerabteil-nahe-bahnhof-floridsdorf---mit-parkplatz-82-euro-zu-mieten-1720969019/) |
|       755    |            52 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/stadthalle-n%C3%A4he-%21-helle-neubauwohnung-in-hofseitiger-ruhelage-1689101383/)                                                                                     |
|       790    |            54 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/charmante-2-zimmer-dachgeschosswohnung-mit-zwei-terrassen-2069008596/)                                                                                                              |
|       790    |            42 |          2 | 23. Liesing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/erstklassige-2-zimmerwohnung-in-der-khekgasse-%7C-ruhige-lage-%7C-erstbezug-998568375/)                                                                                                 |
|       799.1  |            52 |          2 | 23. Liesing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/%23%23-ubahn-n%C3%A4he---sch%C3%B6n-&-charmant---2-zimmer-%23%23-989242957/)                                                                                                            |
|       739.45 |            38 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/fully-furnished.-hell-und-ruhig---eine-perfekte-kleine-wohnung-voll-m%C3%B6bliert-1001661999/)                                                                                          |
|       743.97 |            52 |          2 | 13. Hietzing             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1130-hietzing/2-zimmer-wohnung-im-gr%C3%BCnen:-erstbezug-nach-sanierung-1968875370/)                                                                                                                 |
|       733.77 |            42 |          2 | 19. Döbling              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1190-d%C3%B6bling/gem%C3%BCtliche-singlewohnung-im-19.-bezirk-1191172900/)                                                                                                                           |
|       705.19 |            41 |          2 | 19. Döbling              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1190-d%C3%B6bling/sch%C3%B6ne-2-zimmer-wohnung-im-19.-bezirk-1140179140/)                                                                                                                            |
|       790    |            56 |          3 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/erstbezug-in-heller-sanierter-altbauwohnung-782617572/)                                                                                                                               |
|       749    |            41 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1220-wien---genochplatz---helle-gepfegte-neubauwohnung-im-4ten-liftstock---sofortbezug-1857182406/)                                                                                  |
|       760    |            55 |          2 | 05. Margareten           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/2-zimmerwohnung%2A-privat-1366897509/)                                                                                                                                               |
