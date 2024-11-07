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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                                     | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       798.66 |            43 |          2 | 21. Floridsdorf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/%22brandneu%22---erstbezug-mit-terrasse-2020573822/)                                                              | Nov 07, 10:16      |
|       793.07 |            52 |          2 | 23. Liesing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/unbefristet---2-zimmerwohnung-mit-terrasse-in-ruhiger-lage%21-1668417105/)                                            | Nov 07, 10:08      |
|       790    |            43 |          2 | 23. Liesing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/dg-traum%21-klimatisierter-2-zimmer-neubau-mit-freifl%C3%A4che-und-luftw%C3%A4rmepumpe-1407814580/)                   | Nov 07, 09:30      |
|       555.78 |            45 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/top-lage%21-wundersch%C3%B6ne-2-zimmer-wohnung-mitten-im-10.-bezirk%21-913393564/)                                  | Nov 07, 09:13      |
|       749.05 |            56 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/mi%28e%29tten-in-oberlaa:-unbefristete-2-zimmer-wohnung-mit-balkon-in-1100-wien-zu-mieten-1462635105/)              | Nov 07, 08:33      |
|       676.17 |            45 |          2 | 05. Margareten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/n%C3%A4he-einsiedlerpark-hell-&-freundlich-neue-k%C3%BCche-schlafzimmer-in-den-innenhofunbefristet-2104181788/)    | Nov 07, 07:55      |
|       705.19 |            41 |          2 | 19. Döbling      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1190-d%C3%B6bling/sch%C3%B6ne-2-zimmer-wohnung-im-19.-bezirk-1140179140/)                                                          | Nov 07, 06:48      |
|       733.77 |            42 |          2 | 19. Döbling      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1190-d%C3%B6bling/gem%C3%BCtliche-singlewohnung-im-19.-bezirk-1191172900/)                                                         | Nov 07, 06:48      |
|       785.97 |            73 |          3 | 22. Donaustadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/%28reserviert%29-gemeinde-wohnung-direktvergabe-3-zimmer-1094088024/)                                              | Nov 07, 06:47      |
|       718.59 |            38 |          2 | 21. Floridsdorf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/2-zimmerwohnung-mit-balkon---zu-mieten%21-1374289724/)                                                            | Nov 06, 18:16      |
|       695    |            36 |          2 | 22. Donaustadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/wien---1220---s%C3%BCdseitige-singlewohnung-n%C3%A4he-vetmed/u1-station-kagranerplatz---ab-15.11.2024-1889900530/) | Nov 06, 17:04      |
|       749.99 |            38 |          2 | 18. Währing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1180-w%C3%A4hring/2-zimmerwohnung-1449205274/)                                                                                     | Nov 06, 15:27      |
|       748.1  |            44 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/attraktive-2-zimmer-eckhaus-wohnung-1475643408/)                                                                 | Nov 06, 15:06      |
|       570    |            60 |          2 | 23. Liesing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/gemeinde-wohnung-nur-mit-vormerkschein-1578080393/)                                                                   | Nov 06, 15:03      |
|       713.76 |            56 |          2 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/neuwertig%21-834606661/)                                                                                            | Nov 06, 14:49      |
|       673.33 |            50 |          3 | 05. Margareten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/dienstwohnung-f%C3%BCr-unternehmer-1987939541/)                                                                    | Nov 06, 13:25      |
|       674.43 |            34 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/2-zimmer-terrassenwohnung-in-n%C3%A4he-des-flughafens%21-1243507433/)                                               | Nov 06, 13:07      |
|       799.82 |            45 |          2 | 03. Landstraße   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/unbefristete-bezugsfertige-2-zimmer-klimatisiert-2-.-liftstock-n%C3%A4he-rennweg---fasanviertel-1455266098/)  | Nov 06, 12:57      |
|       749.13 |            40 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/2-zimmer-wohnung-in-zentraler-lage-zu-vermieten-1535156517/)                                                     | Nov 06, 12:36      |
|       699.94 |            48 |          2 | 21. Floridsdorf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/2-zimmer-in-floridsdorf-zu-vermieten-1118328844/)                                                                 | Nov 06, 12:07      |
