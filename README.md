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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                                                                 | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       520    |            60 |          2 | 22. Donaustadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/wohnung-zu-vermieten-1521748133/)                                                                                                              | Dec 10, 20:42      |
|       764.19 |            78 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/sch%C3%B6ne-2-zimmerwohnung-unbefristet-zu-mieten-1602204884/)                                                                                  | Dec 10, 19:33      |
|       640.01 |            33 |          2 | 09. Alsergrund   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/nette-2-zimmer--altbauwohnung-n%C3%A4he-w%C3%A4hringer-stra%C3%9Fe-1854236408/)                                                                | Dec 10, 18:16      |
|       755.9  |            47 |          2 | 21. Floridsdorf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/moderne-2-zimmer-wohnung-mit-balkon-perfekt-ausgerichtet-f%C3%BCr-ruhe---nur-wenige-schritte-vom-bahnhof-floridsdorf-entfernt%21-1111885035/) | Dec 10, 17:39      |
|       482    |            43 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeinde-wohnung-43-m%C2%B2-2-zimmerwohnung-2008548347/)                                                                                        | Dec 10, 17:36      |
|       786.09 |            43 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/freundliche-helle-altbauwohnung-wg-geeignet---2-getrennte-schlafr%C3%A4ume-1298843722/)                                                         | Dec 10, 17:16      |
|       749.34 |            62 |          3 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/wg-taugliche-25-zimmer-wohnung-nahe-lugner-city-1422544592/)                                                                                    | Dec 10, 15:46      |
|       787.39 |            62 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/erstbezug---2-zimmer---62-m%C2%B2---unbefristet---altbau---n%C3%A4he-bahnhof-meidling-2129139096/)                                               | Dec 10, 14:57      |
|       780    |            50 |          2 | 22. Donaustadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/2-zimmer-neubauwohnung-in-1220-1333264685/)                                                                                                    | Dec 10, 14:37      |
|       799.01 |            47 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-dachgeschoss-wohnung-in-top-lage---10.bezirk.---wohntraum-1706949546/)                                                                 | Dec 10, 13:49      |
|       770    |            47 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-wohnung-mit-balkon-im-viola-park-1841570745/)                                                                                          | Dec 10, 12:00      |
|       595    |            52 |          2 | 20. Brigittenau  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1200-brigittenau/sonniger-altbau-nahe-u6-dresdnerstra%C3%9Fe-1109947926/)                                                                                      | Dec 10, 11:59      |
|       795    |            48 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/viola-park---gem%C3%BCtliche-2-zimmer-wohnung-mit-balkon---ihr-neues-zuhause-wartet%21-am-laaer-berg-1843229963/)                               | Dec 10, 11:39      |
|       799    |            42 |          2 | 18. Währing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1180-w%C3%A4hring/sehr-sch%C3%B6ne-mietwohnung-1987707435/)                                                                                                    | Dec 10, 10:58      |
|       562.31 |            43 |          2 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/atelier-:-%29---%3E.-ist-keine-mietwohnung-preiswert-&-aussergew%C3%B6hnlich---56231-eur-bruttomiete-993515347/)                                | Dec 10, 09:18      |
|       749    |            31 |          2 | 19. Döbling      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1190-d%C3%B6bling/singlehit-in-d%C3%B6bling%21%21-1192271109/)                                                                                                 | Dec 10, 04:36      |
|       721.25 |            50 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/erstbezug-nach-sanierung:-2-zimmer-wohnung-im-gr%C3%BCnen-1763482013/)                                                                           | Dec 10, 02:45      |
|       750.2  |            65 |          2 | 03. Landstraße   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/sonnige-2-zimmer-teilm%C3%B6blierte-altbau-wohnung-im-fasanviertel-1568861462/)                                                           | Dec 09, 23:52      |
|       700    |            70 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/gemeindewohnung-premiumausbau-1027601926/)                                                                                                   | Dec 09, 22:11      |
|       680    |            81 |          3 | 20. Brigittenau  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1200-brigittenau/gemeinde-wohnung-vormerkschein-31.05.2024-1850603245/)                                                                                        | Dec 09, 21:33      |
