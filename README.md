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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                                         | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       793.35 |            46 |          2 | 09. Alsergrund   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/neu%21-charmante-2-zimmerwohnung-im-herzen-des-9.-bezirks%21-4.-stock-ohne-lift%21-877268228/)                         | Nov 06, 12:37      |
|       749.13 |            40 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/2-zimmer-wohnung-in-zentraler-lage-zu-vermieten-1535156517/)                                                         | Nov 06, 12:36      |
|       699.94 |            48 |          2 | 21. Floridsdorf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/2-zimmer-in-floridsdorf-zu-vermieten-1118328844/)                                                                     | Nov 06, 12:07      |
|       730    |            49 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/wundersch%C3%B6ne-2-zimmerwohnung-direkt-bei-enkplatz-1302991049/)                                                      | Nov 06, 11:40      |
|       718.59 |            38 |          2 | 21. Floridsdorf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/neu%21-erstbezug%21-ideale-2-zimmer-neubauwohnung-mit-balkon%21-tiefgaragenstellpl%C3%A4tze-im-haus%21-1573233945/)   | Nov 06, 11:28      |
|       799    |            40 |          2 | 21. Floridsdorf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/moderne-2-zimmerwohnung-mit-balkon%21-1693093114/)                                                                    | Nov 06, 10:55      |
|       710    |            41 |          2 | 21. Floridsdorf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/neubau-2023%21-2-zimmer-wohnung-mit-balkon%21-1442632015/)                                                            | Nov 06, 10:09      |
|       720    |            44 |          2 | 21. Floridsdorf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/mietwohnung-genie%C3%9Fen-kaufoption-nutzen:-wohnen-in-stammersdorfer-naturkulisse-761411356/)                        | Nov 06, 10:07      |
|       730    |            37 |          2 | 21. Floridsdorf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/traumhaftes-wohnen:-mietwohnungen-mit-kaufoption-in-stammersdorfer-ruhelage-761411354/)                               | Nov 06, 10:07      |
|       729    |            33 |          2 | 22. Donaustadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/exklusives-wohnen-in-stadlau---erzherzog-karl-stra%C3%9Fe-bahnhof-und-u2-stadlau-in-wenigen-gehminuten%21-1283333646/) | Nov 06, 10:07      |
|       770    |            49 |          2 | 21. Floridsdorf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/jetzt-mieten-sp%C3%A4ter-kaufen:-wohnen-in-stammersdorfer-naturidylle-761411382/)                                     | Nov 06, 10:07      |
|       798.99 |            40 |          2 | 21. Floridsdorf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/moderne-neubauwohnung-mit-balkon-und-einbauk%C3%BCche%21-nahe-stra%C3%9Fenbahn-26-lorettowiese-und-scn-1740472691/)   | Nov 06, 09:59      |
|       798.99 |            40 |          2 | 21. Floridsdorf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/traumwohnungen-in-top-lage-zu-vermieten%21-1055837955/)                                                               | Nov 06, 09:48      |
|       798.11 |            44 |          2 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/attraktive-und-sch%C3%B6ne-2-zimmer-wohnung-in-der-r%C3%B6mergasse%21-903786679/)                                       | Nov 06, 09:36      |
|       740    |            75 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/hauptmiethit-n%C3%A4he-enkplatz-1743984088/)                                                                            | Nov 06, 09:07      |
|       790    |            37 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/moderne-2-zimmerwohnung-mit-guter-anbindung-2123513757/)                                                                | Nov 06, 03:28      |
|       552    |            49 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeindewohnung-2-zimmer-bei-u1-troststra%C3%9Fe-1858699341/)                                                           | Nov 05, 21:35      |
|       726.48 |            40 |          2 | 13. Hietzing     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1130-hietzing/moderne-2-zimmerwohnung-mit-eigenem-garten-in-hietzing-1467693919/)                                                      | Nov 05, 20:38      |
|       685.01 |            43 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/kleinod--erstbezug-in-hauptbahnhof-n%C3%A4he-1577186673/)                                                               | Nov 05, 20:33      |
|       695    |            43 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/zweizimmer-erstbezug-in-hauptbahnhof-n%C3%A4he-824306479/)                                                              | Nov 05, 19:35      |
