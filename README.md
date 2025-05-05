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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                                                                                                    | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       750    |            48 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/ruhige-2-zimmer-wohnung-direkt-an-der-u1-troststra%C3%9Fe-875266522/)                                                                                                              | May 05, 12:01      |
|       735    |            37 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-neubauwohnung-inkl-komplettk%C3%BCche-loggia-und-kellerabteil-/-hs28-top-216-840338411/)                                                                                  | May 05, 11:16      |
|       770    |           nan |          2 | 03. Landstraße   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/wohnen-im-zentrum---mit-blick-zum-%22schweizergarten%22-1981009689/)                                                                                                         | May 05, 10:58      |
|       771.17 |            41 |          2 | 05. Margareten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/zentrale-neubauwohnung-1893775745/)                                                                                                                                               | May 05, 10:49      |
|       700    |            80 |          3 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/vollm%C3%B6blierte-studentenwohnung-1137058099/)                                                                                                                                   | May 05, 10:47      |
|       795    |            40 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/wundersch%C3%B6ne-2-zimmer-wohnung-in-top-lage-1395567074/)                                                                                                                        | May 05, 02:22      |
|       799.99 |            38 |          2 | 14. Penzing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/%2Atop-modern%2A---lichtdurchflutete-neubau-wohnung-mit-balkon-in-bester-lage-1217667538/)                                                                                           | May 05, 00:37      |
|       787    |            58 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/1020-wien-stuwerstrasse:-extrem-sonnige-und-extrem-ruhige-2-zimmer-altbauwohnung-im-2.-stock-mit-zauberhaftem-hofgartenblick-ca.-59-m2%3B-langfristig-zu-vermieten-1649976226/) | May 04, 23:57      |
|       798.87 |            71 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/sonnige-und-teilsanierte-wohnung-f%C3%BCr-singles-und-p%C3%A4rchen-1874882456/)                                                                                                     | May 04, 18:46      |
