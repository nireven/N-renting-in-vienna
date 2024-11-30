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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District     | Link                                                                                                                                                                                                                                    | 📅 Published Date   |
|-------------:|--------------:|-----------:|:----------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       575.41 |            49 |          2 | 10. Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/helle-2-zimmer-wohnung-n%C3%A4chst-viktor-adler-markt-keplerplatz-wielandpark-u1-1721294398/)                                                      | Nov 30, 16:25      |
|       750    |            56 |          2 | 10. Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/provisionsfrei-fernkorngasse-interessante-attraktive-teilm%C3%B6blierte-2-zimmer-wohnung-in-guter-lage-matzleinsdorferplatz-n%C3%A4he-2102019983/) | Nov 30, 16:21      |
|       787.03 |            60 |          2 | 10. Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/neu-renovierte-6040-m%C2%B2-provisionsfrei-und-unbefristet-lift-2-zi-1983501988/)                                                                  | Nov 30, 14:59      |
|       510    |            53 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/gemeindewohnung-in-wien-22-%28stadlau%29---direktvergabe-mit-wohn-ticket-1922999786/)                                                             | Nov 30, 14:59      |
|       755    |            30 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/urgem%C3%BCtliche-30m%C2%B2-designerwohnung-mit-riesiger-terrasse%21-1889468448/)                                                                | Nov 30, 13:05      |
|       578    |            50 |          2 | 14. Penzing     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/50m%C2%B2-unbefristet-gemeinschaftsgarten---nur-mit-m%C3%B6bel-und-abl%C3%B6se-zu-vergeben-1793459916/)                                              | Nov 30, 11:56      |
|       790    |            49 |          2 | 10. Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/viola-park---2-zimmer-und-balkon---wohnen-mit-komfort-und-ausblick---ihre-wohlf%C3%BChloase-am-laaer-berg-1233725437/)                             | Nov 30, 11:28      |
|       790    |            47 |          2 | 10. Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/viola-park---ihre-wohlf%C3%BChloase-am-laaer-berg--gem%C3%BCtliche-2-zimmer-wohnung-mit-balkon-in-ruhiger-lage-1488914495/)                        | Nov 30, 11:28      |
|       790    |            49 |          2 | 10. Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/hochwertige-2-zimmer-wohnung-mit-balkon-und-wohlf%C3%BChlatmosph%C3%A4re---viola-park---am-laaer-berg-1094558488/)                                 | Nov 30, 11:28      |
|       790    |            49 |          2 | 10. Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/viola-park---ihre-wohlf%C3%BChloase-am-laaer-berg---leben-mit-aussicht:-2-zimmer-wohnung-mit-balkon-1168697587/)                                   | Nov 30, 11:28      |
|       790    |            52 |          2 | 17. Hernals     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/wundersch%C3%B6ne-2-zimmer-neubauwohnung-%28kein-makler-keine-provision%29-1974071456/)                                                              | Nov 30, 11:20      |
|       667    |            66 |          3 | 23. Liesing     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/gemeindewohnung/-wiener-wohnen-direktvergabe-1607718592/)                                                                                            | Nov 30, 06:26      |
|       480    |            27 |          3 | 10. Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gem%C3%BCtliche-garconniere-%21-ideal-f%C3%BCr-singles%21-wird-frisch-gereinigt-%C3%BCbergeben%21-1035778997/)                                     | Nov 30, 02:08      |
|       712    |            54 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/2-zimmer-wohnung-1381637617/)                                                                                                                    | Nov 29, 23:39      |
|       785    |            53 |          2 | 16. Ottakring   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/helle-generalsanierte-2-zimmer-wohnung-%28top-12%29-1012451842/)                                                                                   | Nov 29, 20:38      |
|       759.57 |            41 |          2 | 23. Liesing     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/miet-kauf%21---singlehit%21-2-zimmer-neubauwohnung-in-beliebter-wohngegend-liesing%60s---nahe-perchtholdsdorfer-heide-1095208325/)                   | Nov 29, 20:32      |
