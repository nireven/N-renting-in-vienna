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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                                                  | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       741.16 |            59 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/provisionsfrei:-unbefristeter-59m%C2%B2-altbau-mit-lift-n%C3%A4he-wasserturm-favoriten---1100-wien-1475598775/)                  | Nov 08, 21:37      |
|       731.33 |            72 |          3 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/gemeindewohnung-1020-wien---direktvergabe-961976560/)                                                                         | Nov 08, 21:04      |
|       716.78 |            38 |          2 | 18. Währing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1180-w%C3%A4hring/provisionsfrei:-gartenseitiger-38m%C2%B2-altbau-mit-2-zimmern-u.-einbauk%C3%BCche---1180-wien-918828505/)                     | Nov 08, 20:34      |
|       759.57 |            41 |          2 | 23. Liesing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/miet-kauf%21---singlehit%21-2-zimmer-neubauwohnung-in-beliebter-wohngegend-liesing%60s---nahe-perchtholdsdorfer-heide-1095208325/) | Nov 08, 20:32      |
|       680    |            44 |          2 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/privat%21-2-zimmerwohnung-zu-vermieten-1865971676/)                                                                              | Nov 08, 20:25      |
|       799    |            40 |          2 | 05. Margareten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/energieeffizientes-gut-angebundenes-2-zi-raumwunder---provisionsfrei-1747515262/)                                               | Nov 08, 18:05      |
|       799    |            46 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/preiswerte-2-zimmerwohnung-mit-balkon-im-1.-og-im-gr%C3%BCner-umgebung-2009116743/)                                               | Nov 08, 17:36      |
|       650    |            35 |          2 | 17. Hernals      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/zweitwohnung-%7C-studentenwohnung-mit-lift-2004559041/)                                                                            | Nov 08, 16:27      |
|       475    |            46 |          2 | 20. Brigittenau  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1200-brigittenau/gemeindewohnung-2-zimmer-%28vollm%C3%B6beliert%29-1323955363/)                                                                 | Nov 08, 16:09      |
|       761.86 |            53 |          2 | 23. Liesing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/%28reserviert%29-neubauwohnung-zu-vermieten-1328245928/)                                                                           | Nov 08, 15:46      |
|       585    |            38 |          2 | 18. Währing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1180-w%C3%A4hring/1180-freundliche-2-zimmer-wohnung-1542713237/)                                                                                | Nov 08, 15:13      |
|       420    |            15 |          4 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/wg-zimmer/-room-in-shared-flat-m%C3%B6bliert/-furnished-564595195/)                                                              | Nov 08, 14:57      |
|       775    |            48 |          2 | 21. Floridsdorf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/%22flori-flats%22:-mietkauf-in-floridsdorf---idyllisches-wohnen-in-heurigengegend-737461147/)                                  | Nov 08, 14:45      |
|       770    |            49 |          2 | 21. Floridsdorf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/stammersdorfer-wohnparadies:-mietwohnungen-mit-kaufoption-737459071/)                                                          | Nov 08, 14:38      |
|       790    |            63 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/fabelhafte-2-zimmer-wohnung-mit-dachterrassenzugang%21-1165692848/)                                                              | Nov 08, 14:06      |
|       555.94 |            44 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-wohnung-mit-einbauk%C3%BCche-am-erlachplatz-2116482066/)                                                                | Nov 08, 13:49      |
|       799.14 |            42 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/winteraktion---erster-monat-mietfrei%21-moderne-2-zimmerwohnung-mit-balkon%21-1780493551/)                                       | Nov 08, 13:36      |
|       570    |            57 |          2 | 09. Alsergrund   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/privatvergabe-1090-wien-helle-2-zimmerwohnung-im-zweiten-stock-mit-guter-verkehrsanbindung-1573523939/)                         | Nov 08, 13:25      |
|       776.15 |            52 |          2 | 22. Donaustadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/besichtigung-am-montag-um-16:00--2-zimmer-mit-balkon-im-4.-stock---1220-wien-seestadt---unbefristet-863107181/)                 | Nov 08, 13:16      |
|       766.24 |            53 |          2 | 22. Donaustadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/besichtigung-am-montag-um-16:30--2-zimmer-mit-loggia-im-2.-stock---1220-wien-seestadt---unbefristet-1231723804/)                | Nov 08, 13:16      |
