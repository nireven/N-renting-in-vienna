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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                                                    | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       764.19 |            78 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/sch%C3%B6ne-2-zimmerwohnung-unbefristet-zu-mieten-1602204884/)                                                                     | Nov 26, 19:33      |
|       740    |            75 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/hauptmiethit-n%C3%A4he-enkplatz-1578235463/)                                                                                       | Nov 26, 18:58      |
|       786.09 |            43 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/freundliche-helle-altbauwohnung-wg-geeignet---2-getrennte-schlafr%C3%A4ume-1298843722/)                                            | Nov 26, 17:16      |
|       580.5  |            56 |          2 | 21. Floridsdorf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/gemeindewohnung-1210-wien---vormerkschein-nur-bis-31.10.24-953308908/)                                                           | Nov 26, 16:21      |
|       790    |            41 |          2 | 23. Liesing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/top-2-zimmer-s%C3%BCd-balkonwohnung-in-ruhiger-gr%C3%BCnlage-1479201196/)                                                            | Nov 26, 15:56      |
|       749.66 |            41 |          2 | 22. Donaustadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/smarter-wohntraum-mit-gro%C3%9Fz%C3%BCgigem-balkon---u2-seestadt-fu%C3%9Fl%C3%A4ufig-erreichbar-1882417859/)                      | Nov 26, 15:27      |
|       710.34 |            42 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/hofseitige-sch%C3%B6ne-1-zimmer-wohnung-n%C3%A4he-augarten%21-1618270075/)                                                      | Nov 26, 15:27      |
|       780    |            73 |          3 | 20. Brigittenau  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1200-brigittenau/diektvergabe-nur-mit-vormerkschein-31.5.2024-renovierte-3-zimmer-wohnung-1548508489/)                                            | Nov 26, 15:07      |
|       706.59 |            60 |          2 | 14. Penzing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/2-zimmer-daschgescho%C3%9Fwohnung-in-ruhiger-lage-bei-sch%C3%B6nbrunn-858378955/)                                                    | Nov 26, 14:47      |
|       799.01 |            47 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-dachgeschoss-wohnung-in-top-lage---10.bezirk.---wohntraum-1706949546/)                                                    | Nov 26, 13:49      |
|       750    |            46 |          2 | 21. Floridsdorf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/helle-freundliche-2-zimmer-wohnung-nahe-der-donauinsel-1234991560/)                                                              | Nov 26, 13:17      |
|       799    |            40 |          2 | 21. Floridsdorf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/moderne-2-zimmerwohnung-mit-balkon%21-1155042286/)                                                                               | Nov 26, 12:57      |
|       770    |            47 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-wohnung-mit-balkon-im-viola-park-1841570745/)                                                                             | Nov 26, 12:00      |
|       700    |            50 |          2 | 07. Neubau       | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1070-neubau/zwischenmiete-in-wien-1190099783/)                                                                                                    | Nov 26, 10:47      |
|       790.15 |            59 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-wohnung---provisionsfrei-1611971446/)                                                                                     | Nov 26, 10:39      |
|       799    |            39 |          2 | 22. Donaustadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1-monat-mietfrei:-erstbezug-im-gr%C3%BCnen-nahe-der-u2---zwischen-badeteich-hirschstetten-und-seestadt-1143083651/)               | Nov 26, 10:10      |
|       780.27 |            35 |          2 | 20. Brigittenau  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1200-brigittenau/gem%C3%BCtliche-gartenwohnung-mit-praktischen-grundriss-n%C3%A4he-u6-j%C3%A4gerstra%C3%9Fe-und-dresdner-stra%C3%9Fe-1030082805/) | Nov 26, 09:16      |
|       799    |            39 |          2 | 22. Donaustadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1-monat-mietfrei:-erstbezug-im-gr%C3%BCnen-nahe-der-u2---zwischen-badeteich-hirschstetten-und-seestadt-981921692/)                | Nov 26, 09:00      |
|       580    |            55 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/wiener-wohnen-gemeinde-1442608621/)                                                                                                | Nov 26, 08:13      |
|       749    |            46 |          2 | 23. Liesing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/ruhige-25-zimmerwohnung-in-guter-lage-%7C-zellmann-immobilien-2017122355/)                                                           | Nov 26, 07:35      |
