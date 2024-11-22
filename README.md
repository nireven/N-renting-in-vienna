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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                                         | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       721.83 |            62 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/moderne-ruhige-2-zimmer-wohnung-%2862m%C2%B2%29-1006214001/)                                                         | Nov 22, 12:21      |
|       785    |            44 |          2 | 22. Donaustadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/2-zimmer-neubauwohnung-inkl.-komplettk%C3%BCche-loggia-au%C3%9Fenfl%C3%A4che-und-kellerabteil-/-k2-48-1231874088/)     | Nov 22, 11:17      |
|       763.58 |            51 |          2 | 23. Liesing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/sanierte-2-zimmerwohnung-in-rodaun-1765009507/)                                                                           | Nov 22, 10:00      |
|       599.44 |            55 |          2 | 22. Donaustadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/erstbezug---betreutes-wohnen-%28ab-dem-60.-lebensjahr%29-in-1220-wien-1057134043/)                                     | Nov 22, 09:57      |
|       799.1  |            52 |          2 | 23. Liesing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/%23%23-ubahn-n%C3%A4he---sch%C3%B6n-&-charmant---2-zimmer-%23%23-896280538/)                                              | Nov 22, 09:27      |
|       600    |            48 |          2 | 18. Währing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1180-w%C3%A4hring/wohnung-1180-wien-gentzgasse-2012897879/)                                                                            | Nov 22, 08:20      |
|       560    |            53 |          2 | 21. Floridsdorf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/gemeindewohnung-in-direktvergabe-1068293872/)                                                                         | Nov 22, 08:08      |
|       799    |            55 |          2 | 22. Donaustadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/2-zimmer-wohnung-nahe-dem-westfield-donauzentrum---hervorragende-infrastruktur---ab-01.12.-beziehbar%21-1320797671/)   | Nov 22, 08:05      |
|       667.7  |            47 |          2 | 23. Liesing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/helle-und-ruhige-2-zimmer-wohnung-%7C-zellmann-immobilien-2012782510/)                                                    | Nov 22, 07:24      |
|       678.83 |            49 |          2 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/gem%C3%BCtliche-2-zimmer-wohnung-im-3.-og-2009648704/)                                                                  | Nov 22, 02:49      |
|       763.54 |            34 |          2 | 19. Döbling      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1190-d%C3%B6bling/%2A%2Aerstbezug---hofseite%2A%2A-neubauwohnung-mit-balkon-in-sehr-guter-lage%21-1195879260/)                         | Nov 21, 20:43      |
|       786    |            43 |          2 | 20. Brigittenau  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1200-brigittenau/mietwohnung-im-20-bezirk-2085719919/)                                                                                 | Nov 21, 19:21      |
|       630.75 |            58 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/2-zimmer-gemeindewohnung-%28direktvergabe%29-2008341971/)                                                                | Nov 21, 18:25      |
|       555.94 |            44 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-wohnung-mit-einbauk%C3%BCche-am-erlachplatz-1864700059/)                                                       | Nov 21, 17:27      |
|       749    |            43 |          2 | 21. Floridsdorf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/1210-wien---neubau---ostseitige-balkonwohnung-mit-perfektem-grundriss-2010887239/)                                    | Nov 21, 17:02      |
|       790    |            40 |          2 | 03. Landstraße   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/2-zi-wohnung-n%C3%A4he-belvedere-palast-1264996954/)                                                              | Nov 21, 16:55      |
|       502    |            46 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/direktvergabe---top-lage:-voll-m%C3%B6blierte-2-zimmer--gemeindewohnung-im-1020-wien---vms-vor-01.09.24-1043703898/) | Nov 21, 16:36      |
|       778.65 |            74 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/helle-ca.-74-m%C2%B2-wohnung-mit-westseitiger-loggia-%21-992127259/)                                                    | Nov 21, 15:37      |
|       780    |            39 |          2 | 21. Floridsdorf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/top-gepflegte-helle-2-zimmer-wohnung-mit-balkon-in-ruhiger-lage-1654625958/)                                          | Nov 21, 15:07      |
|       525.43 |            50 |          2 | 23. Liesing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/sch%C3%B6ne-gemeindewohnung-direktvergabe-1230-wien-1330485855/)                                                          | Nov 21, 14:16      |
