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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                          | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       560    |            50 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/1140-tiefendorfergasse-25-zimmer-duschbad-k%C3%BCche-1.-liftstock-hell-ruhelage-825609088/)                                                | Oct 25, 11:59      |
|       783.78 |            45 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/moderner-komfort-mit-aussicht:-balkonwohnung-in-top-lage-zu-einem-tollen-preis-1138917178/)                                              | Oct 25, 11:16      |
|       430.16 |            37 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/charmante-2-zimmer-wohnung-im-16.-bezirk---perfekte-lage-am-stillfriedplatz%21-1284449205/)                                              | Oct 25, 11:01      |
|       738.99 |            34 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/charmante-gartenwohnung-in-der-n%C3%A4he-der-seestadt%21-1628903492/)                                                                   | Oct 25, 10:47      |
|       749    |            34 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/charmante-wohnungen-in-der-n%C3%A4he-der-seestadt%21-1461597180/)                                                                       | Oct 25, 10:47      |
|       799.99 |            48 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/2-zimmer-wohnung-inkl.-k%C3%BCche-loggia-und-kellerabteil-u1-kagraner-platz---ausrichtung-wagramer-stra%C3%9Fe/w123-top-18-1628078437/) | Oct 25, 10:09      |
|       790    |            56 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/2-zimmer--vorzimmer-bad-wc-k%C3%BCche-abstellraum-kellerabteil-gartenben%C3%BCtzung-1707587163/)                                           | Oct 25, 08:19      |
|       740    |            49 |          2 | 23. Liesing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/wohnung-zu-vermieten-1302898128/)                                                                                                          | Oct 25, 08:12      |
|       624.94 |            49 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/ger%C3%A4umige-2-zimmer--wohnung-1685955371/)                                                                                            | Oct 25, 06:54      |
|       792.11 |            66 |          2 | 13. Hietzing             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1130-hietzing/ger%C3%A4umte-2-zimmer-bastlerwohnung-im-erdgeschoss-im-gr%C3%BCnen-1417910061/)                                                          | Oct 25, 06:50      |
|       550    |            50 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/saubere-gemeindewohnung-2-zimmer-1610180479/)                                                                                             | Oct 24, 23:15      |
|       685    |            65 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/ger%C3%A4umige-gemeindewohnung-im-14.-bezirk-zu-vergeben-868860133/)                                                                       | Oct 24, 22:29      |
|       627.34 |            59 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/gro%C3%9Fz%C3%BCgige-2-zimmer-wohnung-in-wien-21.-grellgasse---n%C3%A4he-marchfeldkanal-1171854672/)                                   | Oct 24, 21:52      |
|       728.21 |            35 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/wohnen-in-floridsdorf---2-zimmer-wohnung-mit-balkon-n%C3%A4he-shopping-city-nord-&-klink-floridsdorf-1885977017/)                      | Oct 24, 21:38      |
|       570    |            54 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/%28reserviert%29-gemeindewohnung-2-zimmer-direktvergabe-1552750719/)                                                     | Oct 24, 20:18      |
|       650    |            46 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/ideal-f%C3%BCr-singles-&-paare---2-zimmer-wohnung-zu-vermieten-1003400781/)                                                              | Oct 24, 19:54      |
|       679    |            38 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/urbanes-wohnen-in-deiner-neuen-2-zimmerwohnung-mit-balkon-im-wildgarten-1852290692/)                                                      | Oct 24, 19:42      |
|       599    |            57 |          3 | 20. Brigittenau          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1200-brigittenau/gemeinde-wohnung-1204539861/)                                                                                                          | Oct 24, 15:23      |
|       780    |            39 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/top-gepflegte-helle-2-zimmer-wohnung-mit-balkon-in-ruhiger-lage-1654625958/)                                                           | Oct 24, 15:07      |
|       725    |            46 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/roofjet:-tolle-2-zimmerwohnung-im-1.stock-sch%C3%B6nbrunn-n%C3%A4he-1262623521/)                                                           | Oct 24, 14:52      |
