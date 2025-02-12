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
|       623.58 |            63 |          3 | 02. Leopoldstadt         | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/gemeindewohnung-mit-direktvergabr-1927370518/)                                                                     | Feb 12, 10:00      |
|       780    |            47 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/top-2.66:-moderne-2-zimmer-wohnung-mit-blick-%C3%BCber-wien-2046712417/)                                                | Feb 12, 08:28      |
|       770    |            47 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/top-1.14:-neuwertige-2-zimmer-wohnung-mit-k%C3%BCche-und-loggia-1391792531/)                                            | Feb 12, 08:05      |
|       716.8  |            52 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/ger%C3%A4umige-2-zimmer-wohnung-im-eg-1214111912/)                                                                     | Feb 12, 02:47      |
|       609.97 |            59 |          2 | 02. Leopoldstadt         | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/gem%C3%BCtliche-2-zimmer-wohnung-im-3.og.-1311895345/)                                                             | Feb 12, 02:47      |
|       450    |            58 |          3 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/gemeindewohnung-direktvergabe-mit-wohnticket-3-zimmerwohnung-58m%C2%B2-m%C3%B6bliert-1072267081/)                       | Feb 12, 01:52      |
|       774    |            62 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/sehr-sch%C3%B6n-aufgeteilte-2-zimmer-wohnung-1245265926/)                                                       | Feb 11, 19:50      |
|       537.9  |            46 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/unbefristete-altbauwohnung-n%C3%A4he-yppenplatz-1097866149/)                                                          | Feb 11, 15:56      |
|       749    |            44 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/perfekt-angelegte-2-zimmer-wohnung-hell-und-freundlich-150m-zur-u3-sackgasse-1269416129/)                             | Feb 11, 15:27      |
|       503    |            42 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/2-zimmer-wohnung-in-1150-wien---ruhige-lage-gute-anbindung-884447390/)                                | Feb 11, 15:22      |
|       798    |            42 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/sch%C3%B6ne-kleine-2-zimmer-neubauwohnung%21-topzustand%21-1753880696/)                                                | Feb 11, 15:18      |
|       690    |            38 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/ruhige-charmante-2-zimmer-wohnung-sofort-beziehbar%21%21-1455656455/)                                                   | Feb 11, 15:04      |
|       519    |            51 |          3 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/hofseitiger-altbau-nahe-yppenmarkt-1729590772/)                                                                         | Feb 11, 13:50      |
|       785.01 |            42 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/wundervolle-2-zimmer-wohnung-in-toller-lage---einbauk%C3%BCche-inklusive---ab-01.05.2025-verf%C3%BCgbar%21-878246672/) | Feb 11, 13:28      |
|       737.04 |            51 |          2 | 06. Mariahilf            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1060-mariahilf/gem%C3%BCtliche-2-zimmer-wohnung-1525346288/)                                                                         | Feb 11, 13:15      |
