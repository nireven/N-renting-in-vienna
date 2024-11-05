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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                             | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       629.42 |            46 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/2-zimmer-wohnung-im-12.-bezirk---provisionsfrei-814785608/)                                                                  | Nov 05, 10:57      |
|       728    |            52 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/unbefristet-neubau-hofherrgasse-1432332544/)                                                                                | Nov 05, 10:56      |
|       585    |            39 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/entz%C3%BCckende-altbauwohnung-in-ruhiger-lage-n%C3%A4he-mariahilferstrasse-zwischen-u3-und-u6-1419243284/) | Nov 05, 10:10      |
|       740    |            52 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/hell-freundlich-zwei-zentral-begehbare-zimmer-n%C3%A4he-alte-donau%21-1001974147/)                                        | Nov 05, 10:08      |
|       762.37 |            50 |          2 | 13. Hietzing             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1130-hietzing/moderne-sehr-helle-2-zimmerwohnung-in-ober-st.veit%21-966171344/)                                                            | Nov 05, 09:40      |
|       725    |            43 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-wohnung-im-10.bezirk---renovierter-altbau---gute-anbindung-und-infrastruktur-1894245947/)                          | Nov 05, 09:17      |
|       515    |            50 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-gemeindewohnung-direktvergabe-vmd-31.10.24-1942982013/)                                                            | Nov 05, 09:10      |
|       690    |            43 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/2-zimmerwohnung-ab-sofort-zu-vermieten-1686215108/)                                                                          | Nov 05, 09:06      |
|       779    |            44 |          2 | 20. Brigittenau          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1200-brigittenau/wohnung-im-bestzustand---kompakte-2-zimmer-f%C3%BCr-unter-800eur-827709437/)                                              | Nov 05, 08:28      |
|       794.63 |            53 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/ina-%E2%97%8F-die-ecke-hat-mehr-charme-:-b3-07-1611092922/)                                                                 | Nov 05, 08:07      |
|       767.37 |            49 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/ina---wohnanlage-am-leberberg-:-top-b4-17-1348924799/)                                                                      | Nov 05, 08:07      |
|       782.71 |            50 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/designerwohnung-in-einem-wundersch%C3%B6nen-neu-renovierten-gr%C3%BCnderzeithaus-1182456647/)                                 | Nov 05, 07:10      |
|       798.91 |            60 |          2 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/ger%C3%A4umige-2-zimmer--wohnung-1530891048/)                                                                                 | Nov 05, 06:52      |
|       749    |            44 |          2 | 18. Währing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1180-w%C3%A4hring/reizende-stilaltbauwohnung-nahe-kutschkermarkt-1005235341/)                                                              | Nov 05, 03:29      |
|       782    |            43 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/tolle-2-zimmer-wohnung-in-absoluter-ruhelage-mit-sch%C3%B6nem-balkon-1191538653/)                                             | Nov 05, 03:21      |
|       760    |            40 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/klein-fein-zentral-voll-ausgestattet-1698014439/)                                                           | Nov 04, 21:27      |
|       680    |            44 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/privat%21-2-zimmerwohnung-zu-vermieten-1865971676/)                                                                         | Nov 04, 21:22      |
|       725    |            40 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/neubau-ab-01.02.-beziehbar:-sch%C3%B6ne-2-zimmerwohnung-mit-loggia-im-3.-og-2055199338/)                                     | Nov 04, 19:32      |
|       466.28 |            43 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/gemeindewohnung-mit-vormerkschein-01.11.24-2045459672/)                                                                   | Nov 04, 18:48      |
|       799    |            41 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-wohnung-mit-blick-auf-den-stephansdom---ab-15.12.2024-beziehbar%21-1125235828/)                                    | Nov 04, 18:35      |
