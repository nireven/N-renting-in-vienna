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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District     | Link                                                                                                                                                                                                                       | 📅 Published Date   |
|-------------:|--------------:|-----------:|:----------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       884.4  |            64 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/ruhige-wohnung-%28innenhof%29-auf-der-pragerstra%C3%9Fe-76-mit-loggia-%7C-kaufoption-nach-5-jahren-m%C3%B6glich-2015108638/)        | May 21, 17:25      |
|       896.96 |            54 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/provisionsfreier-mietkauf-in-gretl%27s-garten%21-1323578673/)                                                                        | May 21, 17:17      |
|       895    |            47 |          2 | 14. Penzing     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/sonnige-ruhige-wohnung-1584655273/)                                                                                                     | May 21, 17:09      |
|       795    |            54 |          2 | 03. Landstraße  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/3.erdbergstrasse---provisionsfreie-charmante-2-zimmer-neubaumiete-direkt-beim-kardinal-naglplatz-2105617351/)                   | May 21, 15:32      |
|       891.67 |            44 |          2 | 14. Penzing     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/einziehen-und-wohlf%C3%BChlen:-lichtdurchflutete-2-zimmer-wohnung-mit-einbauk%C3%BCche-und-loggia---ab-01.06.-beziehbar%21-2102987612/) | May 21, 15:28      |
|       899    |            42 |          2 | 14. Penzing     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/42m%C2%B2---1.stock---13m%C2%B2-terrasse---moderne-2-zimmer-wohnung-mit-heiz--und-k%C3%BChlkombi-1797747482/)                           | May 21, 14:49      |
|       781.81 |            54 |          2 | 12. Meidling    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/2-zimmer-altbau-mit-guter-anbindung-920846177/)                                                                                        | May 21, 14:27      |
|       899    |            47 |          2 | 16. Ottakring   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/wundersch%C3%B6ne-2-zimmerwohnung-mit-balkon-in-u-bahn-n%C3%A4he-1729833699/)                                                         | May 21, 13:18      |
|       869.93 |            51 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/hochwertige-gartenwohnung-in-hirschstetten-1557963722/)                                                                              | May 21, 13:06      |
|       850.13 |            50 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/ruhige-gartenwohnung-in-hirschstetten-1467490744/)                                                                                   | May 21, 12:58      |
|       899    |            42 |          2 | 14. Penzing     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/hofseitige-garten-2-zimmer-eck-neubauwohnung---geniale-aufteilung%21-1998394624/)                                                       | May 21, 12:56      |
|       865    |            31 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/musicflats---wohnen-wo-musik-entsteht---n%C3%A4he-u1-station-neue-donau-1017347628/)                                                 | May 21, 12:37      |
|       600    |            56 |          3 | 03. Landstraße  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/gemeindewohnug-%28direktvergabe%29-nur-mit-vormerkschein-bis-31.05.2024-3-zimmer-1930743877/)                                   | May 21, 12:22      |
|       510    |            46 |          2 | 03. Landstraße  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/gemeindewohnung-2-zimmer-in-1030-zu-vergeben---direktvergabe-mit-vormerkschein-bis-30.-april-2025-1682675394/)                  | May 21, 12:04      |
|       835    |            47 |          2 | 12. Meidling    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/ideal-geschnittene-2-zimmer-wohnung-im-gr%C3%BCnen-wildgarten%21-2103606604/)                                                          | May 21, 11:47      |
|       899    |            46 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1-monat-mietzinsfrei:-erstbezug-im-gr%C3%BCnen-nahe-der-u2---zwischen-badeteich-hirschstetten-&-seestadt-1583719861/)                | May 21, 11:44      |
|       835    |            44 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/2-zimmer-neubauwohnung-inkl.-komplettk%C3%BCche-balkon-au%C3%9Fenfl%C3%A4che-und-kellerabteil-/-k2-34-922083671/)                    | May 21, 11:19      |
|       849    |            65 |          2 | 12. Meidling    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/helle-2-zimmer-wohnung-mit-pkw-stellplatz-und-lift---n%C3%A4he-schloss-sch%C3%B6nbrunn-und-bahnhof-1966069909/)                        | May 21, 11:12      |
|       569    |            52 |          2 | 20. Brigittenau | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1200-brigittenau/%2Atop-altbau-mit-wintergarten-u6-um%60s-eck%2A-1983177099/)                                                                        | May 21, 10:28      |
|       798.28 |            45 |          2 | 14. Penzing     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/sanierte-2-zimmer-wohnung-%7C-tolle-ausstattung-%7C-bahnhof-penzing-1529095853/)                                                        | May 21, 08:46      |
