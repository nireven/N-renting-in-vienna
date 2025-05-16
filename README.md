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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                    | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       740    |            70 |          3 | 05. Margareten           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/gemeinde-wohnung-direktvergabe-1922505462/)                                                                       | May 16, 21:19      |
|       774.8  |            60 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/am-kanal-73a-/-top-a073-1065124034/)                                                                               | May 16, 18:43      |
|       728.34 |            56 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/herbortgasse-28-/-top-h085-1330591623/)                                                                            | May 16, 18:43      |
|       598.39 |            40 |          2 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/topsanierte-unbefristete-altbauwohnung-in-der-balderichgasse-1410140797/)                                            | May 16, 16:25      |
|       402    |            45 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-sozialbauwohnung-n%C3%A4he-oberlaa-981599380/)                                                            | May 16, 16:16      |
|       778.22 |            54 |          2 | 09. Alsergrund           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/servitenviertel-%28pramergasse%29---miete-inkl.-heizkosten-u.-warmwasserakonto-1968396874/)                       | May 16, 15:53      |
|       690    |            65 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/sanierte-wohnung-im-1.stock-ohne-lift-1559480524/)                                                                 | May 16, 14:58      |
|       795.55 |            63 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/gut-geschnittene-eckwohnung-im-2.-liftstock---revitalisiertes-gr%C3%BCnderzeithaus-1946101800/)    | May 16, 14:27      |
|       726.89 |            36 |          2 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/neubauprojekt-hernals---bezugsfertig-juli-2025---hochwertige-mietwohnungen-%2Ainkl.-einbauk%C3%BCche%2A-1531864024/) | May 16, 13:53      |
|       523.47 |            44 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/unbefristet---wirklich-sch%C3%B6nes-2-zimmer-apartment-komplettk%C3%BCche-1733515380/)                             | May 16, 12:49      |
|       699.99 |            57 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/open-house-am-19.5.-15:50-16:10%21-anfragen-nur-per-mail---keine-anrufe%21-1103624416/)                            | May 16, 12:20      |
|       546.39 |            40 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/open-house-21.5.-16:30-16:50-uhr%21-keine-anrufe---anfragen-nur-per-mail%21-1764113241/)                             | May 16, 12:03      |
|       652.64 |            56 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/open-house-19.5.-16:30-16:50-uhr%21-anfragen-nur-per-mail---keine-anrufe%21-1366934735/)                           | May 16, 11:57      |
|       645.78 |            63 |          3 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/generalsanierte-3-zimmer-wohnung---befristet-1497167484/)                                                          | May 16, 11:36      |
|       678    |            56 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/56-m2-wohnung-wien-16-ruhige-lage-2042061403/)                                                                     | May 16, 10:46      |
|       674    |            59 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/wohnung-sozialbau-625313902/)                                                                                       | May 16, 08:18      |
