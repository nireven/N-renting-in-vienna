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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District     | Link                                                                                                                                                                                                                                | 📅 Published Date   |
|-------------:|--------------:|-----------:|:----------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       622    |            32 |          2 | 19. Döbling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1190-d%C3%B6bling/klein-sehr-fein-dachgeschoss-in-d%C3%B6bling.-privat%21-1431189775/)                                                                        | Nov 29, 15:07      |
|       775    |            48 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/%22flori-flats%22:-mietkauf-in-floridsdorf---idyllisches-wohnen-in-heurigengegend-737461147/)                                                | Nov 29, 14:45      |
|       770    |            49 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/stammersdorfer-wohnparadies:-mietwohnungen-mit-kaufoption-737459071/)                                                                        | Nov 29, 14:38      |
|       799    |            41 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/sonnige-2-zimmer-mit-klimaanlage-und-terrassse-%7C-ruhelage-%7C-badeteich-hirschstetten-in-fu%C3%9Fn%C3%A4he-2003519689/)                     | Nov 29, 14:29      |
|       637.06 |            45 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/1210-wien-leopoldauer-stra%C3%9Fe-top-12-45m%C2%B2-2-zimmer-fu%C3%9Fbodenheizung-einbauk%C3%BCche-balkon-2.-liftstock-erstbezug-2132158813/) | Nov 29, 14:27      |
|       699    |            38 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1220-wien---genochplatz---ab-1.02.2025---gepflegte-neubauwohnung-mit-komplettk%C3%BCche-1695343321/)                                          | Nov 29, 14:03      |
|       799.14 |            42 |          2 | 11. Simmering   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/winteraktion---erster-monat-mietfrei%21-moderne-2-zimmerwohnung-mit-balkon%21-1780493551/)                                                     | Nov 29, 13:36      |
|       690    |            60 |          2 | 12. Meidling    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/%2Aentz%C3%BCckender-neubau-in-hofruhelage%2A-1381779268/)                                                                                      | Nov 29, 13:05      |
|       775.94 |            44 |          2 | 23. Liesing     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/2--zimmer-neubauwohnung-inkl-k%C3%BCche-loggia-au%C3%9Fenfl%C3%A4che-und-kellerabteil---u6-siebenhirten-in-gehweite/-bg65-3-12-1191773339/)      | Nov 29, 12:56      |
|       630    |            40 |          2 | 16. Ottakring   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/charmante-2-zimmer-wohnung-in-ottakring-1007946507/)                                                                                           | Nov 29, 12:45      |
|       617.18 |            49 |          2 | 16. Ottakring   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/moderne-2-zimmer-wohnung%21-anfragen-nur-per-mail---keine-anrufe%21-986669716/)                                                                | Nov 29, 12:36      |
|       795    |            33 |          2 | 12. Meidling    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/privat-:-wundersch%C3%B6ne-ruhige-neubau-wohnung-mit-balkon-2-zimmer-738441518/)                                                                | Nov 29, 12:24      |
|       570    |            55 |          3 | 19. Döbling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1190-d%C3%B6bling/helle-&-renovierte-3-zimmer-gemeinde-wohnung-weiterzugeben-1939841424/)                                                                     | Nov 29, 11:31      |
|       762.37 |            50 |          2 | 13. Hietzing    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1130-hietzing/moderne-sehr-helle-2-zimmerwohnung-in-ober-st.veit%21-921874822/)                                                                               | Nov 29, 10:48      |
|       530    |            54 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/gemeindewohnung-in-wien-1210---direktvergabe-1772731732/)                                                                                    | Nov 29, 10:36      |
|       667.7  |            47 |          2 | 23. Liesing     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/helle-und-ruhige-2-zimmer-wohnung-%7C-zellmann-immobilien-2012782510/)                                                                           | Nov 29, 07:24      |
|       749    |            40 |          2 | 04. Wieden      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1040-wieden/2-zimmer-%22alt-wien-charme%22-1904230961/)                                                                                                       | Nov 29, 07:13      |
|       678.83 |            49 |          2 | 16. Ottakring   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/gem%C3%BCtliche-2-zimmer-wohnung-im-3.-og-2009648704/)                                                                                         | Nov 29, 02:49      |
|       760    |            40 |          2 | 09. Alsergrund  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/single-hit-wohnung-provisionsfrei-ca.-40m2-zwei-zimmer-wien-9.-bezirk-830436206/)                                                             | Nov 28, 22:27      |
|       655    |            64 |          3 | 14. Penzing     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/3---zimmer-gemeindewohnung-64m2-in-1140-wien-2130664628/)                                                                                        | Nov 28, 19:03      |
