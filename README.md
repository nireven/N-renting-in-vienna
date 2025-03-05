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
|       649    |            43 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/2-zimmer-wohnung-%7C-zwischen-schwedenplatz-&-karmelitermarkt-1003946559/)                                         | Mar 05, 12:00      |
|       442.62 |            43 |          2 | 03. Landstraße   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/preisg%C3%BCnstige-2-zimmer-wohnung-%2A-landstra%C3%9Fer-g%C3%BCrtel-1517314984/)                               | Mar 05, 11:58      |
|       676.5  |           nan |          3 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/mitten-im-10ten---zentral-und-ruhig-gelegen-1417930554/)                                                              | Mar 05, 11:27      |
|       623.58 |            63 |          3 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/gemeindewohnung-mit-direktvergabr-1927370518/)                                                                     | Mar 05, 10:00      |
|       593    |            61 |          3 | 17. Hernals      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/1170-wien-lascygasse-27/2/15-1594747767/)                                                                               | Mar 05, 09:50      |
|       640    |            60 |          3 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeinde-wohnung-3-zimmer-vormerkschein-nr-bis-30.04.2024-1600875961/)                                                | Mar 05, 08:53      |
|       716.8  |            52 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/ger%C3%A4umige-2-zimmer-wohnung-im-eg-1214111912/)                                                                     | Mar 05, 02:47      |
|       540    |            48 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/gemeindewohnung/-direktvergabe-1212839346/)                                                                            | Mar 04, 21:23      |
|       743    |            35 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/2-zimmer-wohnung-989031646/)                                                                                       | Mar 04, 20:55      |
|       780    |            45 |          2 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/sehr-sch%C3%B6ne-2---zimmer-neubauwohnung-n%C3%A4he-...-1563695485/)                                                  | Mar 04, 18:20      |
|       620    |            60 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/2-zimmer-direktvergabe-gemeindewohnung-1257905754/)                                                                   | Mar 04, 17:03      |
|       679.36 |            63 |          3 | 17. Hernals      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/gemeindewohnung-wiener-wohnen-vergabedatum-28.-februar-2025-1516562427/)                                                | Mar 04, 15:06      |
|       799.98 |            52 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/nachmieter-gesucht-/-mietwohnung-942922018/)                                                                          | Mar 04, 14:35      |
|       785    |            42 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/wundervolle-2-zimmer-wohnung-in-toller-lage---einbauk%C3%BCche-inklusive---ab-01.05.2025-verf%C3%BCgbar%21-878246672/) | Mar 04, 13:28      |
|       752.6  |            67 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/renovierungsbed%C3%BCrftig%21-helle-mietwohnung-n%C3%A4he-grillgasse-3.-stock-ohne-lift-1296696274/)                  | Mar 04, 12:18      |
