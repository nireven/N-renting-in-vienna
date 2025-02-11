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
|       519    |            51 |          3 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/hofseitiger-altbau-nahe-yppenmarkt-1729590772/)                                                                         | Feb 11, 13:50      |
|       695.74 |            63 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/sch%C3%B6ne-2-zimmerwohnung-in-der-angeligasse-%21-1824043074/)                                                       | Feb 11, 13:38      |
|       785.01 |            42 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/wundervolle-2-zimmer-wohnung-in-toller-lage---einbauk%C3%BCche-inklusive---ab-01.05.2025-verf%C3%BCgbar%21-878246672/) | Feb 11, 13:28      |
|       694.87 |            53 |          2 | 06. Mariahilf            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1060-mariahilf/erstbezug-direkt-in-der-mollardgasse%21-1226267305/)                                                                  | Feb 11, 13:28      |
|       737.04 |            51 |          2 | 06. Mariahilf            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1060-mariahilf/gem%C3%BCtliche-2-zimmer-wohnung-1525346288/)                                                                         | Feb 11, 13:15      |
|       730    |            64 |          2 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/nahe-elterleinplatz-und-j%C3%B6rgerbad%21-1157573936/)                                                                  | Feb 11, 11:23      |
|       799    |            44 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-neubauwohnung-inkl.-komplettk%C3%BCche-loggia-und-kellerabteil-/-hs17-a-16-1693967151/)                      | Feb 11, 10:54      |
|       765    |            44 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/helle-2-zimmer-dg--wohnung-%7C-n%C3%A4he-u4-braunschweiggasse-%7C-ab-sofort-1063133928/)                                | Feb 11, 10:28      |
|       799.59 |            57 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/bezaubernde-2-zimmer-wohnung-nahe-sch%C3%B6nbrunn-mit-parkplatz-%28optional%29-1086519127/)           | Feb 11, 09:20      |
|       708.96 |            51 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/top-sanierte-2-zimmer-wohnung-im-1.og.-835884494/)                                                                    | Feb 11, 02:55      |
|       727.56 |            66 |          2 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/ruhige-2-zimmer-wohnung-provisionsfrei-unbefristet-1057479509/)                                                         | Feb 10, 22:01      |
|       526.43 |            51 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/gemeindewohnung-1500893406/)                                                                                          | Feb 10, 18:33      |
|       739.96 |            51 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/unbefristete-altbauwohnung-in-u3-n%C3%A4he-1755801817/)                                                         | Feb 10, 17:28      |
|       748.91 |            37 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/the-arrow---willkommen-im-gr%C3%BCnen-teil-simmerings-974631888/)                                                     | Feb 10, 16:49      |
|       719    |            48 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/gr%C3%BCnruhelage---unbefristete-altbaumiete-in-sch%C3%B6nem-eckzinshaus-%21-1293383388/)                              | Feb 10, 16:09      |
|       790    |            65 |          2 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/toplage%21-sonnige-2-zimmer-neubauwohnung-1538694809/)                                                                  | Feb 10, 15:57      |
|       799.98 |            52 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/nachmieter-f%C3%BCr-meine-mietwohnung-gesucht-/-rosa-jochmann-ring-16-1345788815/)                                    | Feb 10, 15:44      |
|       738    |            50 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/renovierte-wohnung-1556167138/)                                                                                        | Feb 10, 14:20      |
|       479    |            45 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/gemeindewohnung-zur-direktvergabe-nur-mit-wohnticket-bis-30.06.2024-2021589746/)                                | Feb 10, 14:15      |
