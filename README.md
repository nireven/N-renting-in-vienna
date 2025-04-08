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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                                                     | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       698.92 |            63 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/----2-zimmerwohnung-im-dachgeschoss-%2A1-minute-zur-u2-taborstra%C3%9Fe%2A-----1734539458/)                                      | Apr 08, 11:48      |
|       644.01 |            61 |          2 | 14. Penzing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/sehr-helle-2-zimmer-altbauwohnung---n%C3%A4he-sch%C3%B6nbrunn-810256197/)                                                             | Apr 08, 10:36      |
|       670    |            62 |          3 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/wiener-wohnen-vormerkschein--wundersch%C3%B6ne-gemeindewohnung-in-1110-wien-mit-balkon-als-direktvergabe-weiterzugeben-1625662973/) | Apr 08, 05:47      |
|       700    |            47 |          2 | 17. Hernals      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/wohnung-zum-wohlf%C3%BChlen-1842133416/)                                                                                              | Apr 07, 22:04      |
|       402.66 |            56 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/zwei-zimmer-gemeindewohnung-mit-vormerkschein-vor-31.03.25-1922540623/)                                                             | Apr 07, 21:06      |
|       799    |            45 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/sonnwend---living%21-erstbezug---k%C3%BCche---klima---beschattung---u1-n%C3%A4he%21-1661379415/)                                    | Apr 07, 20:38      |
|       599.79 |            41 |          2 | 17. Hernals      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/h%C3%BCbsche-15-zimmer-wohnung-am-clemens-hofbauer-platz-1887758100/)                                                                 | Apr 07, 20:33      |
|       459.32 |            44 |          2 | 03. Landstraße   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/u-bahn--und-pratern%C3%A4he-2-zimmer-gemeinde-wohnung%3B-ruhig-sch%C3%B6n-gut-gelegen-1815209405/)                            | Apr 07, 16:18      |
|       720    |            54 |          2 | 17. Hernals      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/2-zimmer-hauptmiete-%22unbefristet%22-1860207122/)                                                                                    | Apr 07, 14:39      |
|       679    |            43 |          2 | 05. Margareten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/renovierte-unbefristete-altbaumiete-976442915/)                                                                                    | Apr 07, 13:38      |
|       760    |            56 |          2 | 14. Penzing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/ruhige-helle-2-zimmer-wohnung-mit-loggia-in-penzing-1324810104/)                                                                      | Apr 07, 11:55      |
|       715    |            74 |          3 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/helle-und-g%C3%BCnstige-3-zimmer-wohnung-2109468448/)                                                                               | Apr 07, 11:10      |
|       799    |            67 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/360-tour-/-gro%C3%9Fz%C3%BCgige-2-zimmer-altbauwohnung-in-guter-lage-des-10.-bezirks-1201309134/)                                   | Apr 07, 11:00      |
|       795    |            43 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/helle-2-zimmer-wohnung-mit-balkon-im-wildgarten-%281120%29-1526541523/)                                                              | Apr 07, 10:53      |
