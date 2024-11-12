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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District     | Link                                                                                                                                                                                                                                                              | 📅 Published Date   |
|-------------:|--------------:|-----------:|:----------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       792    |            39 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/moderne-2-zimmer-neubauwohnung-mit-balkon-und-blick-ins-gr%C3%BCne%21-1201935902/)                                                                                          | Nov 12, 21:31      |
|       492    |            52 |          2 | 10. Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/direktvergabe-2-zimmer-gemeindewohnung-4000%E2%82%AC-abl%C3%B6se-vormerkschein-31.07.2024-1934508411/)                                                                       | Nov 12, 21:27      |
|       695    |            43 |          2 | 10. Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/zweizimmer-erstbezug-in-hauptbahnhof-n%C3%A4he-824306479/)                                                                                                                   | Nov 12, 19:35      |
|       798    |            47 |          2 | 19. Döbling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1190-d%C3%B6bling/toplage-n%C3%A4he-s45-oberd%C3%B6bling-%7C-helle-2-zimmer-%7C-einzigartiges-preis-leistungs-verh%C3%A4ltnis-1597423785/)                                                  | Nov 12, 18:49      |
|       683    |            49 |          2 | 18. Währing     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1180-w%C3%A4hring/%28reserviert%29-sch%C3%B6ne-2-zimmer-altbauwohnung-mit-charme-im-18.-bezirk---nachmieter-gesucht%21-1893116067/)                                                         | Nov 12, 17:29      |
|       654    |            57 |          2 | 16. Ottakring   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/u-6-n%C3%A4he-hippgasse-topaltbau-hauptmiete-unbefristet-f%C3%BCr-p%C3%A4rchen-oder-single-geeignet-1926607185/)                                                             | Nov 12, 16:54      |
|       658.27 |            65 |          3 | 10. Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/renovierungsbed%C3%BCrftige-3-zimmer-wohnung-%7C-altbau-%7C-klinik-favoriten-%7C-4.-stock-ohne-lift-1194254801/)                                                             | Nov 12, 16:27      |
|       740.79 |            48 |          2 | 03. Landstraße  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/preiswerte-altbau-wohnung-zwei-zimmer---n%C3%A4he-landstrasser-haupstra%C3%9Fe-1803641523/)                                                                            | Nov 12, 14:26      |
|       765.37 |            45 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/tolle-2-zimmer-wohnung-mit-idealer-raumaufteilung-in-guter-und-infrastrukturell-ansprechender-lage%21-1791769254/)                                                         | Nov 12, 14:18      |
|       749    |            36 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/1210-wien---ruhige-neuwertige-2-zimmer-singlewohnung-mit-aussicht-2139163726/)                                                                                             | Nov 12, 14:01      |
|       716.37 |            40 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/orea-%7C-gem%C3%BCtliche-neubauwohnung-mit-gro%C3%9Fem-garten-und-top-anbindung-%7C-smart-besichtigen-%C2%B7-online-anmieten-957197651/)                                   | Nov 12, 13:52      |
|       798.88 |            41 |          2 | 10. Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/sonnwend-living%21-inklusive-k%C3%BCche%21-erstbezug%21-elektrische-raffstores%21-klima-vorb.%21-n%C3%A4he-u1.---wohntraum-774645004/)                                       | Nov 12, 13:49      |
|       799    |            38 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/leo-131---hochwertiger-neubau-zu-fairen-preisen---gut-angebunden-%28u1-leopoldau-%2B-u6-floridsdorf%29---mit-vollm%C3%B6blierter-k%C3%BCche-&-freifl%C3%A4che-1572554877/) | Nov 12, 13:48      |
|       779.01 |            43 |          2 | 23. Liesing     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/2-zimmer-neubauwohnung-mit-komplettk%C3%BCche-balkon-au%C3%9Fenfl%C3%A4che-und-kellerabteil/-bg17-2-08-1513550130/)                                                            | Nov 12, 13:31      |
|       473.09 |            64 |          3 | 10. Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/3.-zimmer-gemeindewohnung-in-1100-wien-ohne-aufzug%21-/-vormerkschein-bis-30.09.2024-/-n%C3%A4chste-sammelbesichtigung-am-17.11.24-von-16-bis-18h-%21%21-1551815967/)        | Nov 12, 12:33      |
|       770    |            47 |          2 | 10. Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-wohnung-mit-balkon-im-viola-park-1841570745/)                                                                                                                       | Nov 12, 12:00      |
|       795.74 |            64 |          2 | 23. Liesing     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/zwei-zimmer-gartenseitige-loggia-nahe-liesingbach-&-stadtpark-atzgersdorf-1574439531/)                                                                                         | Nov 12, 11:59      |
|       740.83 |            60 |          2 | 14. Penzing     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/heller-studentenhit-1283496078/)                                                                                                                                               | Nov 12, 09:52      |
|       725    |            43 |          2 | 10. Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-wohnung-im-10.bezirk---renovierter-altbau---gute-anbindung-und-infrastruktur-1894245947/)                                                                           | Nov 12, 09:17      |
|       793.9  |            51 |          2 | 09. Alsergrund  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/gem%C3%BCtliche-2-zimmer-wohnung-in-der-alserstra%C3%9Fe-30-zu-vermieten%28offene-besichtigung:-14.11-um-15:00%29-1695822736/)                                              | Nov 12, 08:45      |
