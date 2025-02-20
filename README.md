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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                                                                                                                                                      | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       795    |            50 |          2 | 14. Penzing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/smart-living:-gem%C3%BCtliche-2-zimmerwohnung-1829490532/)                                                                                                                                                                             | Feb 20, 10:24      |
|       549.54 |            48 |          2 | 17. Hernals      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/helle-2-zimmer-wohnung-mit-balkon-im-herzen-von-hernals-793829602/)                                                                                                                                                                    | Feb 20, 10:06      |
|       468    |            44 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/44m2-nur-mit-vormerkschein-bis-31.12.2024-direktvergabe-n%C3%A4he-u3-enkplatz-998600540/)                                                                                                                                            | Feb 19, 21:31      |
|       490    |            47 |          2 | 14. Penzing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/gemeindewohnung-1140-wien-sch%C3%B6nbrunn-n%C3%A4he---direktvergabe-1684316896/)                                                                                                                                                       | Feb 19, 20:55      |
|       550    |            54 |          2 | 14. Penzing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/%28reserviert%29-2-zimmer-wohnung-im-altbau-1649124945/)                                                                                                                                                                               | Feb 19, 18:11      |
|       725.98 |            55 |          2 | 14. Penzing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/ruhige-2-zimmer-wohnung-mit-balkon%21-2142797932/)                                                                                                                                                                                     | Feb 19, 15:49      |
|       748.36 |            50 |          2 | 04. Wieden       | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1040-wieden/n%C3%A4he-st.-elisabeth-platz-kleine-2-zimmer-wohnung-f%C3%BCr-jungebliebene-1205570002/)                                                                                                                                               | Feb 19, 14:23      |
|       599    |            45 |          2 | 17. Hernals      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/provisionsfrei-&-unbefristet%21-ruhige-wohnung-in-zentraler-lage-1381275211/)                                                                                                                                                          | Feb 19, 14:12      |
|       689    |            60 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/provisionsfrei-&-unbefristet%21-ruhige-wohnung-beim-neuen-landgut-1524927764/)                                                                                                                                                       | Feb 19, 14:06      |
|       450    |           140 |          5 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/ein-helles-zimmer-mit-direktem-terrassenzugang-in-7-zimmer-studenten-wohngemeinschaft-mit-5-schlafzimmern-22-m%C2%B2-terrasse-f%C3%BCr-studentinnen-wg-geeignet-%281-k%C3%BCche-2-badezimmer-und-2-wcs%29-ab-1.-april-2-1746791727/) | Feb 19, 12:58      |
|       580    |            50 |          2 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/2-zimmer-im-stilaltbau-992635862/)                                                                                                                                                                                                   | Feb 19, 12:42      |
|       749    |            40 |          2 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/%2Aprovisionsfrei%2A-2-zimmer-wohnung-wilhelminenstra%C3%9Fe-41-867124760/)                                                                                                                                                          | Feb 19, 10:52      |
|       623.58 |            63 |          3 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/gemeindewohnung-mit-direktvergabr-1927370518/)                                                                                                                                                                                    | Feb 19, 10:00      |
