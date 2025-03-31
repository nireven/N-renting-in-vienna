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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District    | Link                                                                                                                                                                                                                            | 📅 Published Date   |
|-------------:|--------------:|-----------:|:---------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       475    |            56 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/wohnung-mit-blick-in-den-innenhof-1353852770/)                                                                                             | Mar 31, 07:46      |
|       620    |            76 |          3 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/balkonwohnung-im-10.-bezirk-951578508/)                                                                                                    | Mar 31, 07:46      |
|       510    |            67 |          3 | 14. Penzing    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/wohnen-am-fl%C3%B6tzersteig-1062030562/)                                                                                                     | Mar 31, 07:46      |
|       740    |            72 |          4 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/4-zimmer-gemeindewohnung-1100-vormerkschein-2018%21%21%21%21-1269361159/)                                                                  | Mar 31, 07:37      |
|       475    |            43 |          2 | 03. Landstraße | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/2-zimmer-gemeindewohnung-in-top-zustand%21-direktvergabe-1083109868/)                                                                | Mar 30, 23:24      |
|       420    |            41 |          2 | 03. Landstraße | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/gemeindewohnung-zur-vergabe-1140494205/)                                                                                             | Mar 30, 22:07      |
|       480    |            47 |          2 | 14. Penzing    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/gemeinde-wohnung-direktvergabe-1140-wien-1988096894/)                                                                                        | Mar 30, 21:35      |
|       795    |            50 |          2 | 12. Meidling   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/helle-2-zimmer-mit-balkon-1328093080/)                                                                                                      | Mar 30, 19:40      |
|       699.99 |            56 |          2 | 16. Ottakring  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/2-zimmer-unbefristet%21-1720907670/)                                                                                                       | Mar 30, 18:49      |
|       750    |            45 |          2 | 05. Margareten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/student:-innen-zur-untermiete-gesucht-%28nur-1-person%29-779443963/)                                                                      | Mar 30, 18:09      |
|       750    |            38 |          2 | 16. Ottakring  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/ruhige-und-helle-2-zimmer-wohnung-mit-blick-in-den-innenhof-keine-provision-&-heizung-in-bk-inkludiert%21-1934789698/)                     | Mar 30, 17:12      |
|       432    |            42 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/%28reserviert%29-direktvergabe-wiener-wohnen-ticket-31.12.2024-1969505461/)                                                                | Mar 30, 16:20      |
|       600.07 |            44 |          2 | 12. Meidling   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/44m2-wohnung---unbefristet-1043020343/)                                                                                                     | Mar 30, 14:33      |
|       610    |            55 |          3 | 14. Penzing    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/gemeindewohnung-direktvergabe-1152453997/)                                                                                                   | Mar 30, 14:09      |
|       470    |            54 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/moderne-sch%C3%B6ne-2-zimmer-wohnung-in-wien-1100-%28oberlaa%29-gef%C3%B6rderte-wohnung-m%C3%B6bliert---sofort-verf%C3%BCgbar-1367589114/) | Mar 30, 12:46      |
|       676.34 |            43 |          2 | 14. Penzing    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/erstbezug-nach-top-sanierung:-helle-2-zimmer-wohnung-nahe-hanusch-krankenhaus-1329993018/)                                                   | Mar 30, 12:16      |
|       469    |            38 |          2 | 11. Simmering  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/moderne-kleinwohnung-2-zimmer-1277902762/)                                                                                                 | Mar 30, 06:40      |
