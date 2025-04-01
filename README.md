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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                                       | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       790    |            74 |          3 | 03. Landstraße   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/direktvergabe-gemeindewohnung-mit-vormerkschein-30.04.2024---hervorragende-lage-949980584/)                     | Apr 01, 19:19      |
|       477    |            47 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/direktvergabe-ger%C3%A4umige-2-zimmer-wohnung-mit-wienerwohnticket:28.02.2025-1836074634/)                         | Apr 01, 17:37      |
|       759    |            58 |          2 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/%2B%2B-neu-%2B%2B-2-zimmer-wohnung-%2B%2B-thaliastra%C3%9Fe-%2B%2B-1738283935/)                                       | Apr 01, 17:20      |
|       433    |            55 |          2 | 14. Penzing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/sozialbau-wohnung-zu-vergeben%21%21-1939365866/)                                                                        | Apr 01, 16:23      |
|       785    |            42 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/wundervolle-2-zimmer-wohnung-in-toller-lage---einbauk%C3%BCche-inklusive---ab-01.05.2025-verf%C3%BCgbar%21-878246672/) | Apr 01, 13:28      |
|       660    |            56 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/sanierte-p%C3%A4rchenwohnung-n%C3%A4he-amalienbad-1891290544/)                                                        | Apr 01, 12:43      |
|       619.01 |            58 |          2 | 17. Hernals      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/wg-geeignet---n%C3%A4he-elterleinplatz-1365044654/)                                                                     | Apr 01, 11:18      |
|       700    |            37 |          2 | 14. Penzing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/kleine-15-zimmer-wohnung-1834575149/)                                                                                   | Apr 01, 10:58      |
|       450    |            42 |          2 | 03. Landstraße   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/ruhige-gemeindewohnung-im-3.-bezirk---direktvergabe-%28nur-mit-g%C3%BCltigem-vormerkschein%29-1673550943/)      | Apr 01, 10:30      |
|       770    |            41 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/stilvolle-neubauwohnung-mit-top-ausstattung---sofort-verf%C3%BCgbar%21-1180156925/)                                   | Apr 01, 07:55      |
|       468    |            44 |          2 | 17. Hernals      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/2-zimmer-gemeindewohnung-zur-direktvergabe-915976557/)                                                                  | Apr 01, 07:27      |
|       469    |            38 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/kleine-2-zimmer-wohnung-1405203863/)                                                                                  | Apr 01, 06:04      |
