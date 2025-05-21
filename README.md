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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                                          | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       865    |            31 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/musicflats---wohnen-wo-musik-entsteht---n%C3%A4he-u1-station-neue-donau-1017347628/)                                                                    | May 21, 12:37      |
|       600    |            56 |          3 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/gemeindewohnug-%28direktvergabe%29-nur-mit-vormerkschein-bis-31.05.2024-3-zimmer-1930743877/)                                                      | May 21, 12:22      |
|       510    |            46 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/gemeindewohnung-2-zimmer-in-1030-zu-vergeben---direktvergabe-mit-vormerkschein-bis-30.-april-2025-1682675394/)                                     | May 21, 12:04      |
|       699.41 |            39 |          2 | 05. Margareten           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/lichtdurchflutete-2-zimmer-wohnung-im-5.-bezirk%21-914529908/)                                                                                          | May 21, 11:53      |
|       835    |            47 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/ideal-geschnittene-2-zimmer-wohnung-im-gr%C3%BCnen-wildgarten%21-2103606604/)                                                                             | May 21, 11:47      |
|       899    |            46 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1-monat-mietzinsfrei:-erstbezug-im-gr%C3%BCnen-nahe-der-u2---zwischen-badeteich-hirschstetten-&-seestadt-1583719861/)                                   | May 21, 11:44      |
|       699.99 |            41 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/2-zimmer-neubauwohnung-inkl-balkon-k%C3%BCche-und-kellerabteil-/zs64-top-52-1089642302/)                                                                | May 21, 11:20      |
|       880.26 |            73 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/gro%C3%9Fz%C3%BCgige-2-zimmer-altbauwohnung---wg-geeignet-1315200909/)                                                                   | May 21, 11:20      |
|       835    |            44 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/2-zimmer-neubauwohnung-inkl.-komplettk%C3%BCche-balkon-au%C3%9Fenfl%C3%A4che-und-kellerabteil-/-k2-34-922083671/)                                       | May 21, 11:19      |
|       849    |            65 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/helle-2-zimmer-wohnung-mit-pkw-stellplatz-und-lift---n%C3%A4he-schloss-sch%C3%B6nbrunn-und-bahnhof-1966069909/)                                           | May 21, 11:12      |
|       569    |            52 |          2 | 20. Brigittenau          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1200-brigittenau/%2Atop-altbau-mit-wintergarten-u6-um%60s-eck%2A-1983177099/)                                                                                           | May 21, 10:28      |
|       798.28 |            45 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/sanierte-2-zimmer-wohnung-%7C-tolle-ausstattung-%7C-bahnhof-penzing-1529095853/)                                                                           | May 21, 08:46      |
|       799.99 |            50 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/2-zimmer-neubauwohnung-inkl.-loggia-komplettk%C3%BCche-und-kellerabteil-nahe-bahnhof-floridsdorf/-ls84-top-35-1479984052/)                             | May 21, 08:46      |
|       795    |            64 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/gem%C3%BCtliche-2-zimmer-mietwohnung-nahe-der-scn-1495470356/)                                                                                         | May 21, 07:14      |
|       800    |            45 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/erstbezug%21-stilvolle-2-zimmer-neubauwohnung_balkon_top-ausstattung_1210-wien%21-1165832201/)                                                         | May 21, 06:48      |
|       660    |            44 |          2 | 19. Döbling              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1190-d%C3%B6bling/1190-wien-heiligenst%C3%A4dter-str.-zwei-zimmer-top-14-44m%C2%B2-k%C3%BCche-im-wohnzimmer-duschbad-1.-liftstock-ruhelage-miete-eur-660---1709631176/) | May 21, 06:48      |
|       699    |            38 |          2 | 05. Margareten           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/superkompakt-%7C-saniert-%7C-zentral-1290304278/)                                                                                                       | May 21, 00:38      |
|       540    |            48 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/%21-dringend%21-gemeindewohnung%21-direktvergabe-nur-mit-g%C3%BCltigem-wiener-wohnticket-vms-30.04.25%21-1068837510/)                                     | May 20, 22:11      |
|       850    |            45 |          2 | 20. Brigittenau          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1200-brigittenau/m%C3%B6blierte-2-zimmer-wohnung-auf-der-hellwagstra%C3%9Fe-zu-vermieten-1036281423/)                                                                   | May 20, 21:28      |
|       848    |            43 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/%7C-2-zimmer-%7C-ab-september-%7C-nachvermietung-%7C-nordwestlich-%7C-balkon-%7C-an-der-alten-donau-%7C-donaustadtbr%C3%BCcke-916358290/)               | May 20, 20:39      |
