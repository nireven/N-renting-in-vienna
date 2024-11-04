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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District     | Link                                                                                                                                                                                                                                                          | 📅 Published Date   |
|-------------:|--------------:|-----------:|:----------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       506.34 |            39 |          2 | 20. Brigittenau | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1200-brigittenau/u6-j%C3%A4gerstra%C3%9Fe---2-zimmer-altbau-im-2.-stock-1711371201/)                                                                                                    | Nov 04, 14:28      |
|       749    |            42 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/2-zimmer-neubauwohnung-inkl.-komplettk%C3%BCche-loggia-au%C3%9Fenfl%C3%A4che-und-kellerabteil-/-alf52-top-1-22-2002366737/)                                             | Nov 04, 14:10      |
|       659.99 |            40 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/2-zimmer-neubauwohnung-inkl.-k%C3%BCche-balkon-au%C3%9Fenfl%C3%A4che-und-kellerabteil-/-sp64-top-2-31-1664768233/)                                                      | Nov 04, 14:10      |
|       761.99 |            43 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/2-zimmer-neubauwohnung-inkl.-komplettk%C3%BCche-balkon-au%C3%9Fenfl%C3%A4che-und-kellerabteil-/-i3-30-1802107066/)                                                      | Nov 04, 14:10      |
|       699.99 |            41 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/2-zimmer-neubauwohnung-inkl.-komplettk%C3%BCche-balkon-au%C3%9Fenfl%C3%A4che-und-kellerabteil---badeteich-vor-der-t%C3%BCre/zs64-44-og3-1826221582/)                    | Nov 04, 14:10      |
|       749    |            44 |          2 | 10. Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/1100-wien---hofseitige-neubauwohnung---u1-n%C3%A4he-keplerplatz-804318935/)                                                                                              | Nov 04, 14:00      |
|       769    |            40 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1220-wien---kirschbl%C3%BCtenpark---u1-n%C3%A4he---hofseitige-gepflegte-balkonwohnung---ab-1.02.2025-1348008516/)                                                       | Nov 04, 14:00      |
|       761.09 |            67 |          2 | 10. Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/sch%C3%B6ne-zwei-zimmer-wohnung-in-der-gudrunstrasse-%21-2029920278/)                                                                                                    | Nov 04, 13:07      |
|       729    |            50 |          2 | 18. Währing     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1180-w%C3%A4hring/altbauwohnung-in-topausstattung-1893547543/)                                                                                                                          | Nov 04, 12:58      |
|       772.75 |            48 |          2 | 23. Liesing     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/ruhige-2-zimmer-wohnung-mit-loggia---nahe-bahnhof-liesing-1829891489/)                                                                                                     | Nov 04, 12:54      |
|       777    |            44 |          2 | 11. Simmering   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/freundliche-und-moderne-2-zimmer-wohnung-mit-gro%C3%9Fem-hofseitigem-balkon-nahe-u3-simmering-/-ab-1.1.25-verf%C3%BCgbar.-1461778021/)                                   | Nov 04, 12:27      |
|       789    |            41 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/moderne-neubauwohnungen-nahe-u1-kagraner-platz---aufstrebendes-wohnviertel-991040077/)                                                                                  | Nov 04, 11:58      |
|       550    |            51 |          2 | 11. Simmering   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/direktvergabe-2-zimmer-gemeindewohnung-1680972474/)                                                                                                                      | Nov 04, 11:55      |
|       495    |            43 |          2 | 05. Margareten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/gemeindewohnung-direktvergabe:-letztmaliges-angebot:-abl%C3%B6se-%E2%82%AC-1500-f%C3%BCr-m%C3%B6blierte-43m2-wohnung-1163696543/)                                       | Nov 04, 11:50      |
|       798.58 |            45 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/leo-131---sonnige-neubauwohnung-mit-s%C3%BCdbalkon-und-k%C3%BCche---10-minuten-zu-u6-und-s-bahn-floridsdorf-sowie-siemensstra%C3%9Fe-bahnhof.---wohntraum-1042336912/) | Nov 04, 11:19      |
|       730    |            42 |          2 | 23. Liesing     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/basler-gasse---neubau-erstbez%C3%BCge-mit-garage-in-1230-wien-1215481577/)                                                                                                 | Nov 04, 11:19      |
|       649    |            33 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1220-wien---fernblick---attraktive-kleinwohnung-im-dachgescho%C3%9F-----ab-1.12.2024-1329071562/)                                                                       | Nov 04, 11:05      |
|       695    |            39 |          2 | 10. Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/wundersch%C3%B6ne-2-zimmer-wohnung-in-top-lage-1590133781/)                                                                                                              | Nov 04, 11:03      |
|       674.43 |            34 |          2 | 11. Simmering   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/2-zimmer-terrassenwohnung-in-n%C3%A4he-des-flughafens%21-814789913/)                                                                                                     | Nov 04, 10:58      |
|       746.09 |            44 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/moderne-2-zimmerwohnung---nahe-der-alten-donau-953832565/)                                                                                                             | Nov 04, 10:37      |
