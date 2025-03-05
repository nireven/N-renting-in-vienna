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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                  | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       696.64 |            51 |          2 | 05. Margareten           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/top---stilaltbauwohnung%21---n%C3%A4he-matzleinsdorferplatz-gelegen%21-1409421198/)                             | Mar 05, 20:37      |
|       629.28 |            50 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/2-zimmer-altbau-wohnung-%2B-balkon-1857522706/)                                                  | Mar 05, 19:56      |
|       676    |            57 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/gemeinde-wohnung-1362623821/)                                                                                    | Mar 05, 17:29      |
|       598    |            56 |          3 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/%2Asonniger-altbau-nahe-elterleinplatz%2A-1737237926/)                                                             | Mar 05, 13:28      |
|       745    |            42 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/%2Aprovisionsfrei%2A-sch%C3%B6negeflegte-2-zimmer-wohnung---ideal-f%C3%BCr-p%C3%A4rchen-oder-singles-871791214/) | Mar 05, 12:34      |
|       650    |            57 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/2-zimmer-wohnung-in-1030-wien---57-m%C2%B2-im-1.-liftstock-1385945099/)                                    | Mar 05, 12:22      |
|       442.62 |            43 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/preisg%C3%BCnstige-2-zimmer-wohnung-%2A-landstra%C3%9Fer-g%C3%BCrtel-1517314984/)                          | Mar 05, 11:58      |
|       745    |            39 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/pracht-werk:-gem%C3%BCtliche-2-zimmerwohnung-mit-balkon-853230679/)                                              | Mar 05, 10:36      |
|       623.58 |            63 |          3 | 02. Leopoldstadt         | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/gemeindewohnung-mit-direktvergabr-1927370518/)                                                                | Mar 05, 10:00      |
|       593    |            61 |          3 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/1170-wien-lascygasse-27/2/15-1594747767/)                                                                          | Mar 05, 09:50      |
|       640    |            60 |          3 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeinde-wohnung-3-zimmer-vormerkschein-nr-bis-30.04.2024-1600875961/)                                           | Mar 05, 08:53      |
|       716.8  |            52 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/ger%C3%A4umige-2-zimmer-wohnung-im-eg-1214111912/)                                                                | Mar 05, 02:47      |
|       540    |            48 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/gemeindewohnung/-direktvergabe-1212839346/)                                                                       | Mar 04, 21:23      |
