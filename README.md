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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District     | Link                                                                                                                                                                                                                                    | 📅 Published Date   |
|-------------:|--------------:|-----------:|:----------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       848    |            43 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/%7C-2-zimmer-%7C-ab-september-%7C-nachvermietung-%7C-nordwestlich-%7C-balkon-%7C-an-der-alten-donau-%7C-donaustadtbr%C3%BCcke-916358290/)         | May 20, 20:39      |
|       830    |            68 |          2 | 12. Meidling    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/u4/u6-l%C3%A4ngenfeldgasse---2-zimmer-wohnung-zur-vermietung-1633237659/)                                                                           | May 20, 20:34      |
|       673    |            52 |          2 | 23. Liesing     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/mietwohnung-52m%C2%B2---zwei-zimmer---naherholung-liesingbach-1709293417/)                                                                           | May 20, 20:26      |
|       412    |            52 |          2 | 23. Liesing     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/direktvergabe-gemeindebauwohnung-2045526229/)                                                                                                        | May 20, 19:56      |
|       889.15 |            42 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/moderne-2-zimmer-wohnung-in-1220-wien---stadlau-%7C-balkon-&-top-anbindung%21-1157852095/)                                                        | May 20, 18:20      |
|       886    |            51 |          2 | 16. Ottakring   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/2-zimmer-wohnung-im-16.-bezirk-in-ruhiger-lage-sowie-zentrumnah-1174305286/)                                                                       | May 20, 17:33      |
|       865    |            46 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/moderne-neubauwohnung-mit-innenhof-balkon-und-abstellraum-nahe-s-bahn-jedlersdorf-stra%C3%9Fenbahn-26-und-scn%21-1694025998/)                    | May 20, 17:26      |
|       790    |            44 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/charmante-2-zimmer-wohnung-mit-freifl%C3%A4che-in-ruhiger-lage---ab-01.08.2025%21-1100301109/)                                                    | May 20, 17:25      |
|       789.93 |            44 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/pog-81---hochwertige-ausstattung-ruhelage-nahe-kagraner-platz-und-top-grundriss%21-ab-august-2025---jetzt-anfragen-1424305801/)                   | May 20, 16:47      |
|       750    |            57 |          2 | 17. Hernals     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/erstbezug---sanierte-2-zimmer-wohnung-mit-separater-k%C3%BCche-und-kellerabteil-im-1.-stock-ohne-lift---n%C3%A4he-lidlpark---unbefristet-947146560/) | May 20, 15:56      |
|       719    |            38 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/ab-01.06.2025---genochplatz---kompakte-singlewohnung-mit-loggia-im-7.stock-1691822508/)                                                           | May 20, 15:33      |
|       885    |            31 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/musicflats---wohnen-wo-musik-entsteht---n%C3%A4he-u1-station-neue-donau-1033840439/)                                                              | May 20, 15:19      |
|       885    |            31 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/musicflats---wohnen-wo-musik-entsteht---n%C3%A4he-u1-station-neue-donau-1702275209/)                                                              | May 20, 15:00      |
|       885    |            30 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/musicflats---wohnen-wo-musik-entsteht---n%C3%A4he-u1-station-neue-donau-1720691876/)                                                              | May 20, 15:00      |
|       770    |           nan |          2 | 03. Landstraße  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/wohnen-im-zentrum---mit-blick-zum-%22schweizergarten%22-1310582384/)                                                                         | May 20, 14:58      |
|       890    |            55 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/2-zimmer-wohnung-mit-7-m%C2%B2-hofseitigem-balkon-802042661/)                                                                                    | May 20, 14:57      |
|       849    |            43 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/moderne-2-zi-wohnung-mit-balkon-provisionsfrei---nahe-u1-2065737265/)                                                                             | May 20, 14:33      |
|       889    |            45 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/moderne-2-zi-wohnung-mit-balkon-provisionsfrei---nahe-u1-1039812629/)                                                                             | May 20, 14:33      |
|       849    |            42 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/moderne-2-zi-wohnung-mit-balkon-provisionsfrei---nahe-u1-1259780440/)                                                                             | May 20, 14:33      |
|       880.54 |            42 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/moderne-2-zi-wohnung-mit-garten-provisionsfrei---nahe-u1-1146838011/)                                                                             | May 20, 14:33      |
