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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                                       | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       764.5  |            65 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/sch%C3%B6ne-2-zimmer-wohnung-u1---n%C3%A4he-4.-og-1881214435/)                                                        | May 14, 08:04      |
|       536    |            45 |          2 | 03. Landstraße   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/toplage-im-3.-bezirk%21-45-m%C2%B2-gemeindewohnung-1529288376/)                                                 | May 13, 23:45      |
|       540    |            48 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/%21-dringend%21-gemeindewohnung%21-direktvergabe-nur-mit-g%C3%BCltigem-wiener-wohnticket-vms-30.04.25%21-1068837510/)  | May 13, 22:11      |
|       749    |            51 |          2 | 05. Margareten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/baujahr-2008---2-zimmer-neubauwohnung-2064208493/)                                                                   | May 13, 20:39      |
|       575    |            56 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/direktvergabe%21-2-zimmer-von-gemeinde-wohnung%21-1532416452/)                                                        | May 13, 18:43      |
|       766    |            60 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/10.-belgradplatz---provisionsfreie-2-zimmer-neubau-loggiamiete-mit-gr%C3%BCnblick-in-wienerberg-n%C3%A4he-869316861/) | May 13, 17:32      |
|       726    |            34 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/mitten-in-meidling---nahe-schlo%C3%9F-sch%C3%B6nbrunn-1938384679/)                                                     | May 13, 15:48      |
|       600    |            42 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/bitte-nicht-mehr-anfragen---ruhige-2-zimmer-wohnung-%7C-3.-stock-%7C-n%C3%A4he-praterstern-1829818422/)            | May 13, 14:33      |
|       700    |            50 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/zentral-lage-%7C-sch%C3%B6ne-2-zimmer-wohnung-1495425221/)                                                            | May 13, 13:29      |
|       783.42 |            53 |          2 | 03. Landstraße   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/2-zimmer-wohnung--hochparterre--provisionsfrei-zu-vermieten-1211063936/)                                        | May 13, 11:50      |
|       769    |            47 |          2 | 14. Penzing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/charmante-altbauwohnung-direkt-bei-u3-318572406/)                                                                       | May 13, 07:45      |
|       750    |            48 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/%22charmante-2-zimmerwohnung-n%C3%A4he-wilhelmsdorfer-park%22-869729092/)                                              | May 13, 07:12      |
|       750    |            60 |          2 | 14. Penzing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/%22teilm%C3%B6blierte-2-zimmer-wohnung-in-ruhiger-lage-in-1140-wien%21%22-916846374/)                                   | May 13, 07:12      |
