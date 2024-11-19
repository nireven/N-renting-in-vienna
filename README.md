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
|       691.33 |            44 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/%28reserviert%29-neubauwohnung-zu-vermieten%21-1644760517/)                                                                                                                | Nov 19, 23:11      |
|       693    |            65 |          2 | 11. Simmering   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/direktvergabe---wiener-wohnticket-bis-30.09.2024-erforderlich%21-865968237/)                                                                                                 | Nov 19, 20:56      |
|       640    |            72 |          2 | 12. Meidling    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/helle-dachgeschosswohnung-1573792139/)                                                                                                                                        | Nov 19, 20:36      |
|       730    |            63 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/nachmieter-gesucht-1037959595/)                                                                                                                                            | Nov 19, 20:12      |
|       787.92 |            41 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/modernes-wohnen-mit-balkon-in-1220-wien---4119m%C2%B2-zum-mietpreis-von-78792-eur%21-1580236359/)                                                                           | Nov 19, 18:35      |
|       730    |            65 |          2 | 05. Margareten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/6517-qm---730-eur-sehr-angenehme-lage-l%C3%A4ssig-lebenswert-eingeteilt-1295129380/)                                                                                        | Nov 19, 18:19      |
|       715    |            43 |          2 | 06. Mariahilf   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1060-mariahilf/15-zimmer-altbaumiete---unbefristet---ideal-f%C3%BCr-singles-1669383427/)                                                                                                    | Nov 19, 17:55      |
|       790    |            45 |          2 | 05. Margareten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/provisionsfrei-spengergasse-moderne-neu-renovierte-2-zimmer-wohnung-887207224/)                                                                                             | Nov 19, 16:21      |
|       500    |            63 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/2-zimmer-gemeindewohnung---direktvergabe-1210-wien-974408444/)                                                                                                             | Nov 19, 16:01      |
|       790    |            41 |          2 | 23. Liesing     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/top-2-zimmer-s%C3%BCd-balkonwohnung-in-ruhiger-gr%C3%BCnlage-1479201196/)                                                                                                      | Nov 19, 15:56      |
|       592    |            44 |          2 | 14. Penzing     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/singlewohnung-hauptmiete-unbefristet-mit-k%C3%BCche-ruhige-wohnlage-1701044569/)                                                                                               | Nov 19, 15:36      |
|       714.98 |            49 |          2 | 14. Penzing     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/provisionsfrei:-unbefristeter-49m%C2%B2-altbau-mit-2-zimmern-und-lift---1140-wien-1204147756/)                                                                                 | Nov 19, 15:26      |
|       680    |            34 |          2 | 14. Penzing     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/smarte-zwei-zimmerwohnung-in-penzing-mit-balkon-1430425795/)                                                                                                                   | Nov 19, 15:07      |
|       650    |            41 |          2 | 18. Währing     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1180-w%C3%A4hring/entz%C3%BCckende-15-zimmer-wohnung-in-gersthof-1397452479/)                                                                                                               | Nov 19, 15:00      |
|       765.37 |            45 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/tolle-2-zimmer-wohnung-mit-idealer-raumaufteilung-in-guter-und-infrastrukturell-ansprechender-lage%21-1791769254/)                                                         | Nov 19, 14:18      |
|       599.83 |            41 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/2-zimmer-wohnung-zu-vermieten-1629360803/)                                                                                                                                 | Nov 19, 14:11      |
|       749    |            36 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/1210-wien---ruhige-neuwertige-2-zimmer-singlewohnung-mit-aussicht-2139163726/)                                                                                             | Nov 19, 14:01      |
|       798.88 |            41 |          2 | 10. Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/sonnwend-living%21-inklusive-k%C3%BCche%21-erstbezug%21-elektrische-raffstores%21-klima-vorb.%21-n%C3%A4he-u1.---wohntraum-774645004/)                                       | Nov 19, 13:49      |
|       799.01 |            47 |          2 | 10. Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-dachgeschoss-wohnung-in-top-lage---10.bezirk.---wohntraum-1706949546/)                                                                                              | Nov 19, 13:49      |
|       799    |            38 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/leo-131---hochwertiger-neubau-zu-fairen-preisen---gut-angebunden-%28u1-leopoldau-%2B-u6-floridsdorf%29---mit-vollm%C3%B6blierter-k%C3%BCche-&-freifl%C3%A4che-1572554877/) | Nov 19, 13:48      |
