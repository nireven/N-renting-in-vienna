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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                              | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       699.93 |            49 |          2 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/sonniges-&-gartenseitiges-2-zimmer-apartment-%28-bj-1993-%29-1247645128/)                                                                      | Dec 17, 09:47      |
|       640.01 |            33 |          2 | 09. Alsergrund           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/nette-2-zimmer--altbauwohnung-n%C3%A4he-w%C3%A4hringer-stra%C3%9Fe-1246524397/)                                                             | Dec 17, 09:26      |
|       562.31 |            43 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/atelier-:-%29---%3E.-ist-keine-mietwohnung-preiswert-&-aussergew%C3%B6hnlich---56231-eur-bruttomiete-993515347/)                             | Dec 17, 09:18      |
|       675.4  |            57 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/hofruhelage/-br%C3%BCnnerstra%C3%9Fe-helle-top-gepflegte-2-zimmer-altbauwohnung-1433733756/)                                               | Dec 17, 09:13      |
|       748.44 |            64 |          2 | 20. Brigittenau          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1200-brigittenau/erstbezug-nach-generalsanierung-1789071851/)                                                                                               | Dec 17, 09:13      |
|       644.86 |            52 |          2 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/sch%C3%B6ne-helle-2-zimmerwohnung-52m2%21-2024560741/)                                                                                         | Dec 17, 09:13      |
|       721.25 |            50 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/erstbezug-nach-sanierung:-2-zimmer-wohnung-im-gr%C3%BCnen-1763482013/)                                                                        | Dec 17, 02:45      |
|       600    |            46 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/suche-nachmieter-f%C3%BCr-eine-46m%C2%B2-altbauwohnung-in-der-n%C3%A4he-von-landstra%C3%9Fer-hauptstra%C3%9Fe-/-juchgasse-1911941489/) | Dec 16, 22:06      |
|       680    |            81 |          3 | 20. Brigittenau          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1200-brigittenau/gemeinde-wohnung-vormerkschein-31.05.2024-1850603245/)                                                                                     | Dec 16, 21:33      |
|       795    |            41 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/neubau-2-zimmer-%2B-loggia-/-u3-simmering-%28privat-provisionsfrei%29-2119696154/)                                                           | Dec 16, 21:03      |
|       795    |            80 |          3 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/%28reserviert%29-80-m%C2%B2-gemeindewohnung-mit-balkon-3-wohnr%C3%A4ume---direktvergabe-1272762783/)                                        | Dec 16, 20:51      |
|       490    |            47 |          2 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/2-zimmer-eckwohnung-1066730584/)                                                                                                               | Dec 16, 18:34      |
|       692.32 |            39 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/gepflegte-studentenwohnungen-mit-einbauk%C3%BCche-in-1210-zu-mieten-1317724224/)                                                           | Dec 16, 17:21      |
|       742.18 |            41 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/gepflegte-studentenwohnungen-mit-einbauk%C3%BCche-in-1210-zu-mieten-1764666987/)                                                           | Dec 16, 16:51      |
|       647.28 |            61 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/sanierte-gemeindewohnung---top-lage-u3&u6-2-zimmer-1138890487/)                                                              | Dec 16, 16:42      |
|       749.85 |            55 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/top-sanierte-2-zimmer-wohnung-mit-balkon-1316550728/)                                                                                          | Dec 16, 16:18      |
|       799    |            48 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/kolo-35---modernes-wohnen-beim-fac-platz-nahe-s-bahn-jedlersdorf-denglerpark-und-scn-1948773484/)                                          | Dec 16, 16:17      |
|       720    |            61 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/unbefristete-hauptmietwohnung-in-1150-wien-1698109630/)                                                                      | Dec 16, 14:59      |
|       743.33 |            43 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/2-zimmer-wohnung-inklusive-abstellraum%21-neubau-und-hochwertig---ab-01.03-1127569884/)                                                    | Dec 16, 14:58      |
|       799    |            60 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/2-zimmer-wohnung-inkl.-stellplatz-erstbezug-nach-sanierung%21-jetzt-anfragen%21-1389328021/)                                                | Dec 16, 14:57      |
