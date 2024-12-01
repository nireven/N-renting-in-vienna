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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District    | Link                                                                                                                                                                                                                                    | 📅 Published Date   |
|-------------:|--------------:|-----------:|:---------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       479    |            45 |          2 | 03. Landstraße | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/gemeindewohnung-zur-direktvergabe-nur-mit-wohnticket-bis-30.06.2024-1235327178/)                                                             | Dec 01, 16:55      |
|       658    |            62 |          3 | 22. Donaustadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/gemeinde-wohnung-direkt-vergabe-kaiserm%C3%BChlen-neben-u1-833386502/)                                                                            | Dec 01, 16:07      |
|       598.96 |            44 |          2 | 03. Landstraße | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/44-m2-zwei-zimmer-wohnung%21-n%C3%A4he-botanischer-garten%21-fasanviertel%21-1390163502/)                                                    | Dec 01, 15:25      |
|       611    |            47 |          2 | 07. Neubau     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1070-neubau/helle-2-zimmer-wohnung-in-1070-wien-nachmieter-gesucht%21-924079937/)                                                                                 | Dec 01, 14:32      |
|       598    |            58 |          2 | 11. Simmering  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/gemeindewohnung-2-zimmer-1110-wien-1124888707/)                                                                                                    | Dec 01, 11:37      |
|       749.71 |            42 |          2 | 11. Simmering  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/ina---p%C3%A4rchenwohnung-mit-freifl%C3%A4che-n%C3%A4he-wasserspielplatz-leberberg-1904606435/)                                                    | Dec 01, 10:24      |
|       575.41 |            49 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/helle-2-zimmer-wohnung-n%C3%A4chst-viktor-adler-markt-keplerplatz-wielandpark-u1-1721294398/)                                                      | Nov 30, 16:25      |
|       750    |            56 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/provisionsfrei-fernkorngasse-interessante-attraktive-teilm%C3%B6blierte-2-zimmer-wohnung-in-guter-lage-matzleinsdorferplatz-n%C3%A4he-2102019983/) | Nov 30, 16:21      |
