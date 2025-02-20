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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District    | Link                                                                                                                                                                                                                                                                                | 📅 Published Date   |
|-------------:|--------------:|-----------:|:---------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       625.29 |            68 |          2 | 14. Penzing    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/unbefristete-2-zimmer-wohnung-mit-terrasse%21-2012023627/)                                                                                                                                       | Feb 20, 13:48      |
|       599    |            34 |          2 | 14. Penzing    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/ca.-34-m2-erstbezug-nach-sanierung-atelier-im-souterrain-f%C3%BCr-firma-oder-privat---all-inclusive-miete-warm-1578533243/)                                                                      | Feb 20, 12:01      |
|       799.98 |            41 |          2 | 09. Alsergrund | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/studentenhit:-2-zimmer-wohnung-mit-kfz-stellplatz-und-perfekter-infrastruktur---n%C3%A4he-spittelau-/-nu%C3%9Fdorferstra%C3%9Fe-u6-%28besichtigungen-erst-ab-23.1-m%C3%B6glich%29-988402127/) | Feb 20, 11:22      |
|       750    |            45 |          2 | 03. Landstraße | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/45-km2-wohnung-750.---euro-warm-in-wien-3-ab-m%C3%A4rz%21-2102603927/)                                                                                                                   | Feb 19, 22:00      |
|       468    |            44 |          2 | 11. Simmering  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/44m2-nur-mit-vormerkschein-bis-31.12.2024-direktvergabe-n%C3%A4he-u3-enkplatz-998600540/)                                                                                                      | Feb 19, 21:31      |
|       490    |            47 |          2 | 14. Penzing    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/gemeindewohnung-1140-wien-sch%C3%B6nbrunn-n%C3%A4he---direktvergabe-1684316896/)                                                                                                                 | Feb 19, 20:55      |
|       550    |            54 |          2 | 14. Penzing    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/%28reserviert%29-2-zimmer-wohnung-im-altbau-1649124945/)                                                                                                                                         | Feb 19, 18:11      |
|       725.98 |            55 |          2 | 14. Penzing    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/ruhige-2-zimmer-wohnung-mit-balkon%21-2142797932/)                                                                                                                                               | Feb 19, 15:49      |
|       748.36 |            50 |          2 | 04. Wieden     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1040-wieden/n%C3%A4he-st.-elisabeth-platz-kleine-2-zimmer-wohnung-f%C3%BCr-jungebliebene-1205570002/)                                                                                                         | Feb 19, 14:23      |
|       599    |            45 |          2 | 17. Hernals    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/provisionsfrei-&-unbefristet%21-ruhige-wohnung-in-zentraler-lage-1381275211/)                                                                                                                    | Feb 19, 14:12      |
|       689    |            60 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/provisionsfrei-&-unbefristet%21-ruhige-wohnung-beim-neuen-landgut-1524927764/)                                                                                                                 | Feb 19, 14:06      |
