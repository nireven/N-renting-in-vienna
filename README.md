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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                            | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       690    |            46 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/nachmieter-gesucht:-moderne-2-zimmer-neubauwohnung-n%C3%A4he-reumannplatz---mit-abl%C3%B6se-1213231136/)   | Dec 06, 15:06      |
|       775    |            48 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/%22flori-flats%22:-mietkauf-in-floridsdorf---idyllisches-wohnen-in-heurigengegend-737461147/)            | Dec 06, 14:45      |
|       770    |            49 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/stammersdorfer-wohnparadies:-mietwohnungen-mit-kaufoption-737459071/)                                    | Dec 06, 14:38      |
|       699    |            38 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1220-wien---genochplatz---ab-1.02.2025---gepflegte-neubauwohnung-mit-komplettk%C3%BCche-1695343321/)      | Dec 06, 14:03      |
|       784.1  |            52 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/n%C3%A4he-u3-erdberg-ii-2-zimmer-mit-separater-k%C3%BCche-ii-an-der-erdbergstra%C3%9Fe-854488554/)   | Dec 06, 13:54      |
|       799.14 |            42 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/winteraktion---erster-monat-mietfrei%21-moderne-2-zimmerwohnung-mit-balkon%21-1780493551/)                 | Dec 06, 13:36      |
|       485.72 |            37 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/topzustand%21-1956714731/)                                                                                 | Dec 06, 12:48      |
|       494.84 |            41 |          2 | 20. Brigittenau          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1200-brigittenau/kompakte-2-zimmer-wohnung%21-1979534702/)                                                                | Dec 06, 12:48      |
|       749.13 |            40 |          2 | 02. Leopoldstadt         | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/2-zimmer-wohnung-in-zentraler-lage-zu-vermieten-1535156517/)                                            | Dec 06, 12:36      |
|       699.94 |            48 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/2-zimmer-in-floridsdorf-zu-vermieten-1118328844/)                                                        | Dec 06, 12:07      |
|       700    |            40 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/2-zimmerwohnung-2142876084/)                                                               | Dec 06, 11:48      |
|       524.6  |            51 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/gemeindewohnung---wohnticket-30.09.2024-%7C-2-zimmer-2063886803/)                                            | Dec 06, 11:47      |
|       530    |            49 |          2 | 02. Leopoldstadt         | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/2-zimmer-gemeinde-wohnung-im-2.-bezirk-%28engerthstra%C3%9Fe-179-183%29-1615377569/)                    | Dec 06, 11:46      |
|       745    |            56 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/%2Aprovisionsfrei%2A-sehr-helle-und-sch%C3%B6ne-2-zimmer-wohnung-856985124/)               | Dec 06, 11:26      |
|       799    |            42 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/komfortabler-erstbezug:-2-zimmer-wohnungen-im-21.-bezirk-mit-balkon-und-moderner-k%C3%BCche-1151352378/) | Dec 06, 10:49      |
|       684.45 |            44 |          2 | 02. Leopoldstadt         | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/ruhelage-15-zimmer-u1/-u2-wu-n%C3%A4he-1386665170/)                                                     | Dec 06, 09:42      |
|       667.7  |            47 |          2 | 23. Liesing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/helle-und-ruhige-2-zimmer-wohnung-%7C-zellmann-immobilien-2012782510/)                                       | Dec 06, 07:24      |
|       731.33 |            72 |          3 | 02. Leopoldstadt         | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/gemeindewohnung-1020-wien---direktvergabe-961976560/)                                                   | Dec 06, 07:20      |
|       678.83 |            49 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/gem%C3%BCtliche-2-zimmer-wohnung-im-3.-og-2009648704/)                                                     | Dec 06, 02:49      |
|       767    |            76 |          3 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/gemeindewohnung-3-zimmer-direktvergabe-mit-balkon-1509367952/)                                            | Dec 05, 23:12      |
