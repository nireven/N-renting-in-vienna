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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District     | Link                                                                                                                                                                                                                                                      | 📅 Published Date   |
|-------------:|--------------:|-----------:|:----------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       799.01 |            47 |          2 | 10. Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-dachgeschoss-wohnung-in-top-lage---10.bezirk.---wohntraum-1706949546/)                                                                                      | Nov 26, 13:49      |
|       750    |            46 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/helle-freundliche-2-zimmer-wohnung-nahe-der-donauinsel-1234991560/)                                                                                                | Nov 26, 13:17      |
|       799    |            40 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/moderne-2-zimmerwohnung-mit-balkon%21-1155042286/)                                                                                                                 | Nov 26, 12:57      |
|       485.72 |            37 |          2 | 10. Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/frisch-renoviert%21-1325416817/)                                                                                                                                     | Nov 26, 12:46      |
|       770    |            47 |          2 | 10. Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-wohnung-mit-balkon-im-viola-park-1841570745/)                                                                                                               | Nov 26, 12:00      |
|       700    |            50 |          2 | 07. Neubau      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1070-neubau/zwischenmiete-in-wien-1190099783/)                                                                                                                                      | Nov 26, 10:47      |
|       790.15 |            59 |          2 | 10. Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-wohnung---provisionsfrei-1611971446/)                                                                                                                       | Nov 26, 10:39      |
|       799    |            39 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1-monat-mietfrei:-erstbezug-im-gr%C3%BCnen-nahe-der-u2---zwischen-badeteich-hirschstetten-und-seestadt-1143083651/)                                                 | Nov 26, 10:10      |
|       780.27 |            35 |          2 | 20. Brigittenau | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1200-brigittenau/gem%C3%BCtliche-gartenwohnung-mit-praktischen-grundriss-n%C3%A4he-u6-j%C3%A4gerstra%C3%9Fe-und-dresdner-stra%C3%9Fe-1030082805/)                                   | Nov 26, 09:16      |
|       799    |            39 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1-monat-mietfrei:-erstbezug-im-gr%C3%BCnen-nahe-der-u2---zwischen-badeteich-hirschstetten-und-seestadt-981921692/)                                                  | Nov 26, 09:00      |
|       580    |            55 |          2 | 10. Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/wiener-wohnen-gemeinde-1442608621/)                                                                                                                                  | Nov 26, 08:13      |
|       749    |            46 |          2 | 23. Liesing     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/ruhige-25-zimmerwohnung-in-guter-lage-%7C-zellmann-immobilien-2017122355/)                                                                                             | Nov 26, 07:35      |
|       595    |            45 |          2 | 18. Währing     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1180-w%C3%A4hring/studentenapartment-%28nur-f%C3%BCr-studenten-die-auf-der-universit%C3%A4t-studieren%29---sofortbezug---hofseitig---alles-inklusive%21-n%C3%A4here-akh-812850915/) | Nov 25, 22:55      |
|       725    |            40 |          2 | 12. Meidling    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/neubau-ab-01.02.-beziehbar:-sch%C3%B6ne-2-zimmerwohnung-mit-loggia-im-3.-og-2055199338/)                                                                              | Nov 25, 19:32      |
|       692.33 |            39 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/gepflegte-studentenwohnungen-mit-einbauk%C3%BCche-in-1210-zu-mieten-1317724224/)                                                                                   | Nov 25, 17:21      |
|       799    |            42 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/moderne-2-zimmer-wohnung-in-floridsdorf:-nachhaltigkeit-trifft-wohnkomfort-1934904306/)                                                                            | Nov 25, 17:18      |
|       799    |            42 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/42m%C2%B2-wohlf%C3%BChlwohnung-in-gr%C3%BCnruhelage:-fu%C3%9Fbodenheizung-&-erdw%C3%A4rme-inklusive-788032770/)                                                    | Nov 25, 17:18      |
|       739    |            47 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/1210-wien---attraktive-dachgeschoss-neubauwohnung-mit-sensationeller-terrasse-und-komplettk%C3%BCche---ab-1.1.2025-814717675/)                                     | Nov 25, 17:01      |
|       742.17 |            41 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/gepflegte-studentenwohnungen-mit-einbauk%C3%BCche-in-1210-zu-mieten-1764666987/)                                                                                   | Nov 25, 16:51      |
|       745    |            42 |          2 | 16. Ottakring   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/%2Aprovisionsfrei%2A-sch%C3%B6ne-lichtdurchflutete-2-zimmer-wohnung-1569081927/)                                                                                     | Nov 25, 16:51      |
