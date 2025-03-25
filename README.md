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
|       542.93 |            41 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/provisionsfrei:-gartenseitiger-41m%C2%B2-altbau-mit-einbauk%C3%BCche---u3-n%C3%A4he-1191403242/)                      | Mar 25, 20:35      |
|       570    |            54 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-gemeindewohnung-1701717242/)                                                                                 | Mar 25, 19:11      |
|       670    |            69 |          2 | 17. Hernals      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/althauswohnung-1170-wien-69m%C2%B2-895356719/)                                                                          | Mar 25, 19:01      |
|       690    |            37 |          2 | 14. Penzing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/gr%C3%BCnblick:-ruhige-%2B-freundliche-2-zimmerwohnung-n%C3%A4he-linie-49-und-u4-ober-st.-veit%21-1019107827/)          | Mar 25, 16:16      |
|       499    |            47 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/helle-befristete-altbaumiete-in-renoviertem-stilhaus-893548877/)                                                       | Mar 25, 16:08      |
|       612    |            64 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/g%C3%BCnstige-gemeindewohnung-direktvergabe-1956908554/)                                                           | Mar 25, 14:06      |
|       785    |            42 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/wundervolle-2-zimmer-wohnung-in-toller-lage---einbauk%C3%BCche-inklusive---ab-01.05.2025-verf%C3%BCgbar%21-878246672/) | Mar 25, 13:28      |
|       696.68 |            67 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/n%C3%A4he-schloss-hetzendorf-=-2-zimmer-wohnung-=-belghofergasse-1669965135/)                                          | Mar 25, 13:13      |
|       619.01 |            58 |          2 | 17. Hernals      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/wg-geeignet---n%C3%A4he-elterleinplatz-1365044654/)                                                                     | Mar 25, 11:18      |
|       450    |            42 |          2 | 03. Landstraße   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/ruhige-gemeindewohnung-im-3.-bezirk---direktvergabe-%28nur-mit-g%C3%BCltigem-vormerkschein%29-1673550943/)      | Mar 25, 10:30      |
|       454    |            43 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/voll-m%C3%B6blierte-gemeindewohnung-mit-direktvergabe-%28nur-mit-g%C3%BCltigem-vormerkschein%29-1279888228/)          | Mar 25, 00:54      |
