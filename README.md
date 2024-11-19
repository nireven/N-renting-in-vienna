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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District     | Link                                                                                                                                                                                                                                        | 📅 Published Date   |
|-------------:|--------------:|-----------:|:----------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       748.62 |            40 |          2 | 11. Simmering   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/ina---wohnanlage-am-leberberg-:-top-a2-18-1851487966/)                                                                                                 | Nov 19, 12:08      |
|       769.07 |            44 |          2 | 17. Hernals     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/wohnung-mit-grosser-wohnk%C3%BCche-zu-mieten%21-878432123/)                                                                                              | Nov 19, 12:08      |
|       755.72 |            43 |          2 | 11. Simmering   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/ina---wohnanlage-am-leberberg-:-top-a2-05-2146745975/)                                                                                                 | Nov 19, 12:08      |
|       790    |            49 |          2 | 10. Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-wohnung-mit-balkon-im-viola-park-874541985/)                                                                                                  | Nov 19, 12:02      |
|       770    |            47 |          2 | 10. Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-wohnung-mit-balkon-im-viola-park-1841570745/)                                                                                                 | Nov 19, 12:00      |
|       799    |            43 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/wien---1220---31m%C2%B2-terrassentraum---u1-n%C3%A4he-kagranerplatz---neubau---ab-15.12.2025-1927445904/)                                             | Nov 19, 11:03      |
|       728.22 |            35 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/%2A%2A%2Awohnen-in-floridsdorf---2-zimmer-wohnung-mit-balkon-und-garagenplatz-n%C3%A4he-shopping-city-nord-&-klink-floridsdorf%2A%2A%2A-1058867222/) | Nov 19, 10:58      |
|       790    |            41 |          2 | 17. Hernals     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/sch%C3%B6ne-neubauwohnung---1-schlafzimmer-1-wohnk%C3%BCche-mit-kleinem-balkon-992656530/)                                                               | Nov 19, 10:22      |
|       740    |            52 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/hell-freundlich-zwei-zentral-begehbare-zimmer-n%C3%A4he-alte-donau%21-1001974147/)                                                                   | Nov 19, 10:08      |
|       725    |            43 |          2 | 10. Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-wohnung-im-10.bezirk---renovierter-altbau---gute-anbindung-und-infrastruktur-1894245947/)                                                     | Nov 19, 09:17      |
|       580    |            55 |          2 | 10. Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/wiener-wohnen-1442608621/)                                                                                                                             | Nov 19, 08:13      |
|       749    |            46 |          2 | 23. Liesing     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/ruhige-25-zimmerwohnung-in-guter-lage-%7C-zellmann-immobilien-2017122355/)                                                                               | Nov 19, 07:35      |
|       572.84 |            48 |          2 | 14. Penzing     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/helle-und-ruhig-terrassengeschoss-wohnung-1301878953/)                                                                                                   | Nov 19, 02:39      |
|       499    |            42 |          2 | 05. Margareten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/liebevolle-2-zimmer-wohnung-in-%2A1050-wien%2A---nahe-wiedner-hauptstra%C3%9Fe-%2Aperfekte-studentinnenwohnung%2A-896652795/)                         | Nov 19, 00:41      |
|       669    |            43 |          2 | 03. Landstraße  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/anfragestopp%21%21-hofseitige-wohnung-im-3.-bezirk-n%C3%A4he-praterallee-1013268207/)                                                            | Nov 18, 21:47      |
|       598    |            61 |          2 | 20. Brigittenau | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1200-brigittenau/moderne-wohnung-mit-balkon-zu-vergeben-in-1200-wien-%28vormerkschein-30.09.24%29-1928293060/)                                                        | Nov 18, 21:20      |
|       769    |            38 |          2 | 19. Döbling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1190-d%C3%B6bling/2---zimmerwohnung-n%C3%A4he-w%C3%A4hringerpark-729834170/)                                                                                          | Nov 18, 21:07      |
|       725    |            40 |          2 | 12. Meidling    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/neubau-ab-01.02.-beziehbar:-sch%C3%B6ne-2-zimmerwohnung-mit-loggia-im-3.-og-2055199338/)                                                                | Nov 18, 19:32      |
|       717    |            76 |          3 | 12. Meidling    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/3-zimmer-neubauwohnung-in-1120-wien-2133282769/)                                                                                                        | Nov 18, 19:32      |
|       786.09 |            43 |          2 | 10. Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/freundliche-helle-altbauwohnung-wg-geeignet---2-getrennte-schlafr%C3%A4ume-2097308034/)                                                                | Nov 18, 17:47      |
