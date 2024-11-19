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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                                                              | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       592    |            44 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/singlewohnung-hauptmiete-unbefristet-mit-k%C3%BCche-ruhige-wohnlage-1701044569/)                                                                                               | Nov 19, 15:36      |
|       714.98 |            49 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/provisionsfrei:-unbefristeter-49m%C2%B2-altbau-mit-2-zimmern-und-lift---1140-wien-1204147756/)                                                                                 | Nov 19, 15:26      |
|       570.02 |            51 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/2-zimmer-wohnung-mit-fernblick%21-1663351407/)                                                                                                               | Nov 19, 15:26      |
|       740.01 |            73 |          2 | 05. Margareten           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/gro%C3%9Fz%C3%BCgige-2-zimmer-wohnung-in-gepflegtem-haus-beim-hauptbahnhof-1294851587/)                                                                                     | Nov 19, 15:26      |
|       680    |            34 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/smarte-zwei-zimmerwohnung-in-penzing-mit-balkon-1430425795/)                                                                                                                   | Nov 19, 15:07      |
|       650    |            41 |          2 | 18. Währing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1180-w%C3%A4hring/entz%C3%BCckende-15-zimmer-wohnung-in-gersthof-1397452479/)                                                                                                               | Nov 19, 15:00      |
|       765.37 |            45 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/tolle-2-zimmer-wohnung-mit-idealer-raumaufteilung-in-guter-und-infrastrukturell-ansprechender-lage%21-1791769254/)                                                         | Nov 19, 14:18      |
|       599.83 |            41 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/2-zimmer-wohnung-zu-vermieten-1629360803/)                                                                                                                                 | Nov 19, 14:11      |
|       749    |            36 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/1210-wien---ruhige-neuwertige-2-zimmer-singlewohnung-mit-aussicht-2139163726/)                                                                                             | Nov 19, 14:01      |
|       799.01 |            47 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-dachgeschoss-wohnung-in-top-lage---10.bezirk.---wohntraum-1706949546/)                                                                                              | Nov 19, 13:49      |
|       798.88 |            41 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/sonnwend-living%21-inklusive-k%C3%BCche%21-erstbezug%21-elektrische-raffstores%21-klima-vorb.%21-n%C3%A4he-u1.---wohntraum-774645004/)                                       | Nov 19, 13:49      |
|       799    |            38 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/leo-131---hochwertiger-neubau-zu-fairen-preisen---gut-angebunden-%28u1-leopoldau-%2B-u6-floridsdorf%29---mit-vollm%C3%B6blierter-k%C3%BCche-&-freifl%C3%A4che-1572554877/) | Nov 19, 13:48      |
|       754.86 |            43 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/ina---wohnanlage-am-leberberg-:-top-a3-13-1170112708/)                                                                                                                       | Nov 19, 12:38      |
|       798.34 |            47 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/ina---wohnanlage-am-leberberg-:-top-a2-29-1500197418/)                                                                                                                       | Nov 19, 12:27      |
|       748.62 |            40 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/ina---wohnanlage-am-leberberg-:-top-a2-18-1851487966/)                                                                                                                       | Nov 19, 12:08      |
|       769.07 |            44 |          2 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/wohnung-mit-grosser-wohnk%C3%BCche-zu-mieten%21-878432123/)                                                                                                                    | Nov 19, 12:08      |
|       755.72 |            43 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/ina---wohnanlage-am-leberberg-:-top-a2-05-2146745975/)                                                                                                                       | Nov 19, 12:08      |
|       790    |            49 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-wohnung-mit-balkon-im-viola-park-874541985/)                                                                                                                        | Nov 19, 12:02      |
|       770    |            47 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-wohnung-mit-balkon-im-viola-park-1841570745/)                                                                                                                       | Nov 19, 12:00      |
|       799    |            43 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/wien---1220---31m%C2%B2-terrassentraum---u1-n%C3%A4he-kagranerplatz---neubau---ab-15.12.2024-1927445904/)                                                                   | Nov 19, 11:03      |
