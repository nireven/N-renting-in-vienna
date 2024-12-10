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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                                   | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       736.11 |            55 |          2 | 22. Donaustadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/erstbezug---betreutes-wohnen-%28ab-dem-60.-lebensjahr%29-in-1220-wien-1973542120/)                               | Dec 10, 14:37      |
|       780    |            50 |          2 | 22. Donaustadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/2-zimmer-neubauwohnung-in-1220-1333264685/)                                                                      | Dec 10, 14:37      |
|       799.01 |            47 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-dachgeschoss-wohnung-in-top-lage---10.bezirk.---wohntraum-1706949546/)                                   | Dec 10, 13:49      |
|       679.1  |            46 |          2 | 17. Hernals      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/sch%C3%B6ne-2-zimmer-neubauwohnung-mit-kleinem-balkon-zu-vermieten-1206944961/)                                     | Dec 10, 12:55      |
|       770    |            47 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-wohnung-mit-balkon-im-viola-park-1841570745/)                                                            | Dec 10, 12:00      |
|       595    |            52 |          2 | 20. Brigittenau  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1200-brigittenau/sonniger-altbau-nahe-u6-dresdnerstra%C3%9Fe-1109947926/)                                                        | Dec 10, 11:59      |
|       795    |            48 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/viola-park---gem%C3%BCtliche-2-zimmer-wohnung-mit-balkon---ihr-neues-zuhause-wartet%21-am-laaer-berg-1843229963/) | Dec 10, 11:39      |
|       799    |            42 |          2 | 18. Währing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1180-w%C3%A4hring/sehr-sch%C3%B6ne-mietwohnung-1987707435/)                                                                      | Dec 10, 10:58      |
|       485.72 |            37 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/topzustand%21-1789495286/)                                                                                        | Dec 10, 10:27      |
|       562.31 |            43 |          2 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/atelier-:-%29---%3E.-ist-keine-mietwohnung-preiswert-&-aussergew%C3%B6hnlich---56231-eur-bruttomiete-993515347/)  | Dec 10, 09:18      |
|       749    |            31 |          2 | 19. Döbling      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1190-d%C3%B6bling/singlehit-in-d%C3%B6bling%21%21-1192271109/)                                                                   | Dec 10, 04:36      |
|       721.25 |            50 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/erstbezug-nach-sanierung:-2-zimmer-wohnung-im-gr%C3%BCnen-1763482013/)                                             | Dec 10, 02:45      |
|       750.2  |            65 |          2 | 03. Landstraße   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/sonnige-2-zimmer-teilm%C3%B6blierte-altbau-wohnung-im-fasanviertel-1568861462/)                             | Dec 09, 23:52      |
|       700    |            70 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/gemeindewohnung-premiumausbau-1027601926/)                                                                     | Dec 09, 22:11      |
|       680    |            81 |          3 | 20. Brigittenau  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1200-brigittenau/gemeinde-wohnung-vormerkschein-31.05.2024-1850603245/)                                                          | Dec 09, 21:33      |
|       795    |            80 |          3 | 22. Donaustadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/80-m%C2%B2-gemeindewohnung-mit-balkon-3-wohnr%C3%A4ume---direktvergabe-1272762783/)                              | Dec 09, 20:51      |
|       580    |            56 |          3 | 22. Donaustadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/newohnung-3-zimmer---direktvergabe-vms-30.11.2024-oder-fr%C3%BCher-786800420/)                                   | Dec 09, 18:09      |
|       692.33 |            39 |          2 | 21. Floridsdorf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/gepflegte-studentenwohnungen-mit-einbauk%C3%BCche-in-1210-zu-mieten-1317724224/)                                | Dec 09, 17:21      |
|       799    |            42 |          2 | 21. Floridsdorf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/moderne-2-zimmer-wohnung-in-floridsdorf:-nachhaltigkeit-trifft-wohnkomfort-1934904306/)                         | Dec 09, 17:18      |
|       742.17 |            41 |          2 | 21. Floridsdorf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/gepflegte-studentenwohnungen-mit-einbauk%C3%BCche-in-1210-zu-mieten-1764666987/)                                | Dec 09, 16:51      |
