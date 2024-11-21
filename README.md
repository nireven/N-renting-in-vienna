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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District     | Link                                                                                                                                                                                                                    | 📅 Published Date   |
|-------------:|--------------:|-----------:|:----------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       799    |            48 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/2-zimmer-neubauwohnung-mit-balkon-an-der-donau-1396740025/)                                                                       | Nov 21, 09:30      |
|       675    |            64 |          3 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/gemeindewohnung-in-direktvergabe-zu-vergeben-1831024200/)                                                                        | Nov 21, 08:50      |
|       733.77 |            42 |          2 | 19. Döbling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1190-d%C3%B6bling/gem%C3%BCtliche-singlewohnung-im-19.-bezirk-1191172900/)                                                                        | Nov 21, 06:48      |
|       705.19 |            41 |          2 | 19. Döbling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1190-d%C3%B6bling/sch%C3%B6ne-2-zimmer-wohnung-im-19.-bezirk-1140179140/)                                                                         | Nov 21, 06:48      |
|       567.77 |            55 |          2 | 19. Döbling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1190-d%C3%B6bling/gemeindewohnung-direktvergabe-1810506657/)                                                                                      | Nov 20, 21:10      |
|       560    |            56 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/2-zimmer-wohnung-/-hartlebengasse-1-17-1220-wien-/-gemeindewohnung-%21%21-nur-mit-vormerkschein-bis-31.08.2024%21%21-1292651993/) | Nov 20, 20:59      |
|       770    |            36 |          2 | 19. Döbling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1190-d%C3%B6bling/ruhige-2-zimmer-wohnung-mit-loggia-und-gr%C3%BCnem-ausblick-1062590326/)                                                        | Nov 20, 20:40      |
|       487.16 |            58 |          2 | 16. Ottakring   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/ihre-2-zimmerwohnung-in-ottakring---ideal-und-erschwinglich-1328390489/)                                                           | Nov 20, 19:32      |
|       658    |            62 |          3 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/gemeinde-wohnung-direkt-vergabe-kaiserm%C3%BChlen-neben-u1-833386502/)                                                            | Nov 20, 17:44      |
|       750    |            44 |          2 | 16. Ottakring   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/brunnenmarkt:-stylische-2-zimmer-wohnung-mit-gutem-grundriss-in-hofruhelage-1860136196/)                                           | Nov 20, 15:29      |
|       670    |            63 |          2 | 10. Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeindewohnung-direktvergabe-vms-31.10.2024-859612510/)                                                                           | Nov 20, 14:26      |
|       690    |            53 |          2 | 12. Meidling    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/balkonhit-mit-traumhaftem-altmannsdorfer-schlosspark-blick-%21-1724174333/)                                                         | Nov 20, 13:07      |
|       750    |            63 |          2 | 12. Meidling    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/topaltbau-hauptmiete-unbefristet-f%C3%BCr-p%C3%A4rchen-oder-single-geeignet-823048139/)                                             | Nov 20, 12:53      |
|       450    |            47 |          2 | 20. Brigittenau | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1200-brigittenau/direktvergabe-gemeindewohnung-zu-vergeben-858549974/)                                                                            | Nov 20, 12:38      |
|       777.21 |            48 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/gepflegte-studentenwohnungen-mit-einbauk%C3%BCche-in-1210-zu-mieten-1030049299/)                                                 | Nov 20, 12:22      |
|       689    |            38 |          2 | 12. Meidling    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/%2Aneues-projekt%2A-urbanes-wohnen-im-wildgarten-ab-01.02.2025-1936334166/)                                                         | Nov 20, 12:18      |
|       730    |            89 |          4 | 10. Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/top-gemeindewohnung-4-zimmer-2104361237/)                                                                                          | Nov 20, 11:35      |
|       690    |            46 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/gr%C3%BCnlage-golfplatz-s%C3%BC%C3%9Fenbrunn-n%C3%A4he-badeteich-1882252758/)                                                     | Nov 20, 11:32      |
|       799    |            40 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/moderne-2-zimmerwohnung-mit-balkon%21-1693093114/)                                                                               | Nov 20, 10:55      |
|       770    |            49 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/jetzt-mieten-sp%C3%A4ter-kaufen:-wohnen-in-stammersdorfer-naturidylle-761411382/)                                                | Nov 20, 10:07      |
