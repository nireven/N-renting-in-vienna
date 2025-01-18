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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District    | Link                                                                                                                                                                                                                                       | 📅 Published Date   |
|-------------:|--------------:|-----------:|:---------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       545    |            57 |          2 | 23. Liesing    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/gemeindewohnung-1230-5690-m%C2%B2-1034212679/)                                                                                                          | Jan 18, 11:48      |
|       799    |            39 |          2 | 22. Donaustadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1.-monat-mietfrei-bei-anmietung-ab-01.02.2025%21---exklusiver-erstbezug-im-gr%C3%BCnen---n%C3%A4he-badeteich-hirschstetten-und-seestadt-1928809618/) | Jan 18, 10:32      |
|       799    |            39 |          2 | 22. Donaustadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1.-monat-mietfrei-bei-anmietung-ab-01.02.2025%21---exklusiver-erstbezug-im-gr%C3%BCnen---n%C3%A4he-badeteich-hirschstetten-und-seestadt-1183927191/) | Jan 18, 10:32      |
|       799    |            39 |          2 | 22. Donaustadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1.-monat-mietfrei-bei-anmietung-ab-01.02.2025%21---exklusiver-erstbezug-im-gr%C3%BCnen---n%C3%A4he-badeteich-hirschstetten-und-seestadt-1536756296/) | Jan 18, 10:32      |
|       799    |            39 |          2 | 22. Donaustadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1.-monat-mietfrei-bei-anmietung-ab-01.02.2025%21---exklusiver-erstbezug-im-gr%C3%BCnen---n%C3%A4he-badeteich-hirschstetten-und-seestadt-872917532/)  | Jan 18, 10:32      |
|       799    |            39 |          2 | 22. Donaustadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1.-monat-mietfrei-bei-anmietung-ab-01.02.2025%21---exklusiver-erstbezug-im-gr%C3%BCnen---n%C3%A4he-badeteich-hirschstetten-und-seestadt-1610205268/) | Jan 18, 10:32      |
|       799    |            39 |          2 | 22. Donaustadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1.-monat-mietfrei-bei-anmietung-ab-01.02.2025%21---exklusiver-erstbezug-im-gr%C3%BCnen---n%C3%A4he-badeteich-hirschstetten-und-seestadt-1257301064/) | Jan 18, 10:31      |
|       799    |            39 |          2 | 22. Donaustadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1.-monat-mietfrei-bei-anmietung-ab-01.02.2025%21---exklusiver-erstbezug-im-gr%C3%BCnen---n%C3%A4he-badeteich-hirschstetten-und-seestadt-1120135051/) | Jan 18, 10:31      |
|       799    |            38 |          2 | 22. Donaustadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1.-monat-mietfrei-bei-anmietung-ab-01.02.2025%21---exklusiver-erstbezug-im-gr%C3%BCnen---n%C3%A4he-badeteich-hirschstetten-und-seestadt-2061795170/) | Jan 18, 10:31      |
|       799    |            39 |          2 | 22. Donaustadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1.-monat-mietfrei-bei-anmietung-ab-01.02.2025%21---exklusiver-erstbezug-im-gr%C3%BCnen---n%C3%A4he-badeteich-hirschstetten-und-seestadt-1375745267/) | Jan 18, 10:31      |
|       799    |            39 |          2 | 22. Donaustadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1.-monat-mietfrei-bei-anmietung-ab-01.02.2025%21---exklusiver-erstbezug-im-gr%C3%BCnen---n%C3%A4he-badeteich-hirschstetten-und-seestadt-1100819372/) | Jan 18, 10:31      |
|       657    |            48 |          2 | 14. Penzing    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/%28reserviert%29-altbau---ruhelage-1207102490/)                                                                                                         | Jan 18, 09:28      |
|       731    |            40 |          2 | 22. Donaustadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/%28reserviert%29-mietwohnung-zu-vergeben-1461129490/)                                                                                                | Jan 18, 09:09      |
|       734.59 |            37 |          2 | 22. Donaustadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/2-zimmer-wohnung-neubau-mit-2-terrassen-zu-vermieten-958266323/)                                                                                     | Jan 18, 08:46      |
|       799    |            39 |          2 | 22. Donaustadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1-monat-mietfrei:-erstbezug-im-gr%C3%BCnen-nahe-der-u2---zwischen-badeteich-hirschstetten-und-seestadt-1305948891/)                                  | Jan 18, 08:02      |
|       799    |            39 |          2 | 22. Donaustadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1-monat-mietfrei:-erstbezug-im-gr%C3%BCnen-nahe-der-u2---zwischen-badeteich-hirschstetten-und-seestadt-1390704747/)                                  | Jan 18, 07:54      |
|       740    |            51 |          2 | 13. Hietzing   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1130-hietzing/2-zimmer-mit-wohnk%C3%BCche-1091791087/)                                                                                                               | Jan 18, 07:32      |
|       752.36 |            54 |          2 | 18. Währing    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1180-w%C3%A4hring/ger%C3%A4umige-2-zimmer--wohnung-1073175621/)                                                                                                      | Jan 18, 02:45      |
|       450    |            43 |          2 | 22. Donaustadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/direktvergabe-2-zimmer-wohnung-mit-wohnticket-bis-31.01.2025-1568408949/)                                                                            | Jan 17, 22:34      |
|       530.87 |            52 |          2 | 16. Ottakring  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/g%C3%BCnstig-und-charmant-in-wien---studenten-p%C3%A4rchen-single-1826750384/)                                                                        | Jan 17, 20:59      |
