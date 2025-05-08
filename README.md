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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District    | Link                                                                                                                                                                                                                                                                                                | 📅 Published Date   |
|-------------:|--------------:|-----------:|:---------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       630    |            62 |          3 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/3--zimmer-gemeindewohnung-2133366038/)                                                                                                                                                                         | May 08, 21:53      |
|       548    |            32 |          2 | 14. Penzing    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/provisionsfrei-f%C3%BCr-den-mieter%21-1140-felbigergasse:-n%C3%A4chst-hanusch-krankenhaus-%C3%A4ltere-32m%C2%B2-neubaumiete-4.-stock---kein-lift--nur-f%C3%BCr-sportliche%21-studenten-bevorzugt%21-1195013145/) | May 08, 20:38      |
|       775.42 |            69 |          3 | 16. Ottakring  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/provisionsfreier-erstbezug:-renovierter-69m%C2%B2-altbau-mit-3-zimmern---1160-wien-1483440899/)                                                                                                                | May 08, 20:35      |
|       536    |            48 |          2 | 03. Landstraße | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/gemeindewohnung-direkvergabe-vormerkschein-vor-dem-30.04.2025---1030-wien---top-lage-nahe-kardinal-nagl-platz-1398015562/)                                                                               | May 08, 18:56      |
|       485    |            50 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/direktvergabe-gemeindewohnung-50-m%C2%B2-wohnticket-2-zimmer-vor-31.03.2025-1689668878/)                                                                                                                       | May 08, 18:25      |
|       799    |            39 |          2 | 16. Ottakring  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/orea-%7C-sch%C3%B6ne-2-zimmer-wohnung-mit-guter-anbindung-%7C-smart-besichtigen-%C2%B7-online-anmieten-935252328/)                                                                                             | May 08, 17:25      |
|       500    |            44 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeindewohnung-direktvergabe-2-zimmer-1414452172/)                                                                                                                                                            | May 08, 17:13      |
|       645    |            40 |          2 | 16. Ottakring  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/charmante-2-zimmer-wohnung-nahe-u6-thaliastra%C3%9Fe---perfekt-f%C3%BCr-singles-oder-paare-1813305604/)                                                                                                        | May 08, 15:48      |
|       669.5  |            35 |          2 | 09. Alsergrund | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/wohnen-in-der-seegasse%21-anfragen-nur-per-mail---keine-anrufe%21-13:00-13:20-uhr.-1159923691/)                                                                                                               | May 08, 12:53      |
|       797.55 |            59 |          2 | 17. Hernals    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/beautiful-2-room-apartment-with-separate-kitchen-1723204266/)                                                                                                                                                    | May 08, 12:27      |
|       799.98 |            41 |          2 | 09. Alsergrund | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/studentenhit:-2-zimmer-wohnung-mit-kfz-stellplatz-und-perfekter-infrastruktur---n%C3%A4he-spittelau-/-nu%C3%9Fdorferstra%C3%9Fe-u6-988402127/)                                                                | May 08, 11:22      |
|       755    |            62 |          2 | 12. Meidling   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/studenten-wg-f%C3%BCr-2-personen-1916946493/)                                                                                                                                                                   | May 07, 21:00      |
