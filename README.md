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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       699.94 |            48 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/2-zimmer-in-floridsdorf-zu-vermieten-1118328844/)                                                            | Dec 06, 12:07      |
|       700    |            40 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/2-zimmerwohnung-2142876084/)                                                                   | Dec 06, 11:48      |
|       524.6  |            51 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/gemeindewohnung---wohnticket-30.09.2024-%7C-2-zimmer-2063886803/)                                                | Dec 06, 11:47      |
|       530    |            49 |          2 | 02. Leopoldstadt         | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/2-zimmer-gemeinde-wohnung-im-2.-bezirk-%28engerthstra%C3%9Fe-179-183%29-1615377569/)                        | Dec 06, 11:46      |
|       730    |            42 |          2 | 23. Liesing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/basler-gasse---neubau-erstbez%C3%BCge-mit-garage-in-1230-wien-1884672930/)                                       | Dec 06, 11:30      |
|       745    |            56 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/%2Aprovisionsfrei%2A-sehr-helle-und-sch%C3%B6ne-2-zimmer-wohnung-856985124/)                   | Dec 06, 11:26      |
|       799    |            42 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/komfortabler-erstbezug:-2-zimmer-wohnungen-im-21.-bezirk-mit-balkon-und-moderner-k%C3%BCche-1151352378/)     | Dec 06, 10:49      |
|       684.45 |            44 |          2 | 02. Leopoldstadt         | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/ruhelage-15-zimmer-u1/-u2-wu-n%C3%A4he-1386665170/)                                                         | Dec 06, 09:42      |
|       667.7  |            47 |          2 | 23. Liesing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/helle-und-ruhige-2-zimmer-wohnung-%7C-zellmann-immobilien-2012782510/)                                           | Dec 06, 07:24      |
|       731.33 |            72 |          3 | 02. Leopoldstadt         | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/gemeindewohnung-1020-wien---direktvergabe-961976560/)                                                       | Dec 06, 07:20      |
|       678.83 |            49 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/gem%C3%BCtliche-2-zimmer-wohnung-im-3.-og-2009648704/)                                                         | Dec 06, 02:49      |
|       767    |            76 |          3 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/gemeindewohnung-3-zimmer-direktvergabe-mit-balkon-1509367952/)                                                | Dec 05, 23:12      |
|       407    |            40 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/gemeindewohnung-2107619867/)                                                                                    | Dec 05, 22:14      |
|       585    |            55 |          3 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/direktvergabe-gemeindewochnung-1750396960/)                                                    | Dec 05, 22:09      |
|       745.9  |            54 |          3 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/provisionsfrei:-unbefristeter-54m%C2%B2-altbau-mit-3-zimmern-n%C3%A4he-wilhelminenberg---1160-wien-825803108/) | Dec 05, 18:46      |
|       750    |            35 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/360-tour-//-balkonwohnung-am-wienerberg-1952506663/)                                                            | Dec 05, 17:37      |
|       600.5  |            57 |          2 | 23. Liesing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/nette-gemeindewohnung-direktvergabe-1230-wien-vorkmerkschein-bis-zum-30.09.2024oder-davor-1077804643/)           | Dec 05, 17:13      |
|       456    |            44 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/direktvergabe-2-zimmer-gemeinde-wohnung-925786459/)                                                            | Dec 05, 17:13      |
|       747.87 |            50 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/zentrale-&-ruhige-wohnung-nahe-rochusmarkt-&-wien-mitte-2015881814/)                                     | Dec 05, 16:52      |
|       530    |            39 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/1140-wien---kompakte-2-zimmer-wohnung-unbefristet-1937087101/)                                                   | Dec 05, 16:51      |
