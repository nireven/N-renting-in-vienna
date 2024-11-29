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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                                | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       799    |            46 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/preiswerte-2-zimmerwohnung-mit-balkon-im-1.-og-im-gr%C3%BCner-umgebung-2009116743/)                                                             | Nov 29, 17:36      |
|       685.85 |            42 |          2 | 20. Brigittenau          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1200-brigittenau/%2Anatur-im-blick%2A-moderne-2-zimmer-wohnung-in-zentraler-lage-mit-u-bahn-anbindung-1722673767/)                                            | Nov 29, 17:26      |
|       600    |            38 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/2-zimmer-wohnung-mit-abstellraum-1138754327/)                                                                                                | Nov 29, 17:24      |
|       579    |            54 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/gemeinde-wohnung-922128962/)                                                                                                                     | Nov 29, 17:01      |
|       723    |            74 |          3 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/wiener-wohnen-direktvergabe-mit-vormerkschein-1804395621/)                                                                     | Nov 29, 16:15      |
|       598    |            57 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/provisionsfrei:-ruhiger-57m%C2%B2-altbau-mit-einbauk%C3%BCche-und-2-zimmern---u3-n%C3%A4he-2056154143/)                                        | Nov 29, 15:55      |
|       730    |           104 |          4 | 23. Liesing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/gemeindewohnung-4-zimmer-104-qm-in-wien-liesing-1250855382/)                                                                                     | Nov 29, 15:23      |
|       622    |            32 |          2 | 19. Döbling              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1190-d%C3%B6bling/klein-sehr-fein-dachgeschoss-in-d%C3%B6bling.-privat%21-1431189775/)                                                                        | Nov 29, 15:07      |
|       775    |            48 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/%22flori-flats%22:-mietkauf-in-floridsdorf---idyllisches-wohnen-in-heurigengegend-737461147/)                                                | Nov 29, 14:45      |
|       770    |            49 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/stammersdorfer-wohnparadies:-mietwohnungen-mit-kaufoption-737459071/)                                                                        | Nov 29, 14:38      |
|       799    |            41 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/sonnige-2-zimmer-mit-klimaanlage-und-terrassse-%7C-ruhelage-%7C-badeteich-hirschstetten-in-fu%C3%9Fn%C3%A4he-2003519689/)                     | Nov 29, 14:29      |
|       637.06 |            45 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/1210-wien-leopoldauer-stra%C3%9Fe-top-12-45m%C2%B2-2-zimmer-fu%C3%9Fbodenheizung-einbauk%C3%BCche-balkon-2.-liftstock-erstbezug-2132158813/) | Nov 29, 14:27      |
|       699    |            38 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1220-wien---genochplatz---ab-1.02.2025---gepflegte-neubauwohnung-mit-komplettk%C3%BCche-1695343321/)                                          | Nov 29, 14:03      |
|       799.14 |            42 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/winteraktion---erster-monat-mietfrei%21-moderne-2-zimmerwohnung-mit-balkon%21-1780493551/)                                                     | Nov 29, 13:36      |
|       690    |            60 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/%2Aentz%C3%BCckender-neubau-in-hofruhelage%2A-1381779268/)                                                                                      | Nov 29, 13:05      |
|       775.94 |            44 |          2 | 23. Liesing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/2--zimmer-neubauwohnung-inkl-k%C3%BCche-loggia-au%C3%9Fenfl%C3%A4che-und-kellerabteil---u6-siebenhirten-in-gehweite/-bg65-3-12-1191773339/)      | Nov 29, 12:56      |
|       630    |            40 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/charmante-2-zimmer-wohnung-in-ottakring-1007946507/)                                                                                           | Nov 29, 12:45      |
|       617.18 |            49 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/moderne-2-zimmer-wohnung%21-anfragen-nur-per-mail---keine-anrufe%21-986669716/)                                                                | Nov 29, 12:36      |
|       795    |            33 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/privat-:-wundersch%C3%B6ne-ruhige-neubau-wohnung-mit-balkon-2-zimmer-738441518/)                                                                | Nov 29, 12:24      |
|       570    |            55 |          3 | 19. Döbling              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1190-d%C3%B6bling/helle-&-renovierte-3-zimmer-gemeinde-wohnung-weiterzugeben-1939841424/)                                                                     | Nov 29, 11:31      |
