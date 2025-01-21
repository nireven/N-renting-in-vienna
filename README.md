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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District     | Link                                                                                                                                                                                                                                                      | 📅 Published Date   |
|-------------:|--------------:|-----------:|:----------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       615    |            60 |          3 | 14. Penzing     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/gemeindewohnung-dirktvergabe-nur-mit-vormerkschein%21%21%21-1905996321/)                                                                                               | Jan 21, 07:37      |
|       729.21 |            33 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/exklusives-wohnen-in-stadlau---erzherzog-karl-stra%C3%9Fe-bahnhof-und-u2-stadlau-in-wenigen-gehminuten.---wohntraum-2131488813/)                                    | Jan 21, 06:55      |
|       749    |            31 |          2 | 19. Döbling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1190-d%C3%B6bling/singlehit-in-d%C3%B6bling%21%21-1192271109/)                                                                                                                      | Jan 21, 04:36      |
|       714.82 |            39 |          2 | 23. Liesing     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/wundersch%C3%B6ne-sonnendurchflutete-wohnung-mit-terrasse-im-23.-bezirk%21%21%21-n%C3%A4he-u6-perfektastra%C3%9Fe%21%21-360%C2%B0-grad-besichtigung%21%21-1650734977/) | Jan 21, 03:48      |
|       721.25 |            50 |          2 | 12. Meidling    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/erstbezug-nach-sanierung:-2-zimmer-wohnung-im-gr%C3%BCnen-1763482013/)                                                                                                | Jan 21, 02:45      |
|       582.16 |            42 |          2 | 16. Ottakring   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/top-sanierte-2-zimmer-wohnung-im-dg%21-978184730/)                                                                                                                   | Jan 21, 02:45      |
|       627.25 |            54 |          2 | 05. Margareten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/54-m%C2%B2-wohnung-n%C3%A4he-u4-margareteng%C3%BCrtel-/-bruno-kreisky-park-/-einsiedlerplatz-provisionsfrei-1088696845/)                                            | Jan 20, 23:58      |
|       505.79 |            56 |          2 | 14. Penzing     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/f%C3%BCnkhgasse-24%21-bastlerhit%21-miete-inkl.-bk-und-heizkosten%21-1960910683/)                                                                                      | Jan 20, 20:37      |
|       780    |            43 |          2 | 12. Meidling    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/wohnung-914967106/)                                                                                                                                                   | Jan 20, 19:59      |
|       770    |            47 |          2 | 14. Penzing     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/privat-helle-hofseitige-sonnige-2-zimmer-wohnung-1162096568/)                                                                                                          | Jan 20, 19:09      |
|       772.61 |            39 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/orea-%7C-sch%C3%B6ne-2-zimmer-wohnung-mit-gro%C3%9Fer-terrasse-in-unmittelbarer-n%C3%A4he-zur-u6-%7C-smart-besichtigen-%C2%B7-online-anmieten-1744031802/)         | Jan 20, 17:56      |
|       781.81 |            54 |          2 | 12. Meidling    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/2-zimmer-altbau-mit-guter-anbindung-2003990576/)                                                                                                                      | Jan 20, 17:26      |
|       729    |            43 |          2 | 13. Hietzing    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1130-hietzing/%C3%A4u%C3%9Ferst-exklusive-2-zimmer-wohnung-mit-bestausstattung-%21%21-heizung-&-warmwasser-inklusive-%21%21-1980055710/)                                            | Jan 20, 17:25      |
|       692.32 |            39 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/gepflegte-studentenwohnungen-mit-einbauk%C3%BCche-in-1210-zu-mieten-1317724224/)                                                                                   | Jan 20, 17:21      |
|       742.18 |            41 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/gepflegte-studentenwohnungen-mit-einbauk%C3%BCche-in-1210-zu-mieten-1764666987/)                                                                                   | Jan 20, 16:51      |
|       769.04 |            47 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/modernes-2-zimmer-juwel-mit-balkon-nahe-floridsdorf-bahnhof---entspannte-und-naturnahe-umgebung-824346859/)                                                        | Jan 20, 15:48      |
|       795.19 |            41 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/moderne-neubauwohnung-mit-gro%C3%9Fem-balkon-und-abstellraum-nahe-u1-kagraner-platz---im-neuen-wohnviertel-am-langen-felde-1911782186/)                             | Jan 20, 15:35      |
|       759.32 |            44 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/gepflegte-studentenwohnungen-mit-einbauk%C3%BCche-in-1210-zu-mieten-1311001680/)                                                                                   | Jan 20, 15:26      |
|       790    |            55 |          2 | 10. Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/dachgeschoss-balkonwohung-hell-2-zimmer-ohne-lift-4.-stock-1274634123/)                                                                                              | Jan 20, 15:23      |
|       725    |            40 |          2 | 12. Meidling    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/%2Aneues-projekt%2A-urbanes-wohnen-im-wildgarten-ab-01.02.2025-895383341/)                                                                                            | Jan 20, 15:12      |
