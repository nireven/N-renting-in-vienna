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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                                                                       | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       440.72 |            42 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/gemeindewohnung-1020-wien-vms:-31.10.2024-928811082/)                                                                                              | Jan 26, 15:57      |
|       523.08 |            51 |          2 | 23. Liesing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/gemeindewohnung-1230-/-u-bahn-n%C3%A4he-und-gr%C3%BCnlage-%28nur-mit-vormerkschein-f%C3%BCr-zwei-wohnr%C3%A4ume-bis-30.11.2024%29-1687561871/)          | Jan 26, 12:42      |
|       780    |            41 |          2 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/%28reserviert%29-sch%C3%B6ne-2-zimmer-wohnung-m%C3%B6bliert-mit-gemeinschaftsterrasse-1177823895/)                                                    | Jan 26, 10:53      |
|       749.71 |            42 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/ina---p%C3%A4rchenwohnung-mit-freifl%C3%A4che-n%C3%A4he-wasserspielplatz-leberberg-1904606435/)                                                       | Jan 26, 10:24      |
|       650    |            60 |          2 | 20. Brigittenau  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1200-brigittenau/arbeiterwohnung/-mitbewohnerin-1791051217/)                                                                                                         | Jan 25, 21:30      |
|       799    |            38 |          2 | 22. Donaustadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1.-monat-mietfrei-bei-anmietung-ab-01.02.2025%21---exklusiver-erstbezug-im-gr%C3%BCnen---n%C3%A4he-badeteich-hirschstetten-und-seestadt-1121430053/) | Jan 25, 21:07      |
|       799    |            39 |          2 | 22. Donaustadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1.-monat-mietfrei-bei-anmietung-ab-01.02.2025%21---exklusiver-erstbezug-im-gr%C3%BCnen---n%C3%A4he-badeteich-hirschstetten-und-seestadt-2024426355/) | Jan 25, 20:37      |
|       799    |            39 |          2 | 22. Donaustadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1.-monat-mietfrei-bei-anmietung-ab-01.02.2025%21---exklusiver-erstbezug-im-gr%C3%BCnen---n%C3%A4he-badeteich-hirschstetten-und-seestadt-936159672/)  | Jan 25, 20:35      |
|       799    |            39 |          2 | 22. Donaustadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1.-monat-mietfrei-bei-anmietung-ab-01.02.2025%21---exklusiver-erstbezug-im-gr%C3%BCnen---n%C3%A4he-badeteich-hirschstetten-und-seestadt-1047595278/) | Jan 25, 20:30      |
|       799    |            39 |          2 | 22. Donaustadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1.-monat-mietfrei-bei-anmietung-ab-01.02.2025%21---exklusiver-erstbezug-im-gr%C3%BCnen---n%C3%A4he-badeteich-hirschstetten-und-seestadt-1246911235/) | Jan 25, 20:24      |
|       799    |            39 |          2 | 22. Donaustadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1.-monat-mietfrei-bei-anmietung-ab-01.02.2025%21---exklusiver-erstbezug-im-gr%C3%BCnen---n%C3%A4he-badeteich-hirschstetten-und-seestadt-1519969127/) | Jan 25, 20:07      |
|       799    |            39 |          2 | 22. Donaustadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1.-monat-mietfrei-bei-anmietung-ab-01.02.2025%21---exklusiver-erstbezug-im-gr%C3%BCnen---n%C3%A4he-badeteich-hirschstetten-und-seestadt-1087427696/) | Jan 25, 19:56      |
|       799    |            39 |          2 | 22. Donaustadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1.-monat-mietfrei-bei-anmietung-ab-01.02.2025%21---exklusiver-erstbezug-im-gr%C3%BCnen---n%C3%A4he-badeteich-hirschstetten-und-seestadt-1963751987/) | Jan 25, 19:43      |
|       799    |            38 |          2 | 22. Donaustadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1.-monat-mietfrei-bei-anmietung-ab-01.02.2025%21---exklusiver-erstbezug-im-gr%C3%BCnen---n%C3%A4he-badeteich-hirschstetten-und-seestadt-2026986773/) | Jan 25, 19:41      |
|       799    |            39 |          2 | 22. Donaustadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1-monat-mietfrei:-erstbezug-im-gr%C3%BCnen-nahe-der-u2---zwischen-badeteich-hirschstetten-und-seestadt-1549024927/)                                  | Jan 25, 17:52      |
|       799    |            39 |          2 | 22. Donaustadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1-monat-mietfrei:-erstbezug-im-gr%C3%BCnen-nahe-der-u2---zwischen-badeteich-hirschstetten-und-seestadt-1522287969/)                                  | Jan 25, 17:38      |
|       799    |            39 |          2 | 22. Donaustadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1-monat-mietfrei:-erstbezug-im-gr%C3%BCnen-nahe-der-u2---zwischen-badeteich-hirschstetten-und-seestadt-1753237766/)                                  | Jan 25, 17:36      |
|       719    |            54 |          2 | 14. Penzing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/gem%C3%BCtliche-2-zimmer-wohnung-in-1140-wien-2107460977/)                                                                                              | Jan 25, 17:30      |
|       704.53 |            70 |          2 | 14. Penzing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/helle-freundliche-p%C3%A4rchen-wohnung-altbau-stauraumwunder-1708739990/)                                                                               | Jan 25, 16:50      |
|       768    |            51 |          3 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/sch%C3%B6ne-ger%C3%A4umige-neue-51m%C2%B2-3-zimmer-mietwohnung-f%C3%BCr-768%E2%82%AC-in-wien-1160-1458707831/)                                        | Jan 25, 16:17      |
