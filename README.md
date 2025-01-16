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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District     | Link                                                                                                                                                                                                          | 📅 Published Date   |
|-------------:|--------------:|-----------:|:----------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       799    |            39 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1-monat-mietfrei:-erstbezug-im-gr%C3%BCnen-nahe-der-u2---zwischen-badeteich-hirschstetten-und-seestadt-1003521952/)     | Jan 16, 09:50      |
|       799    |            39 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1-monat-mietfrei:-erstbezug-im-gr%C3%BCnen-nahe-der-u2---zwischen-badeteich-hirschstetten-und-seestadt-804820142/)      | Jan 16, 09:48      |
|       799    |            39 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1-monat-mietfrei:-erstbezug-im-gr%C3%BCnen-nahe-der-u2---zwischen-badeteich-hirschstetten-und-seestadt-778162811/)      | Jan 16, 09:46      |
|       799    |            39 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1-monat-mietfrei:-erstbezug-im-gr%C3%BCnen-nahe-der-u2---zwischen-badeteich-hirschstetten-und-seestadt-1115588133/)     | Jan 16, 09:40      |
|       799.5  |            44 |          2 | 13. Hietzing    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1130-hietzing/hell-und-stilvoll-wohnen---charmante-2-zimmer-wohnung-in-hietzing---1820138740/)                                          | Jan 16, 09:40      |
|       600.72 |            58 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/erstbezug---1220-wien--zentral-gelegene-2-zimmerwohnung-mit-balkon-1134484591/)                                         | Jan 16, 09:18      |
|       777.98 |            73 |          3 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/erstbezug---1220-wien--sch%C3%B6ne-3-zimmerwohnung-mit-balkon---kaufoption-903248209/)                                  | Jan 16, 09:18      |
|       740    |            51 |          2 | 13. Hietzing    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1130-hietzing/2__zimmer__mit-wohnk%C3%BCche-1751181418/)                                                                                | Jan 16, 08:16      |
|       799    |            38 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1-monat-mietfrei:-erstbezug-im-gr%C3%BCnen-nahe-der-u2---zwischen-badeteich-hirschstetten-und-seestadt-1881694930/)     | Jan 16, 07:45      |
|       733.77 |            42 |          2 | 19. Döbling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1190-d%C3%B6bling/gem%C3%BCtliche-singlewohnung-im-19.-bezirk-1191172900/)                                                              | Jan 16, 06:48      |
|       750    |            61 |          2 | 10. Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/moderne-wohnung-in-zentraler-lage---vollrenoviert-mit-einbauk%C3%BCche-und-parkettboden-1065985315/)                     | Jan 16, 04:40      |
|       790    |            46 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/privat:-gr%C3%BCnruhelage-2-zimmer-wohnung-702574007/)                                                                 | Jan 15, 21:22      |
|       795    |            47 |          2 | 12. Meidling    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/wohnquartier-wildgarten---familienfreundliches-wohnen-auf-der-sonnenseite-wiens-direkt-am-rosenh%C3%BCgel-1596135640/)    | Jan 15, 20:38      |
|       598.95 |            50 |          3 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/3-zimmer-wohnung-mit-gemeinschaftsg%C3%A4rtchen-in-wien-floridsdorf-1724289823/)                                       | Jan 15, 19:30      |
|       798.79 |            43 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/komfortabler-erstbezug:-2-zimmer-wohnungen-im-21.-bezirk-mit-balkon-und-moderner-k%C3%BCche.---wohntraum-1104579405/)  | Jan 15, 18:57      |
|       795.06 |            63 |          2 | 23. Liesing     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/2-zimmer-wohnung-in-absoluter-ruhelage-%7C-zellmann-immobilien-971518084/)                                                 | Jan 15, 18:57      |
|       598    |            54 |          2 | 10. Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/privat-mite-wohnung-847901994/)                                                                                          | Jan 15, 17:55      |
|       759    |            38 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/1210-wien---gut-geschnittene-neubauwohnung-mit-sch%C3%B6nen-ausblick-und-komplettk%C3%BCche---ab-1.2.2025-1836529090/) | Jan 15, 17:51      |
|       695    |            38 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1220-wien---genochplatz---8ter-liftstock---neuwertige-helle-singlewohnung---sofortbezug-967165027/)                     | Jan 15, 17:51      |
|       741.85 |            52 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/m%C3%B6blierte-2-zimmer-wohnung-in-sehr-gutem-zustand---bereit-f%C3%BCr-deinen-einzug%21-973543492/)                    | Jan 15, 17:47      |
