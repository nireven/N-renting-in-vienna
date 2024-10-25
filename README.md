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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District     | Link                                                                                                                                                                                                                           | 📅 Published Date   |
|-------------:|--------------:|-----------:|:----------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       799    |            62 |          2 | 11. Simmering   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/sonnige--bezugsfertige-2-zimmer-balkonmietegr%C3%BCnruhelage-1466824477/)                                                                 | Oct 25, 16:06      |
|       788.76 |            76 |          3 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/direktvergabe-3-zimmer-gemeindewohnung-1220833662/)                                                                                     | Oct 25, 15:51      |
|       785.58 |            53 |          2 | 14. Penzing     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/linzer-stra%C3%9Fe---2-zimmer-neubau-wohnung-zu-vermieten-776282649/)                                                                       | Oct 25, 15:40      |
|       790    |            46 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/ihr-zuhause-in-stammersdorfer-ruhelage:-mietwohnung-mit-kaufoption-737463696/)                                                          | Oct 25, 14:55      |
|       775    |            48 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/%22flori-flats%22:-mietkauf-in-floridsdorf---idyllisches-wohnen-in-heurigengegend-737461147/)                                           | Oct 25, 14:45      |
|       799.99 |            40 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/neubau-erstbezug-im-gr%C3%BCnen-nahe-u2-&-26er:-zwischen-badeteich-hirschstetten-und-seestadt-aspern-1010489877/)                        | Oct 25, 14:41      |
|       770    |            49 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/stammersdorfer-wohnparadies:-mietwohnungen-mit-kaufoption-737459071/)                                                                   | Oct 25, 14:38      |
|       790.58 |            41 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/wundersch%C3%B6ne-neue-2-zimmer-wohnung-beim-bahnhof-floridsdorf%21-987143137/)                                                         | Oct 25, 13:58      |
|       799.14 |            42 |          2 | 11. Simmering   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/winteraktion---erster-monat-mietfrei%21-moderne-2-zimmerwohnung-mit-balkon%21-1780493551/)                                                | Oct 25, 13:36      |
|       561.11 |            41 |          2 | 12. Meidling    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/in-sanierung---n%C3%A4he-u4-/-u6-ii-terrasse-im-garten-ii-2-zimmer-mit-separater-k%C3%BCche-ii-beim-gaudenzdorfer-g%C3%BCrtel-1073028439/) | Oct 25, 13:27      |
|       650    |            72 |          3 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/gemeindewohnung-direktvergabe-reserviert-1250785208/)                                                                                   | Oct 25, 13:19      |
|       749.05 |            59 |          2 | 20. Brigittenau | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1200-brigittenau/super-helle-2-zimmer-stilaltbauwohnung---n%C3%A4he-u6-j%C3%A4gerstra%C3%9Fe-%21-1693131218/)                                            | Oct 25, 13:06      |
|       560    |            50 |          2 | 14. Penzing     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/1140-tiefendorfergasse-25-zimmer-duschbad-k%C3%BCche-1.-liftstock-hell-ruhelage-825609088/)                                                 | Oct 25, 11:59      |
|       783.78 |            45 |          2 | 11. Simmering   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/moderner-komfort-mit-aussicht:-balkonwohnung-in-top-lage-zu-einem-tollen-preis-1138917178/)                                               | Oct 25, 11:16      |
|       430.16 |            37 |          2 | 16. Ottakring   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/charmante-2-zimmer-wohnung-im-16.-bezirk---perfekte-lage-am-stillfriedplatz%21-1284449205/)                                               | Oct 25, 11:01      |
|       749    |            34 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/charmante-wohnungen-in-der-n%C3%A4he-der-seestadt%21-1461597180/)                                                                        | Oct 25, 10:47      |
|       738.99 |            34 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/charmante-gartenwohnung-in-der-n%C3%A4he-der-seestadt%21-1628903492/)                                                                    | Oct 25, 10:47      |
|       799.99 |            48 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/2-zimmer-wohnung-inkl.-k%C3%BCche-loggia-und-kellerabteil-u1-kagraner-platz---ausrichtung-wagramer-stra%C3%9Fe/w123-top-18-1628078437/)  | Oct 25, 10:09      |
|       790    |            56 |          2 | 14. Penzing     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/2-zimmer--vorzimmer-bad-wc-k%C3%BCche-abstellraum-kellerabteil-gartenben%C3%BCtzung-1707587163/)                                            | Oct 25, 08:19      |
|       740    |            49 |          2 | 23. Liesing     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/wohnung-zu-vermieten-1302898128/)                                                                                                           | Oct 25, 08:12      |
