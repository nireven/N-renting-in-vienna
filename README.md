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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District    | Link                                                                                                                                                                                         | 📅 Published Date   |
|-------------:|--------------:|-----------:|:---------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       689    |            40 |          2 | 07. Neubau     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1070-neubau/studentenhit:-2-zimmer-wohnung-in-neubau-1527797968/)                                                      | Mar 03, 10:48      |
|       741.74 |            48 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/ol%C3%A9-ol%C3%A9---oh-la-laa-%21-bezugsfertig-mai-2025%21-1101051871/)                                 | Mar 03, 10:22      |
|       796.4  |            52 |          2 | 03. Landstraße | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/genossenschaftswohnung-mit-balkon-&-top-ausstattung-in-1030-wien-1711325663/)                     | Mar 03, 08:59      |
|       786.55 |            54 |          2 | 06. Mariahilf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1060-mariahilf/gumpendorferstra%C3%9Fe%21-helles-moderne-2-zimmer-mietwohnung-n%C3%A4he-raimundtheater%21-1292456913/) | Mar 02, 17:54      |
|       432    |            42 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/direktvergabe-wiener-wohnen-ticket-31.12.2024-1969505461/)                                              | Mar 02, 16:20      |
|       735.91 |            35 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/singlewohnung-in-oberlaa---sehr-sch%C3%B6ne-neubauwohnung-im-dachgescho%C3%9F-zu-vermieten-1269655757/) | Mar 02, 14:23      |
|       552    |            49 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeindewohnung-2-zimmer-bei-u1-troststra%C3%9Fe-1458909239/)                                           | Mar 02, 14:12      |
|       794    |            50 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/zwei-zimmer---50m%C2%B2---hauptbahnhof-n%C3%A4he-1854453854/)                                           | Mar 02, 13:13      |
|       715    |            36 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gem%C3%BCtliche-2--zimmer-whg---3-liftstock-inkl.-hz-u.-ww-%21%21-1607790328/)                          | Mar 02, 11:25      |
