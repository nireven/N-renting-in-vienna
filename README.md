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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                                                       | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       690    |            50 |          2 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/ruhige-wohnung-im-17.-bezirk-akh-und-ubahn-n%C3%A4he-privat-zu-vermieten-1960960709/)                                                                                   | Nov 05, 14:05      |
|       700    |            44 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/orea-%7C-traumhafte-2-zimmer-neubauwohnung-in-bester-lage-%7C-smart-besichtigen-%C2%B7-online-anmieten-1261856577/)                                                 | Nov 05, 13:58      |
|       716.37 |            40 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/orea-%7C-gem%C3%BCtliche-neubauwohnung-mit-gro%C3%9Fem-garten-und-top-anbindung-%7C-smart-besichtigen-%C2%B7-online-anmieten-957197651/)                            | Nov 05, 13:52      |
|       795    |            51 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/wundersch%C3%B6ne-2-zimmer-wohnung-mit-terrasse-1939918169/)                                                                                          | Nov 05, 13:51      |
|       798.88 |            41 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/sonnwend-living%21-inklusive-k%C3%BCche%21-erstbezug%21-elektrische-raffstores%21-klima-vorb.%21-n%C3%A4he-u1.---wohntraum-774645004/)                                | Nov 05, 13:49      |
|       779.01 |            43 |          2 | 23. Liesing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/2-zimmer-neubauwohnung-mit-komplettk%C3%BCche-balkon-au%C3%9Fenfl%C3%A4che-und-kellerabteil/-bg17-2-08-1513550130/)                                                     | Nov 05, 13:31      |
|       795    |            45 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/baujahr-2020-van-der-n%C3%BCll-gasse---hofseitige-2-zimmer-mit-957m2-gro%C3%9Fem-balkon-1877544970/)                                                                  | Nov 05, 12:35      |
|       473.09 |            64 |          3 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/3.-zimmer-gemeindewohnung-in-1100-wien-ohne-aufzug%21-/-vormerkschein-bis-30.09.2024-/-n%C3%A4chste-sammelbesichtigung-am-10.11.24-von-14-bis-17h-%21%21-1551815967/) | Nov 05, 12:33      |
|       782.71 |            51 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/attraktive-wohnung-mit-loggia-nahe-floridsdorfer-wasserpark-1515002523/)                                                                                            | Nov 05, 12:31      |
|       799.84 |            46 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/orea-%7C-helle-2-zimmer-wohnung-mit-guter-%C3%B6ffentlicher-anbindung-%7C-smart-besichtigen-%C2%B7-online-anmieten-1282757982/)                                       | Nov 05, 12:26      |
|       799.05 |            65 |          2 | 18. Währing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1180-w%C3%A4hring/gersthof-/-helle-gepflegte-zwei-zimmerwohnung-1221482886/)                                                                                                         | Nov 05, 12:13      |
|       749    |            46 |          2 | 23. Liesing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/ruhige-25-zimmerwohnung-in-guter-lage-%7C-zellmann-immobilien-1178243261/)                                                                                              | Nov 05, 11:37      |
|       728    |            52 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/unbefristet-neubau-hofherrgasse-1432332544/)                                                                                                                          | Nov 05, 10:56      |
|       740    |            52 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/hell-freundlich-zwei-zentral-begehbare-zimmer-n%C3%A4he-alte-donau%21-1001974147/)                                                                                  | Nov 05, 10:08      |
|       762.37 |            50 |          2 | 13. Hietzing             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1130-hietzing/moderne-sehr-helle-2-zimmerwohnung-in-ober-st.veit%21-966171344/)                                                                                                      | Nov 05, 09:40      |
|       725    |            43 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-wohnung-im-10.bezirk---renovierter-altbau---gute-anbindung-und-infrastruktur-1894245947/)                                                                    | Nov 05, 09:17      |
|       515    |            50 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-gemeindewohnung-direktvergabe-vmd-31.10.24-1942982013/)                                                                                                      | Nov 05, 09:10      |
|       690    |            43 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/2-zimmerwohnung-ab-sofort-zu-vermieten-1686215108/)                                                                                                                    | Nov 05, 09:06      |
|       779    |            44 |          2 | 20. Brigittenau          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1200-brigittenau/wohnung-im-bestzustand---kompakte-2-zimmer-f%C3%BCr-unter-800eur-827709437/)                                                                                        | Nov 05, 08:28      |
|       794.63 |            53 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/ina-%E2%97%8F-die-ecke-hat-mehr-charme-:-b3-07-1611092922/)                                                                                                           | Nov 05, 08:07      |
