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
|       612    |            64 |          2 | 02. Leopoldstadt         | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/g%C3%BCnstige-gemeindewohnung-direktvergabe-1956908554/)                                                           | Mar 25, 14:06      |
|       785    |            42 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/wundervolle-2-zimmer-wohnung-in-toller-lage---einbauk%C3%BCche-inklusive---ab-01.05.2025-verf%C3%BCgbar%21-878246672/) | Mar 25, 13:28      |
|       696.68 |            67 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/n%C3%A4he-schloss-hetzendorf-=-2-zimmer-wohnung-=-belghofergasse-1669965135/)                                          | Mar 25, 13:13      |
|       619.01 |            58 |          2 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/wg-geeignet---n%C3%A4he-elterleinplatz-1365044654/)                                                                     | Mar 25, 11:18      |
|       450    |            42 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/ruhige-gemeindewohnung-im-3.-bezirk---direktvergabe-%28nur-mit-g%C3%BCltigem-vormerkschein%29-1673550943/)      | Mar 25, 10:30      |
|       454    |            43 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/voll-m%C3%B6blierte-gemeindewohnung-mit-direktvergabe-%28nur-mit-g%C3%BCltigem-vormerkschein%29-1279888228/)          | Mar 25, 00:54      |
|       785    |            52 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/helle-freundliche-2-zimmer-wohnung-mit-blick-auf-den-sonnenuntergang-2119899272/)                                      | Mar 24, 23:05      |
|       799    |            45 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/sonnwend---living%21-erstbezug---k%C3%BCche---klima---beschattung---u1-n%C3%A4he%21-1661379415/)                      | Mar 24, 20:38      |
|       726.94 |            52 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/nachmieter-gesucht---sonnige-2-zimmer-wohnung-mit-balkon-937623685/)                                                   | Mar 24, 17:56      |
|       636.22 |            43 |          2 | 02. Leopoldstadt         | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/provisionsfrei:-2-zimmer-wohnung-ruhelage-u1/-u2/-wu-1286720999/)                                                  | Mar 24, 16:18      |
|       539    |            50 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/2-zimmer-gemeindewohnung-im-15.-bezirk---ideal-als-erste-wohnung%21-1687668521/)                      | Mar 24, 15:01      |
