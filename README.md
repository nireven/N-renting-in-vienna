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
|       799    |            38 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1-monat-mietfrei:-erstbezug-im-gr%C3%BCnen-nahe-der-u2---zwischen-badeteich-hirschstetten-und-seestadt-2033089937/)                                                | Jan 15, 07:46      |
|       712.31 |            43 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/sehr-gut-gelegene-43m%C2%B2-wohnung---ihr-neues-zuhause-mit-allem-was-sie-brauchen%21-5-minuten-zu-fu%C3%9F-von-der-donauinsel-entfernt-1781341824/)              | Jan 15, 02:09      |
|       650    |            63 |          3 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/gemeinde-wohnung-3-zimmer-%21-1388261264/)                                                                                                                           | Jan 14, 21:15      |
|       790    |            48 |          2 | 23. Liesing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/helle-2-zimmer-wohnung-in-liesing-zu-vermieten%21-999240734/)                                                                                                         | Jan 14, 20:45      |
|       525.49 |            54 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/gemeindewohnung-2-zimmer-1990952480/)                                                                                                                              | Jan 14, 19:34      |
|       787.92 |            41 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/modernes-wohnen-mit-balkon-in-1220-wien---4119m%C2%B2-zum-mietpreis-von-78792-eur%21-1580236359/)                                                                  | Jan 14, 18:35      |
|       782.8  |            52 |          2 | 23. Liesing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/tolle-infrastruktur---bhf-liesing-herbert-mayr-park-fu%C3%9Fdistanz-zum-ekz---wien-wien-1768440990/)                                                                  | Jan 14, 18:16      |
|       720.08 |            50 |          2 | 05. Margareten           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/helle-ruhige-2-zimmer-wohnung-%2A-n%C3%A4he-sch%C3%B6nbrunnerstrasse-/-margaretenstrasse-1704629688/)                                                              | Jan 14, 15:44      |
|       609.93 |            44 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/wohnung-892890212/)                                                                                                                                                 | Jan 14, 14:31      |
|       799    |            43 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-neubauwohnung-inkl.-komplettk%C3%BCche-loggia-und-kellerabteil-bei-u1-neulaa-/hs17-a-14-825042242/)                                                        | Jan 14, 14:00      |
|       759    |            43 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/ruhig-gelegene-2-zimmer-wohnung-inkl-komplettk%C3%BCche-loggia-und-kellerabteil-bei-u1-neulaa---innenhofseitig-/hs17-a-18-1825451538/)                              | Jan 14, 13:51      |
|       712.27 |            34 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/2-zimmer-neubau-in-simmering-1110-wien:-perfekte-lage-nahe-u3%21-1126216033/)                                                                                       | Jan 14, 13:41      |
|       689.06 |            49 |          2 | 13. Hietzing             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1130-hietzing/h%C3%BCgelgasse:-2-zimmer-dachgescho%C3%9Fwohnung-in-gr%C3%BCnlage-1677621748/)                                                                                      | Jan 14, 11:28      |
|       790    |            46 |          2 | 23. Liesing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/wundersch%C3%B6ne-gepflegte-2-zimmer-mit-grossem-balkon%21-789859620/)                                                                                                | Jan 14, 11:23      |
|       750    |            71 |          3 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/gemeindewohnung-direktvergabe-967536679/)                                                                                                                          | Jan 14, 11:13      |
|       750    |            48 |          2 | 08. Josefstadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1080-josefstadt/ideal-f%C3%BCr-singles-studenten-und-p%C3%A4rchen:-zwei-zimmer-wohnung-mitten-im-achten%21-open-house-24.01.2025-von-13:00-16:00-ohne-voranmeldung%21-1188368425/) | Jan 14, 10:38      |
|       717.65 |            38 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/neu%21-erstbezug%21-ideale-2-zimmer-neubauwohnung-mit-balkon%21-tiefgaragenstellpl%C3%A4tze-im-haus%21-1579238205/)                                               | Jan 14, 09:50      |
|       720.88 |            78 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/waaassss%21-721-eur-bruttomiete.-....die-ich-%C3%BCberleg-ich-mir-.....-1395745534/)                                                                | Jan 14, 09:24      |
|       562.31 |            43 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/atelier-:-%29---%3E.-ist-keine-mietwohnung-preiswert-&-aussergew%C3%B6hnlich---56231-eur-bruttomiete-993515347/)                                                    | Jan 14, 09:18      |
|       799    |            39 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1-monat-mietfrei:-erstbezug-im-gr%C3%BCnen-nahe-der-u2---zwischen-badeteich-hirschstetten-und-seestadt-981921692/)                                                 | Jan 14, 09:00      |
