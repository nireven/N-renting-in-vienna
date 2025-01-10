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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                                                                 | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       686    |            47 |          2 | 05. Margareten           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/helle-ruhige-2-zimmer-wohnung-in-zentraler-lage-n%C3%A4chst-wiedner-hauptstra%C3%9Fe-und-unweit-u1%21-911983497/)                                                              | Jan 10, 11:49      |
|       790.02 |            53 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/tolle-2-zimmer-wohnung-mit-gro%C3%9Fer-neuer-k%C3%BCche---hohe-r%C3%A4ume-im-altbau-mit-schlafzimmer-in-den-innenhof---wg-geeignet-1183774507/)                 | Jan 10, 11:49      |
|       799    |            39 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1-monat-mietfrei:-erstbezug-im-gr%C3%BCnen-nahe-der-u2---zwischen-badeteich-hirschstetten-und-seestadt-807881379/)                                                             | Jan 10, 11:46      |
|       745    |            56 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/%2Aprovisionsfrei%2A-sehr-helle-und-sch%C3%B6ne-2-zimmer-wohnung-856985124/)                                                                                    | Jan 10, 11:26      |
|       678.56 |            54 |          3 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/sanierter-neubau-mit-balkon-in-zentraler-lage%21-978154174/)                                                                                                                    | Jan 10, 10:58      |
|       612.45 |            47 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/neu-saniert-%2A%2A%2A-am-migazziplatz-%2A%2A%2A-n%C3%A4he-u4/u6-station-%2A%2A%2A-1-zimmer-mit-kabinett-und-separater-k%C3%BCche-%2A%2A%2A-beim-theresienbad-/-park-1543014494/) | Jan 10, 10:58      |
|       775    |            45 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/traumhafte-2-zimmer-wohnung-mit-atemberaubendem-ausblick-in-toller-lage-1494136099/)                                                                                          | Jan 10, 09:27      |
|       780.99 |            51 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/moderne-miete-mit-terrasse-und-kleiner-gartenfl%C3%A4che-oberlaa-1069628360/)                                                                                                   | Jan 10, 09:27      |
|       775    |            47 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/traumhafte-2-zimmer-wohnung-mit-tollem-ausblick-in-ausgezeichneter-lage-2060437291/)                                                                                          | Jan 10, 09:25      |
|       799    |            39 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1-monat-mietfrei:-erstbezug-im-gr%C3%BCnen-nahe-der-u2---zwischen-badeteich-hirschstetten-und-seestadt-943234822/)                                                             | Jan 10, 08:50      |
|       799    |            38 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1-monat-mietfrei:-erstbezug-im-gr%C3%BCnen-nahe-der-u2---zwischen-badeteich-hirschstetten-und-seestadt-1322667550/)                                                            | Jan 10, 08:26      |
|       680    |            41 |          2 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/provisionsfrei%21-helle-ruhige-41m2-wohnung-mit-gr%C3%BCnblick-1216582435/)                                                                                                       | Jan 10, 08:19      |
|       799    |            38 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1-monat-mietfrei:-erstbezug-im-gr%C3%BCnen-nahe-der-u2---zwischen-badeteich-hirschstetten-und-seestadt-1889003533/)                                                            | Jan 10, 08:11      |
|       799    |            39 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1-monat-mietfrei:-erstbezug-im-gr%C3%BCnen-nahe-der-u2---zwischen-badeteich-hirschstetten-und-seestadt-1704280680/)                                                            | Jan 10, 07:54      |
|       750    |            47 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/%22kompakte-eleganz:-erstbezug-in-sanierter-wohnung%21%22-1010670731/)                                                                                                          | Jan 10, 07:12      |
|       678.83 |            49 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/gem%C3%BCtliche-2-zimmer-wohnung-im-3.-og-2009648704/)                                                                                                                          | Jan 10, 02:49      |
|       705    |            68 |          3 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/3-zimmer-gemeindewohnung-1459925097/)                                                                                                                                          | Jan 09, 21:59      |
|       766    |            65 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/altbauappartement-im-hetzendorfer-cottage-2001283882/)                                                                                                                           | Jan 09, 20:37      |
|       617    |            64 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/wohnung-zu-vermieten-1813785410/)                                                                                                                                               | Jan 09, 20:30      |
|       779    |            35 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/2-zimmer-wohnung-%7C-thaliastra%C3%9Fe-%7C-billa-im-haus-%7C-3.-liftstock-1753848084/)                                                                                          | Jan 09, 19:33      |
