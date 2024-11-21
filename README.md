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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                    | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       725    |            44 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/top-erstbezug-mit-kleinem-balkon-1162558783/)                                                                                      | Nov 21, 12:58      |
|       600    |            65 |          3 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/praktische-gemeindewohnung---sonnige-lage-829873203/)                                                                              | Nov 21, 12:03      |
|       746.31 |            55 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/charmante-2-zimmer-wohnung-am-sechshauser-g%C3%BCrtel-%21-1142683402/)                                             | Nov 21, 11:58      |
|       790    |            48 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-wohntraum-mit-balkon-im-viola-park-1011592335/)                                                                           | Nov 21, 11:58      |
|       790    |            47 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-wohnung-mit-balkon-im-viola-park-1566207186/)                                                                             | Nov 21, 11:51      |
|       750    |            57 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/modernisierte-2-zimmer-wohnung-in-direkter-u-bahn-und-fh-campus-n%C3%A4he-1740397186/)                                             | Nov 21, 11:16      |
|       755    |            52 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/stadthalle-n%C3%A4he-%21-helle-neubauwohnung-in-hofseitiger-ruhelage-1689101383/)                                  | Nov 21, 11:09      |
|       570    |            60 |          3 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/gemeindewohnung-dirktvergabe-nur-mit-vormerkschein%21%21%21-1381019521/)                                                             | Nov 21, 10:39      |
|       790    |            54 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/charmante-2-zimmer-dachgeschosswohnung-mit-zwei-terrassen-2069008596/)                                                           | Nov 21, 10:39      |
|       799    |            48 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/%28reserviert%29-%28reserviert-wegen-zu-vielen-anfragen%29-2--zimmer-neubauwohnung-mit-balkon-an-der-donau-1396740025/)           | Nov 21, 09:30      |
|       675    |            64 |          3 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/gemeindewohnung-in-direktvergabe-zu-vergeben-1831024200/)                                                                        | Nov 21, 08:50      |
|       705.19 |            41 |          2 | 19. Döbling              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1190-d%C3%B6bling/sch%C3%B6ne-2-zimmer-wohnung-im-19.-bezirk-1140179140/)                                                                         | Nov 21, 06:48      |
|       733.77 |            42 |          2 | 19. Döbling              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1190-d%C3%B6bling/gem%C3%BCtliche-singlewohnung-im-19.-bezirk-1191172900/)                                                                        | Nov 21, 06:48      |
|       567.77 |            55 |          2 | 19. Döbling              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1190-d%C3%B6bling/gemeindewohnung-direktvergabe-1810506657/)                                                                                      | Nov 20, 21:10      |
|       560    |            56 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/2-zimmer-wohnung-/-hartlebengasse-1-17-1220-wien-/-gemeindewohnung-%21%21-nur-mit-vormerkschein-bis-31.08.2024%21%21-1292651993/) | Nov 20, 20:59      |
|       770    |            36 |          2 | 19. Döbling              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1190-d%C3%B6bling/ruhige-2-zimmer-wohnung-mit-loggia-und-gr%C3%BCnem-ausblick-1062590326/)                                                        | Nov 20, 20:40      |
|       487.16 |            58 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/ihre-2-zimmerwohnung-in-ottakring---ideal-und-erschwinglich-1328390489/)                                                           | Nov 20, 19:32      |
|       658    |            62 |          3 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/gemeinde-wohnung-direkt-vergabe-kaiserm%C3%BChlen-neben-u1-833386502/)                                                            | Nov 20, 17:44      |
|       750    |            44 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/brunnenmarkt:-stylische-2-zimmer-wohnung-mit-gutem-grundriss-in-hofruhelage-1860136196/)                                           | Nov 20, 15:29      |
|       670    |            63 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeindewohnung-direktvergabe-vms-31.10.2024-859612510/)                                                                           | Nov 20, 14:26      |
