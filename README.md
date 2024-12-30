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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District     | Link                                                                                                                                                                                                                                    | 📅 Published Date   |
|-------------:|--------------:|-----------:|:----------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       795    |            80 |          3 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/%28reserviert%29-80-m%C2%B2-gemeindewohnung-mit-balkon-3-wohnr%C3%A4ume---direktvergabe-1272762783/)                                              | Dec 30, 20:51      |
|       496.96 |            49 |          2 | 13. Hietzing    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1130-hietzing/direktvergabe-ger%C3%A4umige-2-zimmer-gemeindewohnung-im-13.-bezirk-mit-ausblick-ins-gr%C3%BCne-1874911032/)                                        | Dec 30, 19:09      |
|       798.79 |            43 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/komfortabler-erstbezug:-2-zimmer-wohnungen-im-21.-bezirk-mit-balkon-und-moderner-k%C3%BCche---jetzt-anfragen-1638831855/)                        | Dec 30, 18:56      |
|       728.83 |            34 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/exklusives-wohnen-in-stadlau---erzherzog-karl-stra%C3%9Fe-bahnhof-und-u2-stadlau-in-wenigen-gehminuten.---wohntraum-1875264800/)                  | Dec 30, 18:56      |
|       479    |            46 |          2 | 19. Döbling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1190-d%C3%B6bling/vormerkschein-bzw.-wiener-wohnticket-f%C3%BCr-2-zimmer---30.11.2024.-1273072554/)                                                               | Dec 30, 18:56      |
|       692.32 |            39 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/gepflegte-studentenwohnungen-mit-einbauk%C3%BCche-in-1210-zu-mieten-1317724224/)                                                                 | Dec 30, 17:21      |
|       742.18 |            41 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/gepflegte-studentenwohnungen-mit-einbauk%C3%BCche-in-1210-zu-mieten-1764666987/)                                                                 | Dec 30, 16:51      |
|       762    |            55 |          2 | 10. Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/bitte-nur-schriftliche-anfragen-keine-anrufe.-unbefristete-h%C3%BCbsche-2-zimmer-wohnung-in-der-pernerstorfergasse-1570761075/)                    | Dec 30, 16:24      |
|       750    |            56 |          2 | 10. Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/provisionsfrei-fernkorngasse-interessante-attraktive-teilm%C3%B6blierte-2-zimmer-wohnung-in-guter-lage-matzleinsdorferplatz-n%C3%A4he-2102019983/) | Dec 30, 16:21      |
|       799    |            48 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/kolo-35---modernes-wohnen-beim-fac-platz-nahe-s-bahn-jedlersdorf-denglerpark-und-scn-1948773484/)                                                | Dec 30, 16:17      |
|       795.19 |            41 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/moderne-neubauwohnungen-nahe-u1-kagraner-platz---aufstrebendes-wohnviertel-1517264677/)                                                           | Dec 30, 16:16      |
|       795.19 |            41 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/moderne-neubauwohnung-mit-gro%C3%9Fem-balkon-und-abstellraum-nahe-u1-kagraner-platz---im-neuen-wohnviertel-am-langen-felde-1911782186/)           | Dec 30, 15:35      |
|       743.33 |            43 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/2-zimmer-wohnung-inklusive-abstellraum%21-neubau-und-hochwertig---ab-01.03-1127569884/)                                                          | Dec 30, 14:58      |
|       799    |            60 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/2-zimmer-wohnung-inkl.-stellplatz-erstbezug-nach-sanierung%21-jetzt-anfragen%21-1389328021/)                                                      | Dec 30, 14:57      |
|       798    |            37 |          2 | 20. Brigittenau | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1200-brigittenau/sehr-sch%C3%B6ne-2-zimmerwohnung---n%C3%A4he-donauinsel-&-handelskai-1066009313/)                                                                | Dec 30, 14:15      |
|       729.82 |            60 |          2 | 23. Liesing     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/kuschlig-wohnen-im-zentrum-von-liesing-1880260887/)                                                                                                  | Dec 30, 13:34      |
|       790    |            47 |          2 | 10. Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/stilvolles-2-zimmer-apartment-mit-sonniger-terrasse---viola-park---ihre-wohlf%C3%BChloase-am-laaer-berg-1518345975/)                               | Dec 30, 11:55      |
|       790    |            48 |          2 | 10. Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/viola-park---ihre-wohlf%C3%BChloase-am-laaer-berg-%7C-freiraum-genie%C3%9Fen:-2-zimmer-mit-terrasse-2043360015/)                                   | Dec 30, 11:55      |
|       779    |            48 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/ab-1.1.2025---1220-wien---neubauwohnung-inkl.-komplettk%C3%BCche-mit-perfektem-grundriss-und-gro%C3%9Fz%C3%BCgigem-balkon-1303837320/)            | Dec 30, 11:02      |
|       522    |            45 |          2 | 19. Döbling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1190-d%C3%B6bling/gemeindewohnung/-wiener-wohnen---direktvergabe-1299701607/)                                                                                     | Dec 30, 10:49      |
