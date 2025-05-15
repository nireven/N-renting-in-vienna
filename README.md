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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                                                     | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       645    |            40 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/charmante-2-zimmer-wohnung-nahe-u6-thaliastra%C3%9Fe---perfekt-f%C3%BCr-singles-oder-paare-1813305604/)                                                             | May 15, 15:48      |
|       690    |            64 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-wohnung-mit-ca.-64m%C2%B2-1205283037/)                                                                                                                     | May 15, 15:03      |
|       790    |            35 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/moderne-singlewohnung-in-der-linzer-strasse-1258677953/)                                                                                                              | May 15, 13:49      |
|       750    |            54 |          2 | 07. Neubau               | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1070-neubau/%28reserviert%29-charmante-single-oder-p%C3%A4rchen-wohnung-798890361/)                                                                                                | May 15, 13:18      |
|       799.98 |            41 |          2 | 09. Alsergrund           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/studentenhit:-2-zimmer-wohnung-mit-kfz-stellplatz-und-perfekter-infrastruktur---n%C3%A4he-spittelau-/-nu%C3%9Fdorferstra%C3%9Fe-u6-988402127/)                     | May 15, 11:22      |
|       753.54 |            69 |          3 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/m%C3%A4rzstra%C3%9Fe-3-zimmer-n%C3%A4he-u-bahn-1030574630/)                                                                                         | May 15, 10:20      |
|       650    |            55 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-wohnung-1435747819/)                                                                                                                                       | May 15, 09:27      |
|       770    |           nan |          3 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/mitten-im-10ten---zentral-und-ruhig-gelegen-943546318/)                                                                                                             | May 15, 08:25      |
|       785.84 |            52 |          2 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/wohnen-im-gepflegten-altbau-1253679793/)                                                                                                                              | May 14, 21:55      |
|       684.04 |            59 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/renovierungsbed%C3%BCrftige-2-zimmer-wohnung-%7C-altbau-%7C-klinik-favoriten-901202578/)                                                                            | May 14, 20:35      |
|       555    |            51 |          2 | 02. Leopoldstadt         | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/2-zimmer-gemeinde-wohnung-inkl.-m%C3%B6beln-/-gute-%C3%B6ffentliche-anbindungen-/-gute-parkm%C3%B6glichkeiten-/-sch%C3%B6n-zentral-mit-freier-sicht-1996075914/) | May 14, 19:36      |
|       650    |            38 |          3 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/sonnige-s%C3%BCdseitige-balkonwohnung-schn%C3%A4ppchen%21-1475646740/)                                                                                              | May 14, 18:56      |
|       690    |            61 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/sanierte-2-zimmer-wohnung-nahe-sonnwendviertel-1105127325/)                                                                                                         | May 14, 16:19      |
|       795    |            54 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/3.erdbergstrasse---provisionsfreie-charmante-2-zimmer-neubaumiete-direkt-beim-kardinal-naglplatz-2105617351/)                                                 | May 14, 15:32      |
