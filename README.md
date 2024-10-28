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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                                             | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       635.87 |            48 |          2 | 20. Brigittenau          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1200-brigittenau/super-sch%C3%B6ne-stilaltbauwohnung%21-1704699933/)                                                                                                       | Oct 28, 17:55      |
|       789    |            48 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/toll-aufgeteilte-2-zimmer-wohnung-mit-balkon-in-ruhiger-lage-1174359063/)                                                                                     | Oct 28, 17:38      |
|       799    |            44 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/wohnen-zum-fairen-preis---wohnen-im-gr%C3%BCnen-und-doch-urban-%28u1-leopoldau-%2B-u6-floridsdorf%29---mit-vollm%C3%B6blierter-k%C3%BCche%21-1647352448/) | Oct 28, 17:36      |
|       780    |            40 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/preis-inkl.-heizung-von-privat:-tolle-studio-wohnung-in-ruhiger-lage-1243001313/)                                                                           | Oct 28, 17:28      |
|       760.31 |            60 |          2 | 05. Margareten           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/2-zimmer-wohnung-n%C3%A4he-wiedner-hauptstra%C3%9Fe-1122358245/)                                                                                           | Oct 28, 17:16      |
|       699.75 |            51 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/tolle-2-zimmerwohnung-an-der-u4%21-1867811360/)                                                                                             | Oct 28, 17:16      |
|       775    |            42 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/%2Aprovisionsfrei%2A-sch%C3%B6ne-lichtdurchflutete-2-zimmer-wohnung-1569081927/)                                                                            | Oct 28, 16:51      |
|       742.17 |            41 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/gepflegte-studentenwohnungen-mit-einbauk%C3%BCche-in-1210-zu-mieten-1764666987/)                                                                          | Oct 28, 16:51      |
|       780.3  |            35 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/singlehit-in-1210-wien-zu-mieten-1946913358/)                                                                                                             | Oct 28, 16:35      |
|       798.11 |            44 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/attraktive-und-sch%C3%B6ne-2-zimmer-wohnung-in-der-r%C3%B6mergasse%21-1026444880/)                                                                          | Oct 28, 15:26      |
|       638    |           nan |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/der-weitblick-von-den-dachterrassen-begeistert-1540369155/)                                                                                                  | Oct 28, 14:56      |
|       616    |           nan |          2 | 02. Leopoldstadt         | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/11-stockwerke-mit-traumhaften-wien-blick-1666407079/)                                                                                                    | Oct 28, 14:29      |
|       655    |            66 |          3 | 23. Liesing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/gemeindewohnung-1230-wien---direktvergabe-1816195797/)                                                                                                        | Oct 28, 14:15      |
|       799    |            44 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/1100-wien---hofseitige-neubauwohnung---u1-n%C3%A4he-keplerplatz-804318935/)                                                                                 | Oct 28, 14:00      |
|       690    |            44 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/provisionsfrei%21-ruhige-und-grossz%C3%BCgige-15-zimmer-wohnung-n%C3%A4he-b%C3%B6hmischer-prater-mit-toller-nahversorgung-1782063371/)                      | Oct 28, 13:59      |
|       627.77 |            48 |          2 | 20. Brigittenau          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1200-brigittenau/wohnung-im-20.bezirk:-top-objekt-mit-guter-infrastruktur-984183264/)                                                                                      | Oct 28, 13:26      |
|       497.65 |            42 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/provisionsfrei:-toprenovierter-42m%C2%B2-altbau-mit-einbauk%C3%BCche---u3-n%C3%A4he-1924517026/)                                                            | Oct 28, 12:57      |
|       799.85 |            43 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/ina---wohnanlage-am-leberberg-:-top-a3-41-776704156/)                                                                                                       | Oct 28, 12:18      |
|       762.56 |            40 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/ina---sonnige-wohnung-mit-loggia/balkon-:-top-a3-39-1499881145/)                                                                                            | Oct 28, 12:18      |
|       797.76 |            46 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/ina---wohnanlage-am-leberberg-:-top-a4-39-1306355823/)                                                                                                      | Oct 28, 12:18      |
