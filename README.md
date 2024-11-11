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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                                                    | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       559    |            45 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/zwei-zimmerwohnung-n%C3%A4he-hauptbahnhof%21-1028523875/)                                                                          | Nov 11, 16:16      |
|       690    |            53 |          2 | 18. Währing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1180-w%C3%A4hring/befristete-hochparterre-loggia-wohnung-ohne-k%C3%BCche-1337941615/)                                                             | Nov 11, 16:09      |
|       623.73 |            51 |          2 | 17. Hernals      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/provisionsfrei:-unbefristeter-51m%C2%B2-altbau-mit-einbauk%C3%BCche---1170-wien-1474648056/)                                         | Nov 11, 15:57      |
|       799    |            39 |          2 | 03. Landstraße   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/rennweg:-ruhige-hofseitige-zweizimmerwohnung-in-sehr-zentraler-lage-1434298105/)                                             | Nov 11, 14:54      |
|       763.58 |            51 |          2 | 23. Liesing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/sanierte-2-zimmerwohnung-in-rodaun-1765009507/)                                                                                      | Nov 11, 14:38      |
|       695    |            53 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-wohnung-am-columbusplatz---n%C3%A4he-hauptbahnhof-und-u1-keplerplatz-2103889381/)                                         | Nov 11, 14:03      |
|       769    |            40 |          2 | 22. Donaustadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1220-wien---kirschbl%C3%BCtenpark---u1-n%C3%A4he---hofseitige-gepflegte-balkonwohnung---ab-1.02.2025-1348008516/)                 | Nov 11, 14:00      |
|       550.53 |            50 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/%2B%2B%2B-wiener-wohnen-vms-31.10.2024-direktvergabe-2-zimmer-gemeindewohnung-2.-bezirk-direkt-am-donaukanal-1085693727/)       | Nov 11, 13:00      |
|       770    |            41 |          2 | 19. Döbling      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1190-d%C3%B6bling/studioappartement-im-souterrain-814302408/)                                                                                     | Nov 11, 12:36      |
|       759    |            54 |          2 | 17. Hernals      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/sch%C3%B6ne-2-zimmerwohnung-in-ruhiger-lage-1102021958/)                                                                             | Nov 11, 12:29      |
|       762.56 |            40 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/ina---sonnige-wohnung-mit-loggia/balkon-:-top-a3-39-1499881145/)                                                                   | Nov 11, 12:18      |
|       799.85 |            43 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/ina---wohnanlage-am-leberberg-:-top-a3-41-776704156/)                                                                              | Nov 11, 12:18      |
|       797.76 |            46 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/ina---wohnanlage-am-leberberg-:-top-a4-39-1306355823/)                                                                             | Nov 11, 12:18      |
|       729.97 |            37 |          2 | 22. Donaustadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/esslingliving---ihr-neues-zuhause:-gek%C3%BChlte-2-zimmer-wohnung-mit-terrasse-%7C-ausgezeichnete-anbindung-1679703444/)          | Nov 11, 12:02      |
|       789    |            41 |          2 | 22. Donaustadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/moderne-neubauwohnungen-nahe-u1-kagraner-platz---aufstrebendes-wohnviertel-991040077/)                                            | Nov 11, 11:58      |
|       770    |            46 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/ihr-neuer-lieblingsort:-viola-park---2-zimmer-wohnung-mit-gem%C3%BCtlichem-balkon-%7C-am-laaer-berg-960899048/)                    | Nov 11, 11:55      |
|       790    |            48 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/viola-park---ihre-wohlf%C3%BChloase-am-laaer-berg-%7C-freiraum-genie%C3%9Fen:-2-zimmer-mit-terrasse-2043360015/)                   | Nov 11, 11:55      |
|       790    |            50 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/wohnen-im-gr%C3%BCnen---viola-park:-2-zimmer-wohnung-mit-gro%C3%9Fem-balkon-%7C-wohlf%C3%BChloase-am-laaer-berg-1747205449/)       | Nov 11, 11:55      |
|       790    |            47 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/stilvolles-2-zimmer-apartment-mit-sonniger-terrasse---viola-park---ihre-wohlf%C3%BChloase-am-laaer-berg-1518345975/)               | Nov 11, 11:55      |
|       495    |            43 |          2 | 05. Margareten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/gemeindewohnung-direktvergabe:-letztmaliges-angebot:-abl%C3%B6se-%E2%82%AC-1500-f%C3%BCr-m%C3%B6blierte-43m2-wohnung-1163696543/) | Nov 11, 11:50      |
