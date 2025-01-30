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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                                                             | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       799    |            38 |          2 | 22. Donaustadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1-monat-mietfrei:-erstbezug-im-gr%C3%BCnen-nahe-der-u2---zwischen-badeteich-hirschstetten-und-seestadt-1881694930/)                        | Jan 30, 07:45      |
|       499.04 |            42 |          2 | 21. Floridsdorf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/am-ho%C3%9Fplatz%21-2132264392/)                                                                                                          | Jan 30, 06:55      |
|       480    |            48 |          2 | 05. Margareten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/gemeindewohnung-direktvergabe-vmd:30.11.2024-1376592591/)                                                                                  | Jan 29, 20:09      |
|       798.79 |            43 |          2 | 21. Floridsdorf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/komfortabler-erstbezug:-2-zimmer-wohnungen-im-21.-bezirk-mit-balkon-und-moderner-k%C3%BCche.---wohntraum-1104579405/)                     | Jan 29, 18:57      |
|       622    |            55 |          3 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/gemeinde-wohnung-1918764507/)                                                                                                               | Jan 29, 18:03      |
|       715    |            36 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gem%C3%BCtliche-2--zimmer-whg---3-liftstock-inkl.-hz-u.-ww-993047565/)                                                                      | Jan 29, 17:41      |
|       760    |            47 |          2 | 21. Floridsdorf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/2-zimmer-wohnung-mit-balkon-n%C3%A4he-marchfeldkanal-879926782/)                                                                          | Jan 29, 17:18      |
|       785    |            48 |          2 | 03. Landstraße   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/rasumofskygasse:-gem%C3%BCtliche-2-zimmer-wohnung-in-hofruhelage-1248372906/)                                                         | Jan 29, 16:41      |
|       750    |            56 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/provisionsfreie-mietwohnung-fernkorngasse-interessante-attraktive-2-zimmerwohnung-in-guter-lage-matzleinsdorferplatz-n%C3%A4he-2102019983/) | Jan 29, 16:21      |
|       550    |            68 |          4 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/gemeindewohnung-zur-direktvergabe-936296652/)                                                                                               | Jan 29, 15:48      |
|       768.75 |            46 |          2 | 17. Hernals      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/helle-2-zimmerwohnung-%2B-begr%C3%BCnter-innenhof---im-17.-1655086503/)                                                                       | Jan 29, 15:32      |
|       799.99 |            43 |          2 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/2-zimmer-%7C-u3-ottakring-%7C-garagenplatz-verf%C3%BCgbar-1041913329/)                                                                      | Jan 29, 14:48      |
|       788.56 |            39 |          2 | 21. Floridsdorf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/leo-131---hochwertige-neubauwohnungen-mit-anbindung-zu-u6-s-bahn-und-u1-in-leopoldau-mit-inkludierter-k%C3%BCche-1058670682/)             | Jan 29, 14:17      |
|       495    |            45 |          2 | 21. Floridsdorf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/vormerkticket-ab-dezember-2024-1731311323/)                                                                                               | Jan 29, 14:08      |
|       595    |            32 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/provisionsfrei---sch%C3%B6ne-2-zimmer-wohnung-ideal-f%C3%BCr-p%C3%A4rchen-oder-singles-2109286336/)                                         | Jan 29, 14:03      |
|       780    |            40 |          2 | 22. Donaustadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/neubauwohnung-mit-balkon-und-idealer-anbindung-an-den-%C3%B6ffentlichen-nahverkehr-1651408411/)                                            | Jan 29, 14:02      |
|       765.95 |            47 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/hofseitige-2-zimmer-stielalbauwohnung---n%C3%A4he-u1-vorgartenstra%C3%9Fe-934931577/)                                                    | Jan 29, 12:53      |
|       767.95 |            49 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/terrassentraum-f%C3%BCr-p%C3%A4rchen---wohnung-mit-perfektem-grundriss---n%C3%A4he-einkaufszentrum-huma-eleven-1338398862/)                 | Jan 29, 12:53      |
|       785.84 |            47 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/ina---p%C3%A4rchenwohnung-mit-perfektem-grundriss---n%C3%A4he-kaiserebersdorf-1590079860/)                                                  | Jan 29, 12:53      |
|       771.62 |            42 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/n%C3%A4he-schloss-neugeb%C3%A4ude---wohnung-perfekt-f%C3%BCr-singles-oder-p%C3%A4rchen-mit-freifl%C3%A4che-1759659165/)                     | Jan 29, 12:29      |
