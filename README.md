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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                                                                                              | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       790    |            37 |          2 | 14. Penzing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/perfekt-f%C3%BCr-singles:-sehr-sch%C3%B6ne-&-ruhige-2-zi.-balkonwohnung-2094804467/)                                                                                           | Nov 22, 21:24      |
|       785    |            60 |          2 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/2-zimmer-wohnung-am-fu%C3%9Fe-des-wilhelminenbergs-1104026569/)                                                                                                              | Nov 22, 21:20      |
|       759.57 |            41 |          2 | 23. Liesing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/miet-kauf%21---singlehit%21-2-zimmer-neubauwohnung-in-beliebter-wohngegend-liesing%60s---nahe-perchtholdsdorfer-heide-1095208325/)                                             | Nov 22, 20:32      |
|       690    |            50 |          2 | 21. Floridsdorf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/wien-1210-floridsdorf-1405169109/)                                                                                                                                         | Nov 22, 19:00      |
|       799    |            46 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/preiswerte-2-zimmerwohnung-mit-balkon-im-1.-og-im-gr%C3%BCner-umgebung-2009116743/)                                                                                           | Nov 22, 17:36      |
|       520    |            49 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/direktvergabe%21%21-in-bestposition%21%21-wien-1100-1531093127/)                                                                                                             | Nov 22, 17:32      |
|       685.85 |            42 |          2 | 20. Brigittenau  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1200-brigittenau/%2Anatur-im-blick%2A-moderne-2-zimmer-wohnung-in-zentraler-lage-mit-u-bahn-anbindung-1722673767/)                                                                          | Nov 22, 17:26      |
|       741    |            76 |          3 | 14. Penzing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/gemeinde-wohnung-direkt-vergabe-wiener-wohn-ticket-brauchen-sie-mit-3-zummer-und-das-datummuss-vor-dem-30.06.2024-sein.-achtung-es-%C3%A4ndert-sich-jedes-monat.-846732733/)   | Nov 22, 16:25      |
|       790.58 |            41 |          2 | 21. Floridsdorf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/wundersch%C3%B6ne-neue-2-zimmer-wohnung-beim-bahnhof-floridsdorf%21-835049219/)                                                                                            | Nov 22, 15:45      |
|       775    |            48 |          2 | 21. Floridsdorf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/%22flori-flats%22:-mietkauf-in-floridsdorf---idyllisches-wohnen-in-heurigengegend-737461147/)                                                                              | Nov 22, 14:45      |
|       770    |            49 |          2 | 21. Floridsdorf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/stammersdorfer-wohnparadies:-mietwohnungen-mit-kaufoption-737459071/)                                                                                                      | Nov 22, 14:38      |
|       749    |            39 |          2 | 21. Floridsdorf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/leo-131---hochwertiger-neubau-zu-fairen-preisen---gut-angebunden-%28u1-leopoldau-%2B-u6-floridsdorf%29---mit-vollm%C3%B6blierter-k%C3%BCche-&-freifl%C3%A4che-1649275672/) | Nov 22, 13:57      |
|       799.14 |            42 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/winteraktion---erster-monat-mietfrei%21-moderne-2-zimmerwohnung-mit-balkon%21-1780493551/)                                                                                   | Nov 22, 13:36      |
|       798.34 |            41 |          2 | 14. Penzing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/holzwohnung-2-zimmer-fu%C3%9Fbodenheizung/-k%C3%BChlung-w%C3%A4rmepumpe-eichenparkett-u4/-linie-49%2B52/-s-bahn-1799838551/)                                                   | Nov 22, 13:20      |
|       749.01 |            52 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/renovierte-2-zimmer-wohnung---ideale-raumaufteilung-1157935289/)                                                                                                             | Nov 22, 13:17      |
|       729    |            60 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/%2Aentz%C3%BCckender-neubau-in-hofruhelage%2A-1381779268/)                                                                                                                    | Nov 22, 13:05      |
|       605.35 |            45 |          2 | 19. Döbling      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1190-d%C3%B6bling/3-monate-mietfrei%21-2-zimmerwohnung-im-19.-wiener-gemeindebezirk-n%C3%A4he-nu%C3%9Fdorfer-platz-zu-vermieten-814432459/)                                                 | Nov 22, 12:37      |
|       799    |            50 |          2 | 21. Floridsdorf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/ab-februar:-sonnige-traumhafte-neubauwohnung-am-park---provisionsfrei-mit-einladendem-balkon-1571549908/)                                                                  | Nov 22, 12:31      |
|       745.57 |            55 |          2 | 17. Hernals      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/%2Aneubau-mit-balkon-n%C3%A4he-brunnenmarkt%2A-1743416776/)                                                                                                                    | Nov 22, 12:28      |
|       721.83 |            62 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/moderne-ruhige-2-zimmer-wohnung-%2862m%C2%B2%29-1006214001/)                                                                                                              | Nov 22, 12:21      |
