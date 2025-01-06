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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                                                                              | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       696.92 |            42 |          2 | 03. Landstraße   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/radetzkplatz-n%C3%A4he-/-2-zimmer-wohnung-/-neu-saniert-/-in-zentraler-lage-/-befristete-hauptmiete-auf-drei-jahre-1455240672/)                        | Jan 06, 09:45      |
|       790    |            46 |          2 | 21. Floridsdorf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/stammersdorfer-wohntr%C3%A4ume-erleben:-mietwohnungen-mit-option-auf-zuk%C3%BCnftigen-kauf-739383800/)                                                     | Jan 06, 08:56      |
|       798.53 |            37 |          2 | 14. Penzing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/unbefristete-neubauwohnung-in-gehweite-des-bahnhof-penzing---ruhige-seitengasse-der-linzer-stra%C3%9Fe%21-ab-m%C3%A4rz-2025%21---jetzt-zuschlagen-2060975917/) | Jan 05, 18:56      |
|       572.51 |            57 |          3 | 13. Hietzing     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1130-hietzing/direktvergabe-3-zimmer-gemeindewohnung-1933072043/)                                                                                                           | Jan 05, 18:12      |
|       777    |            64 |          2 | 22. Donaustadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/student%28inn%29enwohnung-nahe-u2.-1605479077/)                                                                                                             | Jan 05, 17:26      |
|       630    |            36 |          2 | 14. Penzing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/neu-renovierte-2-zimmer-wohnung-2082530443/)                                                                                                                   | Jan 05, 15:32      |
|       790    |            53 |          2 | 14. Penzing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/privat---2-zimmer-whg-%2853m2%29-nahe-u3-h%C3%BCtteldorfer-stra%C3%9Fe-1980849806/)                                                                            | Jan 05, 12:48      |
|       749.13 |            40 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/2-zimmer-wohnung-in-zentraler-lage-zu-vermieten-1535156517/)                                                                                              | Jan 05, 12:36      |
|       738.21 |            57 |          2 | 22. Donaustadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/2-zimmer-wohnung-f%C3%BCr-sozialbau-mitglieder-1030165400/)                                                                                                 | Jan 05, 12:26      |
|       699.94 |            48 |          2 | 21. Floridsdorf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/2-zimmer-in-floridsdorf-zu-vermieten-1118328844/)                                                                                                          | Jan 05, 12:07      |
|       600.5  |            57 |          2 | 23. Liesing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/nette-gemeindewohnung-direktvergabe-1230-wien-vorkmerkschein-bis-zum-30.09.2024oder-davor-1350930838/)                                                         | Jan 05, 12:00      |
|       749.71 |            42 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/ina---p%C3%A4rchenwohnung-mit-freifl%C3%A4che-n%C3%A4he-wasserspielplatz-leberberg-1904606435/)                                                              | Jan 05, 10:24      |
