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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                                                                        | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       696.56 |            61 |          2 | 09. Alsergrund   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/wundersch%C3%B6ne-sehr-helle-unbefristete-hauptmietwohnung---n%C3%A4he-u6-station-nu%C3%9Fdorferstra%C3%9Fe-%21-1399290272/)                          | Jan 29, 13:18      |
|       619.31 |            47 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/helle-ruhige-2-zimmer-in-stilaltbau-nahe-u2-station---augarten-1892315569/)                                                                         | Jan 29, 13:14      |
|       765.95 |            47 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/hofseitige-2-zimmer-stielalbauwohnung---n%C3%A4he-u1-vorgartenstra%C3%9Fe-934931577/)                                                               | Jan 29, 12:53      |
|       767.95 |            49 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/terrassentraum-f%C3%BCr-p%C3%A4rchen---wohnung-mit-perfektem-grundriss---n%C3%A4he-einkaufszentrum-huma-eleven-1338398862/)                            | Jan 29, 12:53      |
|       785.84 |            47 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/ina---p%C3%A4rchenwohnung-mit-perfektem-grundriss---n%C3%A4he-kaiserebersdorf-1590079860/)                                                             | Jan 29, 12:53      |
|       771.62 |            42 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/n%C3%A4he-schloss-neugeb%C3%A4ude---wohnung-perfekt-f%C3%BCr-singles-oder-p%C3%A4rchen-mit-freifl%C3%A4che-1759659165/)                                | Jan 29, 12:29      |
|       498.64 |            41 |          2 | 20. Brigittenau  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1200-brigittenau/kompakte-2-zimmer-wohnung%21-1406170543/)                                                                                                            | Jan 29, 11:20      |
|       720    |            44 |          2 | 21. Floridsdorf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/mietwohnung-genie%C3%9Fen-kaufoption-nutzen:-wohnen-in-stammersdorfer-naturkulisse-761411356/)                                                       | Jan 29, 10:07      |
|       770    |            49 |          2 | 21. Floridsdorf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/jetzt-mieten-sp%C3%A4ter-kaufen:-wohnen-in-stammersdorfer-naturidylle-761411382/)                                                                    | Jan 29, 10:07      |
|       799    |            38 |          2 | 22. Donaustadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1-monat-mietfrei:-erstbezug-im-gr%C3%BCnen-nahe-der-u2---zwischen-badeteich-hirschstetten-und-seestadt-954325505/)                                    | Jan 29, 07:56      |
|       799    |            38 |          2 | 22. Donaustadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1-monat-mietfrei:-erstbezug-im-gr%C3%BCnen-nahe-der-u2---zwischen-badeteich-hirschstetten-und-seestadt-968537777/)                                    | Jan 29, 07:54      |
|       799    |            38 |          2 | 22. Donaustadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1-monat-mietfrei:-erstbezug-im-gr%C3%BCnen-nahe-der-u2---zwischen-badeteich-hirschstetten-und-seestadt-2033089937/)                                   | Jan 29, 07:46      |
|       799    |            45 |          2 | 17. Hernals      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/sonnige-2-zimmer-neubauwohnung-mit-loggia-n%C3%A4he-elterleinplatz-1864249983/)                                                                          | Jan 29, 03:32      |
|       570.48 |            68 |          2 | 22. Donaustadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/charmante-2-zimmer-wohnung-1729044802/)                                                                                                               | Jan 29, 02:48      |
|       716.8  |            52 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/ger%C3%A4umige-2-zimmer-wohnung-im-eg-1214111912/)                                                                                                      | Jan 29, 02:47      |
|       712.31 |            43 |          2 | 21. Floridsdorf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/sehr-gut-gelegene-43m%C2%B2-wohnung---ihr-neues-zuhause-mit-allem-was-sie-brauchen%21-5-minuten-zu-fu%C3%9F-von-der-donauinsel-entfernt-1781341824/) | Jan 29, 02:09      |
|       585.44 |            57 |          2 | 21. Floridsdorf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/sch%C3%B6ne-wohnung-mit-toller-aussicht-%2821.-bezirk%29-%2Ateilm%C3%B6bliert%2A-1638582499/)                                                        | Jan 28, 23:03      |
|       733    |            50 |          2 | 20. Brigittenau  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1200-brigittenau/mietwohnung-im-20.-bezirk-1829835939/)                                                                                                               | Jan 28, 22:00      |
|       690    |            82 |          3 | 21. Floridsdorf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/%28reserviert%29-3zimmer-gemeinde-mit-direkt-vergabe-vms-08.03.2024-1559971839/)                                                                     | Jan 28, 19:31      |
|       787.92 |            41 |          2 | 22. Donaustadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/modernes-wohnen-mit-balkon-in-1220-wien---4119m%C2%B2-zum-mietpreis-von-78792-eur%21-1580236359/)                                                     | Jan 28, 18:35      |
