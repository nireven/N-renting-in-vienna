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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                                                                                          | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       798.11 |            44 |          2 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/attraktive-und-sch%C3%B6ne-2-zimmer-wohnung-in-der-r%C3%B6mergasse%21-1026444880/)                                                                                       | Oct 28, 15:26      |
|       638    |           nan |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/der-weitblick-von-den-dachterrassen-begeistert-1540369155/)                                                                                                               | Oct 28, 14:56      |
|       616    |           nan |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/11-stockwerke-mit-traumhaften-wien-blick-1666407079/)                                                                                                                 | Oct 28, 14:29      |
|       655    |            66 |          3 | 23. Liesing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/gemeindewohnung-1230-wien---direktvergabe-1816195797/)                                                                                                                     | Oct 28, 14:15      |
|       799    |            44 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/1100-wien---hofseitige-neubauwohnung---u1-n%C3%A4he-keplerplatz-804318935/)                                                                                              | Oct 28, 14:00      |
|       690    |            44 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/provisionsfrei%21-ruhige-und-grossz%C3%BCgige-15-zimmer-wohnung-n%C3%A4he-b%C3%B6hmischer-prater-mit-toller-nahversorgung-1782063371/)                                   | Oct 28, 13:59      |
|       627.77 |            48 |          2 | 20. Brigittenau  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1200-brigittenau/wohnung-im-20.bezirk:-top-objekt-mit-guter-infrastruktur-984183264/)                                                                                                   | Oct 28, 13:26      |
|       497.65 |            42 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/provisionsfrei:-toprenovierter-42m%C2%B2-altbau-mit-einbauk%C3%BCche---u3-n%C3%A4he-1924517026/)                                                                         | Oct 28, 12:57      |
|       797.76 |            46 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/ina---wohnanlage-am-leberberg-:-top-a4-39-1306355823/)                                                                                                                   | Oct 28, 12:18      |
|       762.56 |            40 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/ina---sonnige-wohnung-mit-loggia/balkon-:-top-a3-39-1499881145/)                                                                                                         | Oct 28, 12:18      |
|       799.85 |            43 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/ina---wohnanlage-am-leberberg-:-top-a3-41-776704156/)                                                                                                                    | Oct 28, 12:18      |
|       710    |            61 |          2 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/ruhige-wohnung-in-guter-lage-1343079052/)                                                                                                                                | Oct 28, 12:10      |
|       789    |            41 |          2 | 22. Donaustadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/moderne-neubauwohnungen-nahe-u1-kagraner-platz---aufstrebendes-wohnviertel-991040077/)                                                                                  | Oct 28, 11:58      |
|       495    |            43 |          2 | 05. Margareten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/gemeindewohnung-direktvergabe:-letztmaliges-angebot:-abl%C3%B6se-%E2%82%AC-1500-f%C3%BCr-m%C3%B6blierte-43m2-wohnung-1163696543/)                                       | Oct 28, 11:50      |
|       798.58 |            45 |          2 | 21. Floridsdorf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/leo-131---sonnige-neubauwohnung-mit-s%C3%BCdbalkon-und-k%C3%BCche---10-minuten-zu-u6-und-s-bahn-floridsdorf-sowie-siemensstra%C3%9Fe-bahnhof.---wohntraum-1042336912/) | Oct 28, 11:19      |
|       730    |            42 |          2 | 23. Liesing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/basler-gasse---neubau-erstbez%C3%BCge-mit-garage-in-1230-wien-1215481577/)                                                                                                 | Oct 28, 11:19      |
|       695    |            39 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/wundersch%C3%B6ne-2-zimmer-wohnung-in-top-lage-1590133781/)                                                                                                              | Oct 28, 11:03      |
|       779.99 |            46 |          2 | 23. Liesing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/2-zimmerwohnung---dachterrasse---einbauk%C3%BCche-1847041513/)                                                                                                             | Oct 28, 11:01      |
|       746.09 |            44 |          2 | 21. Floridsdorf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/moderne-2-zimmerwohnung---nahe-der-alten-donau-953832565/)                                                                                                             | Oct 28, 10:37      |
|       790    |            55 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gut-geschnittene-2-zimmer-wohnung-direkt-bei-der-ubahn---ab-sofort%21-1495581085/)                                                                                       | Oct 28, 10:08      |
