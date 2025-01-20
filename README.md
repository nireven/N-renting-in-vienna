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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District     | Link                                                                                                                                                                                                                                                                   | 📅 Published Date   |
|-------------:|--------------:|-----------:|:----------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       799    |            39 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1-monat-mietfrei-in-der-pfalzgasse-29---2-zimmer-wohnung-mit-balkon---erstbezug-in-ruhelage-1609375860/)                                                                         | Jan 20, 11:51      |
|       799    |            39 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/pfalzgasse-29---traumhafter-erstbezug-in-ruhelage---1-monat-mietfrei%21-2-zimmer-apartment-mit-balkon-1705094653/)                                                               | Jan 20, 11:46      |
|       799    |            39 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/pfalzgasse-29---1-monat-mietfrei%21-2-zimmer-wohnung-mit-balkon-%7C-traumhafter-erstbezug-in-ruhelage-1283007542/)                                                               | Jan 20, 11:41      |
|       799    |            38 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/pfalzgasse-29---lichtdurchflutet-und-modern:-2-zimmer-wohnung-mit-balkon--erstbezug-in-ruhelage-786080173/)                                                                      | Jan 20, 11:37      |
|       799    |            38 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/pfalzgasse-29---traumhafter-erstbezug-in-ruhelage-1311362301/)                                                                                                                   | Jan 20, 11:35      |
|       799    |            38 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/pfalzgasse-29---2-zimmer-aartment-mit-balkon-traumhafter-erstbezug-in-ruhelage-1043504437/)                                                                                      | Jan 20, 11:33      |
|       774    |            38 |          2 | 03. Landstraße  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/%28reserviert%29-sch%C3%B6ner-wohnen-mit-stil-%2A-2-zimmer-wohnung-vollst%C3%A4ndig-m%C3%B6bliert---3.-bezirk-f%C3%BCr-universit%C3%A4ten/-business-%2A-all-in-1559533337/) | Jan 20, 11:29      |
|       727.98 |            52 |          2 | 17. Hernals     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/anzeige-953354258/)                                                                                                                                                                 | Jan 20, 11:28      |
|       762.3  |            55 |          2 | 17. Hernals     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/geniale-2-zimmerwohnung-mit-lift-und-neuer-k%C3%BCche-%28ist-bis-zum-einzug-eingebaut%21%29-1532035290/)                                                                            | Jan 20, 11:22      |
|       650    |            42 |          2 | 09. Alsergrund  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/charmante-15-zimmer-wohnung-in-top-lage---alserbachstra%C3%9Fe-33-top-25-1536373683/)                                                                                            | Jan 20, 11:01      |
|       769    |            40 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/2-zimmer-neubauwohnung-inkl.-komplettk%C3%BCche-balkon-au%C3%9Fenfl%C3%A4che-und-kellerabteil/-sp64-top-5-50-1330949619/)                                                        | Jan 20, 11:00      |
|       719    |            34 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1220-wien---kirschbl%C3%BCtenpark---u1-n%C3%A4he-kagran---hofseitige-singlewohnung---provisionsfrei-1610628281/)                                                                 | Jan 20, 10:58      |
|       492.65 |            49 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/direktvergabe-2-zimmerwohnung-gemeinde-wohnung-vm:-31.10.2024-1586604573/)                                                                                                      | Jan 20, 10:35      |
|       609.71 |            62 |          3 | 23. Liesing     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/3-zimmer-gemeindewohnung---abl%C3%B6se-2000-euro---schnell-zugreifen%21%21%21-1282788944/)                                                                                          | Jan 20, 10:19      |
|       729.31 |            46 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/provisionsfreie-traumwohnung:-2-zimmer-%7C-top-lage%7C-ausgezeichnete-anbindung-1587911057/)                                                                                    | Jan 20, 10:03      |
|       799    |            43 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/2-zimmer-neubauwohnung-inkl.-komplettk%C3%BCche-balkon-au%C3%9Fenfl%C3%A4che-und-kellerabteil/-alf41-top-32-1275531367/)                                                         | Jan 20, 09:49      |
|       779.99 |            44 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/2-zimmer-neubauwohnung-inkl.-komplettk%C3%BCche-und-kellerabteil-/-i3-top-31-1430668443/)                                                                                        | Jan 20, 09:27      |
|       779.99 |            43 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/2-zimmer-neubauwohnung-inkl.-komplettk%C3%BCche-balkon-au%C3%9Fenfl%C3%A4che-und-kellerabteil-/-i3-top-14-1996398254/)                                                           | Jan 20, 09:27      |
|       770    |            43 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/2-zimmer-neubauwohnung-inkl.-komplettk%C3%BCche-balkon-au%C3%9Fenfl%C3%A4che-und-kellerabteil-/-i3-top-46-864784617/)                                                            | Jan 20, 09:27      |
|       554    |            57 |          2 | 16. Ottakring   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/sonnige-2-zimmer-gemeinde-wohnung-vm:-31.12.2024-1787398134/)                                                                                                                     | Jan 20, 09:01      |
