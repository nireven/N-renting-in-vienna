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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                                                     | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       799    |            43 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-neubauwohnung-inkl.-komplettk%C3%BCche-loggia-und-kellerabteil-bei-u1-neulaa-/hs17-a-14-825042242/)                                                        | Jan 14, 14:00      |
|       759    |            43 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/ruhig-gelegene-2-zimmer-wohnung-inkl-komplettk%C3%BCche-loggia-und-kellerabteil-bei-u1-neulaa---innenhofseitig-/hs17-a-18-1825451538/)                              | Jan 14, 13:51      |
|       712.27 |            34 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/2-zimmer-neubau-in-simmering-1110-wien:-perfekte-lage-nahe-u3%21-1126216033/)                                                                                       | Jan 14, 13:41      |
|       799    |            47 |          2 | 05. Margareten           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/sonnige-neubauwohnung-f%C3%BCr-singles-oder-paare%21-1839642744/)                                                                                                  | Jan 14, 12:57      |
|       689.06 |            49 |          2 | 13. Hietzing             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1130-hietzing/h%C3%BCgelgasse:-2-zimmer-dachgescho%C3%9Fwohnung-in-gr%C3%BCnlage-1677621748/)                                                                                      | Jan 14, 11:28      |
|       790    |            46 |          2 | 23. Liesing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/wundersch%C3%B6ne-gepflegte-2-zimmer-mit-grossem-balkon%21-789859620/)                                                                                                | Jan 14, 11:23      |
|       750    |            71 |          3 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/gemeindewohnung-direktvergabe-967536679/)                                                                                                                          | Jan 14, 11:13      |
|       750    |            48 |          2 | 08. Josefstadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1080-josefstadt/ideal-f%C3%BCr-singles-studenten-und-p%C3%A4rchen:-zwei-zimmer-wohnung-mitten-im-achten%21-open-house-24.01.2025-von-13:00-16:00-ohne-voranmeldung%21-1188368425/) | Jan 14, 10:38      |
|       717.65 |            38 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/neu%21-erstbezug%21-ideale-2-zimmer-neubauwohnung-mit-balkon%21-tiefgaragenstellpl%C3%A4tze-im-haus%21-1579238205/)                                               | Jan 14, 09:50      |
|       720.88 |            78 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/waaassss%21-721-eur-bruttomiete.-....die-ich-%C3%BCberleg-ich-mir-.....-1395745534/)                                                                | Jan 14, 09:24      |
|       562.31 |            43 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/atelier-:-%29---%3E.-ist-keine-mietwohnung-preiswert-&-aussergew%C3%B6hnlich---56231-eur-bruttomiete-993515347/)                                                    | Jan 14, 09:18      |
|       799    |            39 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1-monat-mietfrei:-erstbezug-im-gr%C3%BCnen-nahe-der-u2---zwischen-badeteich-hirschstetten-und-seestadt-981921692/)                                                 | Jan 14, 09:00      |
|       692    |            70 |          3 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/gemeinde-wohnung-1030-wien-880898176/)                                                                                                                        | Jan 14, 08:47      |
|       799.32 |            42 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/moderne-2-zimmer-wohnung-in-floridsdorf:-nachhaltigkeit-trifft-wohnkomfort%21---jetzt-zuschlagen-1070055439/)                                                     | Jan 14, 06:56      |
|       559.31 |            56 |          2 | 23. Liesing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/gemeindewohnung--2-zimmer--vms-31.12.2024-996780603/)                                                                                                                 | Jan 14, 06:04      |
|       721.25 |            50 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/erstbezug-nach-sanierung:-2-zimmer-wohnung-im-gr%C3%BCnen-1763482013/)                                                                                               | Jan 14, 02:45      |
|       582.16 |            42 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/top-sanierte-2-zimmer-wohnung-im-dg%21-978184730/)                                                                                                                  | Jan 14, 02:45      |
|       749.71 |            52 |          2 | 13. Hietzing             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1130-hietzing/erstbezug-nach-sanierung:-unbefristete-2-zimmer-wohnung-im-gr%C3%BCnen-816574775/)                                                                                   | Jan 14, 02:43      |
|       717.65 |            38 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/2-zimmerwohnung-mit-balkon---zu-mieten%21-1772524427/)                                                                                                            | Jan 14, 00:39      |
|       730    |            58 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/helle-ruhige-2-zimmer-wohnung-58m2-zu-vermieten-1629648070/)                                                                                                         | Jan 13, 21:01      |
