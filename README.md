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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                                                      | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       690    |            50 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/u6-meidling-bahnhof-%7C-unbefristet-%7C-2-zimmer-1630923804/)                                                                                                         | Jan 21, 15:58      |
|       540    |            50 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/gemeindewohnung-2064413350/)                                                                                                                                           | Jan 21, 15:34      |
|       749    |            44 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/perfekt-angelegte-2-zimmer-wohnung-hell-und-freundlich-150m-zur-u3-sackgasse-1269416129/)                                                                            | Jan 21, 15:27      |
|       543    |            50 |          2 | 20. Brigittenau          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1200-brigittenau/moderne-sanierte-&-sehr-ruhige-2-zimmer-altbauwohnung---u4-friedensbr%C3%BCcke-2126029473/)                                                                        | Jan 21, 15:24      |
|       625    |            47 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/sonnige-15-zimmer-altbaumiete-n%C3%A4he-sechshauserstra%C3%9Fe-877252103/)                                                                           | Jan 21, 15:00      |
|       457    |            43 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeindewohnung-direktvergabe-vormerkschein-vor-30.09.2024-1148048258/)                                                                                              | Jan 21, 14:09      |
|       799    |            43 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-neubauwohnung-inkl.-komplettk%C3%BCche-loggia-und-kellerabteil-bei-u1-neulaa-/hs17-a-14-825042242/)                                                         | Jan 21, 14:00      |
|       783.3  |            76 |          3 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeindewohnung-76m%C2%B2-in-direktvergabe-mit-vormerkschein-und-abl%C3%B6se-zu-vergeben-850662848/)                                                                 | Jan 21, 13:56      |
|       725    |            40 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/zuhause-in-der-wildgartenallee:-preiswerte-2-zimmerwohnung-mit-loggia-im-3.-og-ab-februar-1058477395/)                                                                | Jan 21, 13:41      |
|       694.02 |            62 |          2 | 02. Leopoldstadt         | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/ruhige-2-zimmer-wohnung-%2862m%C2%B2%29-1300985245/)                                                                                                              | Jan 21, 13:30      |
|       469.43 |            44 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/direktvergabe-gemeindewohnung-952593689/)                                                                                                                              | Jan 21, 13:10      |
|       733.49 |            68 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/direktvergabe-gemeindewohnung-2135053486/)                                                                                                           | Jan 21, 10:05      |
|       672.64 |            84 |          3 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/unbefristete-3-zimmer-wohnung-mit-guter-anbindung%21-1832730646/)                                                                                                    | Jan 21, 09:28      |
|       610    |            65 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/gemeinde-wohnung-%28direktvergabe%29-1938183637/)                                                                                                                  | Jan 21, 09:01      |
|       799    |            39 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1-monat-mietfrei:-erstbezug-im-gr%C3%BCnen-nahe-der-u2---zwischen-badeteich-hirschstetten-und-seestadt-981921692/)                                                  | Jan 21, 09:00      |
|       795    |            61 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/unbefristete-hauptmietwohnung-in-1110-wien-2009205611/)                                                                                                              | Jan 21, 08:31      |
|       615    |            60 |          3 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/gemeindewohnung-dirktvergabe-nur-mit-vormerkschein%21%21%21-1905996321/)                                                                                               | Jan 21, 07:37      |
|       729.21 |            33 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/exklusives-wohnen-in-stadlau---erzherzog-karl-stra%C3%9Fe-bahnhof-und-u2-stadlau-in-wenigen-gehminuten.---wohntraum-2131488813/)                                    | Jan 21, 06:55      |
|       749    |            31 |          2 | 19. Döbling              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1190-d%C3%B6bling/singlehit-in-d%C3%B6bling%21%21-1192271109/)                                                                                                                      | Jan 21, 04:36      |
|       714.82 |            39 |          2 | 23. Liesing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/wundersch%C3%B6ne-sonnendurchflutete-wohnung-mit-terrasse-im-23.-bezirk%21%21%21-n%C3%A4he-u6-perfektastra%C3%9Fe%21%21-360%C2%B0-grad-besichtigung%21%21-1650734977/) | Jan 21, 03:48      |
