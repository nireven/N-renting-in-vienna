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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                                                                                          | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       799    |            39 |          2 | 22. Donaustadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1-monat-mietfrei:-erstbezug-im-gr%C3%BCnen-nahe-der-u2---zwischen-badeteich-hirschstetten-und-seestadt-2131104915/)                                                     | Jan 31, 17:35      |
|       799    |            39 |          2 | 22. Donaustadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1-monat-mietfrei:-erstbezug-im-gr%C3%BCnen-nahe-der-u2---zwischen-badeteich-hirschstetten-und-seestadt-813297785/)                                                      | Jan 31, 17:25      |
|       799    |            39 |          2 | 22. Donaustadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1-monat-mietfrei:-erstbezug-im-gr%C3%BCnen-nahe-der-u2---zwischen-badeteich-hirschstetten-und-seestadt-1426066826/)                                                     | Jan 31, 17:17      |
|       799    |            39 |          2 | 22. Donaustadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1-monat-mietfrei:-erstbezug-im-gr%C3%BCnen-nahe-der-u2---zwischen-badeteich-hirschstetten-und-seestadt-1630202996/)                                                     | Jan 31, 17:15      |
|       799    |            39 |          2 | 22. Donaustadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1-monat-mietfrei:-erstbezug-im-gr%C3%BCnen-nahe-der-u2---zwischen-badeteich-hirschstetten-und-seestadt-1553680659/)                                                     | Jan 31, 17:13      |
|       799    |            39 |          2 | 22. Donaustadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1-monat-mietfrei:-erstbezug-im-gr%C3%BCnen-nahe-der-u2---zwischen-badeteich-hirschstetten-und-seestadt-1068440575/)                                                     | Jan 31, 17:11      |
|       770    |            49 |          2 | 21. Floridsdorf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/stammersdorfer-wohnparadies:-mietwohnungen-mit-kaufoption-737459071/)                                                                                                  | Jan 31, 14:38      |
|       798    |            46 |          2 | 21. Floridsdorf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/traumhafte-wohnung-mit-gro%C3%9Fz%C3%BCgiger-freifl%C3%A4che%21-1159451458/)                                                                                           | Jan 31, 13:47      |
|       799    |            40 |          2 | 22. Donaustadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/2-zimmer-neubauwohnung-inkl.-komplettk%C3%BCche-balkon-au%C3%9Fenfl%C3%A4che-und-kellerabteil/-sp64-top-5-64-913298614/)                                                | Jan 31, 13:19      |
|       750    |            45 |          2 | 18. Währing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1180-w%C3%A4hring/charmante-2-zimmer-wohnung-in-1180-wien-1877927501/)                                                                                                                  | Jan 31, 12:37      |
|       799    |            39 |          2 | 22. Donaustadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1-monat-mietfrei:-erstbezug-im-gr%C3%BCnen-nahe-der-u2---zwischen-badeteich-hirschstetten-und-seestadt-1193457345/)                                                     | Jan 31, 12:19      |
|       799.5  |            44 |          2 | 13. Hietzing     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1130-hietzing/hell-und-stilvoll-wohnen---charmante-2-zimmer-wohnung-in-hietzing---1820138740/)                                                                                          | Jan 31, 12:01      |
|       799    |            39 |          2 | 22. Donaustadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1-monat-mietfrei:-erstbezug-im-gr%C3%BCnen-nahe-der-u2---zwischen-badeteich-hirschstetten-und-seestadt-807881379/)                                                      | Jan 31, 11:46      |
|       799.34 |            37 |          2 | 20. Brigittenau  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1200-brigittenau/kompakte-neubau-gartenwohnung-in-direkter-nahe-zur-u6-und-s-bahn-handelskai-sowie-millennium-city%21-ab-mai-2025%21---jetzt-zuschlagen-2038820083/)                    | Jan 31, 11:20      |
|       629    |            50 |          2 | 20. Brigittenau  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1200-brigittenau/moderne-2-zimmerwohnung-neben-u-bahn-1269054020/)                                                                                                                      | Jan 31, 11:03      |
|       799    |            45 |          2 | 22. Donaustadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/2-zimmer-neubauwohnung-inkl.-komplettk%C3%BCche-balkon-au%C3%9Fenfl%C3%A4che-und-kellerabteil-/-k3-42-1713275848/)                                                      | Jan 31, 10:49      |
|       580    |            52 |          2 | 17. Hernals      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/direktvergabe-gemeinde-wohnung-1260479768/)                                                                                                                                | Jan 31, 10:45      |
|       720    |            35 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/1020-wien-heinestra%C3%9Fe-sonnige-vollm%C3%B6blierte-helle-2-zimmer-dachgescho%C3%9Fwohnung-n%C3%A4he-augarten-und-u2-taborstrasse-privat-zu-vermieten.-1197964975/) | Jan 31, 10:34      |
|       799    |            42 |          2 | 22. Donaustadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/2-zimmer-neubauwohnung-inkl.-komplettk%C3%BCche-balkon-au%C3%9Fenfl%C3%A4che-und-kellerabteil-/-k3-29-1539621446/)                                                      | Jan 31, 09:48      |
|       799    |            39 |          2 | 22. Donaustadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1-monat-mietfrei:-erstbezug-im-gr%C3%BCnen-nahe-der-u2---zwischen-badeteich-hirschstetten-und-seestadt-943234822/)                                                      | Jan 31, 08:50      |
