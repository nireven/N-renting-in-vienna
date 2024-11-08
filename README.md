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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                                                         | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       497    |            55 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeindewohnung-mit-wundersch%C3%B6ner-aussicht-1972336147/)                                                                                                            | Nov 08, 00:31      |
|       620    |            28 |          2 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/zweitwohnung-%7C-studentenwohnung-795194672/)                                                                                                                             | Nov 07, 20:21      |
|       679    |            38 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/urbanes-wohnen-in-deiner-neuen-2-zimmerwohnung-mit-balkon-im-wildgarten-1852290692/)                                                                                     | Nov 07, 19:42      |
|       730    |            55 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/provisionsfrei-f%C3%BCr-den-mieter%21-hasnerstra%C3%9Fe-hofruhelage-altbauerstbezug-55m%C2%B2-neue-komplettk%C3%BCche-wg-eignung%21-studenten-bevorzugt%21-1039056920/) | Nov 07, 19:33      |
|       719    |            34 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1220-wien---kirschbl%C3%BCtenpark---u1-n%C3%A4he-kagran---helle-hofseitige-ruhige-singlewohnung---provisionsfrei-1906948080/)                                          | Nov 07, 17:04      |
|       769    |            43 |          2 | 05. Margareten           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/sonnige-topmiete---erstbezug-1664639619/)                                                                                                                              | Nov 07, 15:27      |
|       689    |            66 |          3 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/vermietung-3-zimmer-wohnung-2100524494/)                                                                                                                              | Nov 07, 15:17      |
|       780    |            39 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/top-gepflegte-helle-2-zimmer-wohnung-mit-balkon-in-ruhiger-lage-1654625958/)                                                                                          | Nov 07, 15:07      |
|       799.98 |            42 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/gem%C3%BCtliche-2-zimmer-wohnung-mit-balkon---n%C3%A4he-meidlinger-hauptstra%C3%9Fe%21-2134798976/)                                                                      | Nov 07, 14:15      |
|       561.11 |            41 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/in-sanierung---n%C3%A4he-u4-/-u6-ii-terrasse-im-garten-ii-2-zimmer-mit-separater-k%C3%BCche-ii-beim-gaudenzdorfer-g%C3%BCrtel-798182927/)                                | Nov 07, 14:07      |
|       714    |            36 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/wien---1150---klimatisierte-helle-singlewohnung-im-6ten-liftstock---n%C3%A4he-u6-station--gumpendorferstra%C3%9Fe-1762056592/)                          | Nov 07, 14:06      |
|       749    |            36 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/1210-wien---sensationelle-ruhige-neubau-gartenwohnung-inklusive-komplettk%C3%BCche-1513762631/)                                                                       | Nov 07, 14:06      |
|       749.62 |            61 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/helle-2-zimmer-altbauwohnung-1784266801/)                                                                                                                               | Nov 07, 13:17      |
|       725    |            44 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/top-erstbezug-mit-kleinem-balkon-1162558783/)                                                                                                                           | Nov 07, 12:58      |
|       685    |            65 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/ger%C3%A4umige-gemeindewohnung-im-14.-bezirk-zu-vergeben-868860133/)                                                                                                      | Nov 07, 12:54      |
|       728.21 |            35 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/wohnen-in-floridsdorf---2-zimmer-wohnung-mit-balkon-und-garagenplatz-n%C3%A4he-shopping-city-nord-&-klink-floridsdorf-836134213/)                                     | Nov 07, 12:20      |
|       736    |            63 |          3 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/gemeindewohnung-direktvergabe-3-zimmer-1859939417/)                                                                                                     | Nov 07, 12:20      |
|       747.76 |            44 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/traumhaftes-neubauprojekt-mit-hochwertiger-ausstattung-und-freifl%C3%A4chen-in-zentraler-lage-1563246811/)                                                              | Nov 07, 12:15      |
|       504.26 |            42 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/schmuckst%C3%BCck-am-brunnenmarkt-1009745277/)                                                                                                                          | Nov 07, 11:39      |
|       750    |            57 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/modernisierte-2-zimmer-wohnung-in-direkter-u-bahn-und-fh-campus-n%C3%A4he-1740397186/)                                                                                  | Nov 07, 11:16      |
