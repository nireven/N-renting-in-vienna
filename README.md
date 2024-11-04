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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District     | Link                                                                                                                                                                                                                                       | 📅 Published Date   |
|-------------:|--------------:|-----------:|:----------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       798.11 |            44 |          2 | 16. Ottakring   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/attraktive-und-sch%C3%B6ne-2-zimmer-wohnung-in-der-r%C3%B6mergasse%21-1680208443/)                                                                    | Nov 04, 17:17      |
|       618    |            55 |          2 | 12. Meidling    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/wundersch%C3%B6ne-2-zimmer-wohnung-ab-01.12.-verf%C3%BCgbar-1029525485/)                                                                               | Nov 04, 17:12      |
|       742.17 |            41 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/gepflegte-studentenwohnungen-mit-einbauk%C3%BCche-in-1210-zu-mieten-1764666987/)                                                                    | Nov 04, 16:51      |
|       775    |            42 |          2 | 16. Ottakring   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/%2Aprovisionsfrei%2A-sch%C3%B6ne-lichtdurchflutete-2-zimmer-wohnung-1569081927/)                                                                      | Nov 04, 16:51      |
|       780.3  |            35 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/singlehit-in-1210-wien-zu-mieten-1946913358/)                                                                                                       | Nov 04, 16:35      |
|       591.36 |            64 |          2 | 10. Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/helle-gemeindewohnung-n%C3%A4he-oberlaa-2-zimmer-und-balkon-851498696/)                                                                               | Nov 04, 16:21      |
|       708.78 |            72 |          3 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/helle-3-zimmerwohnung-in-stadlau--n%C3%A4he-u2-hardeggasse-874772596/)                                                                               | Nov 04, 16:17      |
|       748.52 |            45 |          2 | 17. Hernals     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/zweitbezug-nach-generalsanierung-top-ausgestattete-2-zimmerwohnung-44m%C2%B2-n%C3%A4he-elterleinplatz-1714340348/)                                      | Nov 04, 15:57      |
|       698    |            65 |          2 | 12. Meidling    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/direktvergabe-gemeindewohnung-zu-vergeben-2028574869/)                                                                                                 | Nov 04, 15:45      |
|       699.99 |            41 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/2-zimmer-neubauwohnung-inkl.-komplettk%C3%BCche-balkon-au%C3%9Fenfl%C3%A4che-und-kellerabteil---badeteich-vor-der-t%C3%BCre/zs64-44-og3-1826221582/) | Nov 04, 14:10      |
|       761.99 |            43 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/2-zimmer-neubauwohnung-inkl.-komplettk%C3%BCche-balkon-au%C3%9Fenfl%C3%A4che-und-kellerabteil-/-i3-30-1802107066/)                                   | Nov 04, 14:10      |
|       749    |            42 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/2-zimmer-neubauwohnung-inkl.-komplettk%C3%BCche-loggia-au%C3%9Fenfl%C3%A4che-und-kellerabteil-/-alf52-top-1-22-2002366737/)                          | Nov 04, 14:10      |
|       659.99 |            40 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/2-zimmer-neubauwohnung-inkl.-k%C3%BCche-balkon-au%C3%9Fenfl%C3%A4che-und-kellerabteil-/-sp64-top-2-31-1664768233/)                                   | Nov 04, 14:10      |
|       769    |            40 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1220-wien---kirschbl%C3%BCtenpark---u1-n%C3%A4he---hofseitige-gepflegte-balkonwohnung---ab-1.02.2025-1348008516/)                                    | Nov 04, 14:00      |
|       749    |            44 |          2 | 10. Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/1100-wien---hofseitige-neubauwohnung---u1-n%C3%A4he-keplerplatz-804318935/)                                                                           | Nov 04, 14:00      |
|       761.09 |            67 |          2 | 10. Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/sch%C3%B6ne-zwei-zimmer-wohnung-in-der-gudrunstrasse-%21-2029920278/)                                                                                 | Nov 04, 13:07      |
|       729    |            50 |          2 | 18. Währing     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1180-w%C3%A4hring/altbauwohnung-in-topausstattung-1893547543/)                                                                                                       | Nov 04, 12:58      |
|       772.75 |            48 |          2 | 23. Liesing     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/ruhige-2-zimmer-wohnung-mit-loggia---nahe-bahnhof-liesing-1829891489/)                                                                                  | Nov 04, 12:54      |
|       789    |            41 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/moderne-neubauwohnungen-nahe-u1-kagraner-platz---aufstrebendes-wohnviertel-991040077/)                                                               | Nov 04, 11:58      |
|       550    |            51 |          2 | 11. Simmering   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/direktvergabe-2-zimmer-gemeindewohnung-1680972474/)                                                                                                   | Nov 04, 11:55      |
