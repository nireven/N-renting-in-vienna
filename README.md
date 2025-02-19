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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                                                                                                                      | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       671.99 |            60 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/ruhige-60-m2-gro%C3%9Fe-zwei-zimmer-wohnung%21-u-bahn-station-johnstra%C3%9Fe%21-1038325202/)                                                                                                                        | Feb 19, 14:47      |
|       748.36 |            50 |          2 | 04. Wieden               | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1040-wieden/n%C3%A4he-st.-elisabeth-platz-kleine-2-zimmer-wohnung-f%C3%BCr-jungebliebene-1205570002/)                                                                                                                                               | Feb 19, 14:23      |
|       599    |            45 |          2 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/provisionsfrei-&-unbefristet%21-ruhige-wohnung-in-zentraler-lage-1381275211/)                                                                                                                                                          | Feb 19, 14:12      |
|       689    |            60 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/provisionsfrei-&-unbefristet%21-ruhige-wohnung-beim-neuen-landgut-1524927764/)                                                                                                                                                       | Feb 19, 14:06      |
|       450    |           140 |          5 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/ein-helles-zimmer-mit-direktem-terrassenzugang-in-7-zimmer-studenten-wohngemeinschaft-mit-5-schlafzimmern-22-m%C2%B2-terrasse-f%C3%BCr-studentinnen-wg-geeignet-%281-k%C3%BCche-2-badezimmer-und-2-wcs%29-ab-1.-april-2-1746791727/) | Feb 19, 12:58      |
|       580    |            50 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/2-zimmer-in-stilaltbau-992635862/)                                                                                                                                                                                                   | Feb 19, 12:42      |
|       749    |            40 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/%2Aprovisionsfrei%2A-2-zimmer-wohnung-wilhelminenstra%C3%9Fe-41-867124760/)                                                                                                                                                          | Feb 19, 10:52      |
|       623.58 |            63 |          3 | 02. Leopoldstadt         | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/gemeindewohnung-mit-direktvergabr-1927370518/)                                                                                                                                                                                    | Feb 19, 10:00      |
|       716.8  |            52 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/ger%C3%A4umige-2-zimmer-wohnung-im-eg-1214111912/)                                                                                                                                                                                    | Feb 19, 02:47      |
|       733.55 |            50 |          2 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/h%C3%BCbsche-2-zimmer-wohnung---n%C3%A4he-elterleinplatz---2.-stock-mit-lift-1833688315/)                                                                                                                                              | Feb 18, 17:56      |
|       530    |            16 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/zentrale-einzelzimmerwohnung-eigens-bad-wc-k%C3%BCche-und-schlafzimmer-2107993462/)                                                                                                                                                  | Feb 18, 17:14      |
|       458.26 |            46 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/gemeindewohnung-1160-wien-1406931763/)                                                                                                                                                                                               | Feb 18, 16:29      |
|       468    |            41 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/gut-gepflegte-m%C3%B6blierte-2-zimmer-wohnung-ab-01.05.2025-wiener-wohnen-1402071743/)                                                                                                                               | Feb 18, 15:30      |
|       749    |            44 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/perfekt-angelegte-2-zimmer-wohnung-hell-und-freundlich-150m-zur-u3-sackgasse-1269416129/)                                                                                                                                            | Feb 18, 15:27      |
