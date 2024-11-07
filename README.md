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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                     | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       750    |            57 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/modernisierte-2-zimmer-wohnung-in-direkter-u-bahn-und-fh-campus-n%C3%A4he-1740397186/)                              | Nov 07, 11:16      |
|       755    |            52 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/stadthalle-n%C3%A4he-%21-helle-neubauwohnung-in-hofseitiger-ruhelage-1689101383/)                   | Nov 07, 11:09      |
|       542.49 |            34 |          2 | 04. Wieden               | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1040-wieden/neu%21-preisg%C3%BCnstige-2-zimmerwohnung-mit-terrasse-zu-vermieten%21-2048243563/)                                    | Nov 07, 11:06      |
|       665    |            30 |          2 | 20. Brigittenau          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1200-brigittenau/2-zimmer-naubau-wohnung---klosterneuburger-stra%C3%9Fe-852109904/)                                                | Nov 07, 10:42      |
|       790    |            54 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/charmante-2-zimmer-dachgeschosswohnung-mit-zwei-terrassen-2069008596/)                                            | Nov 07, 10:39      |
|       790    |            42 |          2 | 23. Liesing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/erstklassige-2-zimmerwohnung-in-der-khekgasse-%7C-ruhige-lage-%7C-erstbezug-998568375/)                               | Nov 07, 10:32      |
|       798.66 |            43 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/fr%C3%B6mmlgasse---heller-neubau-mit-terrasse-2020573822/)                                                        | Nov 07, 10:16      |
|       793.07 |            52 |          2 | 23. Liesing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/unbefristet---2-zimmerwohnung-mit-terrasse-in-ruhiger-lage%21-1668417105/)                                            | Nov 07, 10:08      |
|       790    |            43 |          2 | 23. Liesing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/dg-traum%21-klimatisierter-2-zimmer-neubau-mit-freifl%C3%A4che-und-luftw%C3%A4rmepumpe-1407814580/)                   | Nov 07, 09:30      |
|       555.78 |            45 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/top-lage%21-wundersch%C3%B6ne-2-zimmer-wohnung-mitten-im-10.-bezirk%21-913393564/)                                  | Nov 07, 09:13      |
|       749.05 |            56 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/mi%28e%29tten-in-oberlaa:-unbefristete-2-zimmer-wohnung-mit-balkon-in-1100-wien-zu-mieten-1462635105/)              | Nov 07, 08:33      |
|       676.17 |            45 |          2 | 05. Margareten           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/n%C3%A4he-einsiedlerpark-hell-&-freundlich-neue-k%C3%BCche-schlafzimmer-in-den-innenhofunbefristet-2104181788/)    | Nov 07, 07:55      |
|       705.19 |            41 |          2 | 19. Döbling              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1190-d%C3%B6bling/sch%C3%B6ne-2-zimmer-wohnung-im-19.-bezirk-1140179140/)                                                          | Nov 07, 06:48      |
|       733.77 |            42 |          2 | 19. Döbling              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1190-d%C3%B6bling/gem%C3%BCtliche-singlewohnung-im-19.-bezirk-1191172900/)                                                         | Nov 07, 06:48      |
|       785.97 |            73 |          3 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/%28reserviert%29-gemeinde-wohnung-direktvergabe-3-zimmer-1094088024/)                                              | Nov 07, 06:47      |
|       718.59 |            38 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/2-zimmerwohnung-mit-balkon---zu-mieten%21-1374289724/)                                                            | Nov 06, 18:16      |
|       695    |            36 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/wien---1220---s%C3%BCdseitige-singlewohnung-n%C3%A4he-vetmed/u1-station-kagranerplatz---ab-15.11.2024-1889900530/) | Nov 06, 17:04      |
|       749.99 |            38 |          2 | 18. Währing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1180-w%C3%A4hring/2-zimmerwohnung-1449205274/)                                                                                     | Nov 06, 15:27      |
|       748.1  |            44 |          2 | 02. Leopoldstadt         | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/attraktive-2-zimmer-eckhaus-wohnung-1475643408/)                                                                 | Nov 06, 15:06      |
|       570    |            60 |          2 | 23. Liesing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/gemeinde-wohnung-nur-mit-vormerkschein-1578080393/)                                                                   | Nov 06, 15:03      |
