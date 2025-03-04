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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                        | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       785    |            42 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/wundervolle-2-zimmer-wohnung-in-toller-lage---einbauk%C3%BCche-inklusive---ab-01.05.2025-verf%C3%BCgbar%21-878246672/)                  | Mar 04, 13:28      |
|       752.6  |            67 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/renovierungsbed%C3%BCrftig%21-helle-mietwohnung-n%C3%A4he-grillgasse-3.-stock-ohne-lift-1296696274/)                                   | Mar 04, 12:18      |
|       750    |            35 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/360%C2%B0-tour-//-neubau-balkonwohnung-am-wienerberg-783053018/)                                                                        | Mar 04, 07:13      |
|       799    |            84 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/%22perfekt-zum-wohlf%C3%BChlen%21%22-1268461944/)                                                                                      | Mar 04, 07:10      |
|       550    |            34 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/%222-zimmer-wohnung-n%C3%A4he-u3-station-schweglerstra%C3%9Fe%22-1901443782/)                                          | Mar 04, 07:10      |
|       545    |            54 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/gemeindewohnung-direktvergabe-997187755/)                                                                                              | Mar 03, 23:30      |
|       799    |            36 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/hofseitige-2-zimmer-neubauwohnung-mit-idealer-aufteilung-1313787120/)                                                                    | Mar 03, 18:35      |
|       526.43 |            51 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/gemeindewohnung-1500893406/)                                                                                                           | Mar 03, 18:33      |
|       799    |            37 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/37m%C2%B2---2.stock---moderne-2-zimmer-wohnung-mit-heiz--und-k%C3%BChlkombi-1255935771/)                                                 | Mar 03, 16:55      |
|       720    |            42 |          2 | 05. Margareten           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/vermieten-gepflegte-wohnung-in-guter-lage-1050-wien-1532518638/)                                                                      | Mar 03, 16:08      |
|       557.12 |            43 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/erstbezug-nach-sanierung---2-zimmer-wohnung-in-zentraler-lage-1771938847/)                                             | Mar 03, 14:51      |
|       715.83 |            45 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/moderne-sehr-helle-dachgeschosswohnung-mit-sonniger-terrasse---2er-wg-tauglich---vis-a-vis-u3-station-enkplatz-gelegen%21-2080381507/) | Mar 03, 14:27      |
|       728    |            61 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/gut-geschnittene-wohnung-in-guter-lage-932927905/)                                                                                     | Mar 03, 13:49      |
