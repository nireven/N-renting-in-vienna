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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                        | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       662.71 |            42 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/2-zimmerwohnung-zwischen-botanischer-garten-und-schweizer-garten-1221223994/)                                    | Mar 31, 15:42      |
|       799.94 |            40 |          2 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/modernes-wohnen-im-erstbezug---frisch-sanierte-wohnung-mit-hochwertiger-ausstattung%21---jetzt-zuschlagen-1534867671/)   | Mar 31, 14:31      |
|       715    |            67 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/komfortable-2--zimmer--altbauwohnung-%7C-unbefristet-%7C-ab-sofort-981340160/)                                         | Mar 31, 14:17      |
|       796.38 |            42 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/vollm%C3%B6bliert-gegen-abl%C3%B6se%21%21-neubauwohnung-mit-kl.-west-garten-und-gro%C3%9Fer-terrasse-1857977035/)      | Mar 31, 12:37      |
|       799    |            67 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/360-tour-/-gro%C3%9Fz%C3%BCgige-2-zimmer-altbauwohnung-in-guter-lage-des-10.-bezirks-1009168043/)                      | Mar 31, 12:36      |
|       797.55 |            59 |          2 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/beautiful-2-room-apartment-with-separate-kitchen-1404727785/)                                                            | Mar 31, 12:36      |
|       799.99 |            37 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/%2A%2A%2A2-zimmer-neubauwohnung-mit-stellplatz-nahe-therme-oberlaa%2A%2A%2A-1431876738/)                               | Mar 31, 11:26      |
|       799.79 |            44 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/attraktive-und-sch%C3%B6ne-2-zimmer-wohnung-in-der-r%C3%B6mergasse%21-1999381649/)                                     | Mar 31, 10:57      |
|       748    |            43 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/2-zimmerwohnung-im-2.og-mit-loggia-1888310546/)                                                                        | Mar 31, 10:53      |
|       781.81 |            54 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/2-zimmer-altbau-mit-guter-anbindung-785072780/)                                                                         | Mar 31, 10:46      |
|       710.66 |            71 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/hofseitige-2-zimmerwohnung-mit-allen-nebenr%C3%A4umen%2A%2A%2Aunbefristet%2A%2A%2A-1158573175/)                        | Mar 31, 09:27      |
|       670    |            42 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/gem%C3%BCtliche-2-zimmerwohnung-in-ottakring-1145584139/)                                                              | Mar 31, 09:26      |
|       613    |            41 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/helle-2-zimmerwohnung-in-top-lage-provisionsfrei-2142910840/)                                          | Mar 31, 08:19      |
|       740    |            72 |          4 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/4-zimmer-gemeindewohnung-1100-vormerkschein-2018%21%21%21%21-1269361159/)                                              | Mar 31, 07:37      |
|       475    |            43 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/2-zimmer-gemeindewohnung-in-top-zustand%21-direktvergabe-1083109868/)                                            | Mar 30, 23:24      |
|       420    |            41 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/gemeindewohnung-zur-vergabe-1140494205/)                                                                         | Mar 30, 22:07      |
|       480    |            47 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/gemeinde-wohnung-direktvergabe-1140-wien-1988096894/)                                                                    | Mar 30, 21:35      |
|       795    |            50 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/helle-2-zimmer-mit-balkon-1328093080/)                                                                                  | Mar 30, 19:40      |
|       750    |            45 |          2 | 05. Margareten           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/student:-innen-zur-untermiete-gesucht-%28nur-1-person%29-779443963/)                                                  | Mar 30, 18:09      |
|       750    |            38 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/ruhige-und-helle-2-zimmer-wohnung-mit-blick-in-den-innenhof-keine-provision-&-heizung-in-bk-inkludiert%21-1934789698/) | Mar 30, 17:12      |
