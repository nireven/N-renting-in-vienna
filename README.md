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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                                   | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       520    |            50 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/gemeindewohnung-zu-vergeben---2-zimmer-balkon-teilm%C3%B6bliert---mit-vormerkschein-1306684366/)               | May 05, 20:59      |
|       408    |            56 |          3 | 03. Landstraße   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/wiener-wohnen-direktvergabe-vormerkschein-29.04.2024-3-zimmer-1682915199/)                                  | May 05, 18:42      |
|       693    |            50 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/ruhige-renovierte-neubauwohnung-hofseitig-1775181648/)                                                            | May 05, 17:56      |
|       786    |            56 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/hauptbahnhof-u1-wenige-meter-fussg%C3%A4ngerzone-2112264378/)                                                     | May 05, 16:58      |
|       697.96 |            42 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/provisionsfreie-2-zimmer-wohnung-in-meidling-1398414697/)                                                          | May 05, 16:19      |
|       749.78 |            47 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/sch%C3%B6ne-2-zimmer-wohnung-n%C3%A4he-sch%C3%B6nbrunner-schlosspark%21-1257201030/)                               | May 05, 15:27      |
|       738    |            40 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/%2A%2A%2A%2A%2Akleine-mietwohnung-mit-balkon%2A%2A%2A%2A%2A-1121261867/)                                          | May 05, 15:17      |
|       568.89 |            47 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/wundersch%C3%B6ne-unbefristete-2-zimmer-wohnung-in-ruhiger-lage-n%C3%A4he-meidlinger-hauptstra%C3%9Fe-1005399512/) | May 05, 13:38      |
|       750    |            48 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/ruhige-2-zimmer-wohnung-direkt-an-der-u1-troststra%C3%9Fe-875266522/)                                             | May 05, 12:01      |
|       735    |            37 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-neubauwohnung-inkl-komplettk%C3%BCche-loggia-und-kellerabteil-/-hs28-top-216-840338411/)                 | May 05, 11:16      |
|       770    |           nan |          2 | 03. Landstraße   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/wohnen-im-zentrum---mit-blick-zum-%22schweizergarten%22-1981009689/)                                        | May 05, 10:58      |
|       771.17 |            41 |          2 | 05. Margareten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/zentrale-neubauwohnung-1893775745/)                                                                              | May 05, 10:49      |
|       700    |            80 |          3 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/vollm%C3%B6blierte-studentenwohnung-1137058099/)                                                                  | May 05, 10:47      |
|       795    |            40 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/wundersch%C3%B6ne-2-zimmer-wohnung-in-top-lage-1395567074/)                                                       | May 05, 02:22      |
|       799.99 |            38 |          2 | 14. Penzing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/%2Atop-modern%2A---lichtdurchflutete-neubau-wohnung-mit-balkon-in-bester-lage-1217667538/)                          | May 05, 00:37      |
