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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                                                                                      | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       625    |            45 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/%21%21-top-sanierte-wohnung-im-4.-liftstock-zu-vermieten%21%21-673103482/)                                                                                        | Nov 16, 16:19      |
|       473.09 |            64 |          3 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/3.-zimmer-gemeindewohnung-in-1100-wien-ohne-aufzug%21-/-vormerkschein-bis-30.09.2024-/-n%C3%A4chste-sammelbesichtigung-am-17.11.24-von-16-bis-18h-%21%21-891212848/) | Nov 16, 15:28      |
|       530    |            50 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/%28reserviert%29-gemeindewohnung-12.-bezirk-%28vmd-31.10.2024%29-1731146026/)                                                                                         | Nov 16, 13:55      |
|       755    |            30 |          2 | 21. Floridsdorf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/urgem%C3%BCtliche-30m%C2%B2-designerwohnung-mit-riesiger-terrasse%21-1889468448/)                                                                                  | Nov 16, 13:05      |
|       580    |            56 |          2 | 05. Margareten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/gemeindewohnung-direktvergabe-mit-wohnticket-vor-30.10.24-1087280518/)                                                                                              | Nov 16, 13:03      |
|       630    |            45 |          2 | 20. Brigittenau  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1200-brigittenau/1200-wien-hannovergasse:-zentral-gelegene--zimmer-altbautraumwohnung-ca.45-m2-unbefristet-zu-vermieten-1229179400/)                                                | Nov 16, 12:25      |
|       790    |            49 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/viola-park---2-zimmer-und-balkon---wohnen-mit-komfort-und-ausblick---ihre-wohlf%C3%BChloase-am-laaer-berg-1233725437/)                                               | Nov 16, 11:28      |
|       760    |            45 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/viola-park---zwei-zimmer-ein-balkon---wohnen-in-perfekter-balance---ihre-wohlf%C3%BChloase-am-laaer-berg-1019099001/)                                                | Nov 16, 11:28      |
|       790    |            49 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/hochwertige-2-zimmer-wohnung-mit-balkon-und-wohlf%C3%BChlatmosph%C3%A4re---viola-park---am-laaer-berg-1094558488/)                                                   | Nov 16, 11:28      |
|       790    |            49 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/viola-park---ihre-wohlf%C3%BChloase-am-laaer-berg---leben-mit-aussicht:-2-zimmer-wohnung-mit-balkon-1168697587/)                                                     | Nov 16, 11:28      |
|       790    |            47 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/viola-park---ihre-wohlf%C3%BChloase-am-laaer-berg--gem%C3%BCtliche-2-zimmer-wohnung-mit-balkon-in-ruhiger-lage-1488914495/)                                          | Nov 16, 11:28      |
|       786.58 |            47 |          2 | 14. Penzing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/elegante-2-zimmer-wohnung-in-toplage-928046563/)                                                                                                                       | Nov 16, 09:25      |
|       560    |            55 |          2 | 22. Donaustadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/gemeindewohnung-mit-balkon-2047842329/)                                                                                                                             | Nov 16, 09:23      |
|       563.88 |            82 |          3 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/gemeindewohnung-zu-vergeben-%282.-bez%29-1030780942/)                                                                                                             | Nov 16, 04:20      |
|       729    |            33 |          2 | 22. Donaustadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/exklusives-wohnen-in-stadlau---erzherzog-karl-stra%C3%9Fe-bahnhof-und-u2-stadlau-in-wenigen-gehminuten%21-1536752301/)                                              | Nov 16, 03:26      |
|       792    |            39 |          2 | 22. Donaustadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/moderne-2-zimmer-neubauwohnung-mit-balkon-und-blick-ins-gr%C3%BCne%21-2012724801/)                                                                                  | Nov 16, 02:38      |
|       620    |            70 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/wohnung-nur-995-euro-ink.-bk-h-und-ww-847353122/)                                                                                                                    | Nov 15, 23:31      |
|       759.57 |            41 |          2 | 23. Liesing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/miet-kauf%21---singlehit%21-2-zimmer-neubauwohnung-in-beliebter-wohngegend-liesing%60s---nahe-perchtholdsdorfer-heide-1095208325/)                                     | Nov 15, 20:32      |
|       799    |            52 |          2 | 17. Hernals      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/sonnige-2-zimmer-wohnung-in-ruhiger-lage-1195424816/)                                                                                                                  | Nov 15, 20:08      |
|       799    |            46 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/preiswerte-2-zimmerwohnung-mit-balkon-im-1.-og-im-gr%C3%BCner-umgebung-2009116743/)                                                                                   | Nov 15, 17:36      |
