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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                                                     | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       748.21 |            55 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/gr%C3%BCnruhelage-%21-wundersch%C3%B6ne-stilaltbauwohnung---n%C3%A4he-u1-vorgartenstra%C3%9Fe-797282377/)                        | Apr 29, 13:26      |
|       790    |            51 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/provisionfrei-2-zimmer-u1-n%C3%A4he-zu-mieten-650200020/)                                                                           | Apr 29, 12:50      |
|       765.57 |            41 |          2 | 09. Alsergrund   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/erstbezug-nach-sanierung-15-zimmer-neubauwohnung-41m%C2%B2-n%C3%A4he-spittelau-5-minuten-zur-u6-schriftl.-anfragen%21-1369327747/) | Apr 29, 12:48      |
|       779    |            52 |          2 | 14. Penzing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/superzentrale-superhauptmiete%21-831972445/)                                                                                          | Apr 29, 11:27      |
|       619    |            57 |          3 | 05. Margareten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/gemeindewohnung-direktvergabe-f%C3%BCr-3-zimmer-mit-vmd-bis-31.03.2025-1942525057/)                                                | Apr 29, 06:42      |
|       718.44 |            50 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/supermiete--ruhige-2-zimmerwohnung--n%C3%A4he-augarten--unbefristet-823336343/)                                                  | Apr 28, 20:31      |
|       588.86 |            56 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/gemeindewohnung-11.-bezirk-mit-balkon-5662m2-1820479435/)                                                                           | Apr 28, 15:44      |
|       750    |            45 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/helle-45-m2-wohnung-privat-zu-vermieten-1835727011/)                                                                                 | Apr 28, 12:30      |
