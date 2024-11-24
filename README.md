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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District     | Link                                                                                                                                                                                                        | 📅 Published Date   |
|-------------:|--------------:|-----------:|:----------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       523.08 |            51 |          2 | 23. Liesing     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/gemeindewohnung-1230-/-u-bahn-n%C3%A4he-und-gr%C3%BCnlage-%28nur-mit-vormerkschein-bis-31.10.2024%29-789153519/)         | Nov 24, 18:19      |
|       760    |            47 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/2-zimmer-wohnung-mit-balkon-n%C3%A4he-marchfeldkanal-1217593785/)                                                    | Nov 24, 17:25      |
|       748    |            48 |          2 | 10. Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/sch%C3%B6ne-2-zimmer-wohnung-1701311299/)                                                                              | Nov 24, 17:23      |
|       776    |            85 |          3 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/top-wohnung-in-1210-bwsg-genossenschaft-50000%E2%82%AC-genossenschaftsanteil-20000%E2%82%AC-abl%C3%B6se-1658735151/) | Nov 24, 15:16      |
|       619    |            59 |          2 | 10. Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/direktvergabe-gemeindewohnung-2-zimmer-mit-loggia-1778704295/)                                                         | Nov 24, 13:56      |
|       586    |            58 |          3 | 10. Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeindewohnung-mit-vmd-bis-31.10.2024-f%C3%BCr-3-zimmer-869974245/)                                                   | Nov 24, 13:19      |
|       710    |            32 |          2 | 13. Hietzing    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1130-hietzing/all-in-tarif%21-provisionsfrei%21-koffer-packen-und-einziehen%21-wohnung-voll-m%C3%B6bliert-1887682130/)                | Nov 24, 12:12      |
|       612.36 |            46 |          2 | 14. Penzing     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/top-12-%7C-u4-hietzing-%7C-sch%C3%B6nbrunn-1133761678/)                                                                  | Nov 24, 11:25      |
|       736.46 |            46 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/zweizimmerwohnung-mit-hofseitigem-balkon-2069493154/)                                                                 | Nov 24, 10:44      |
|       749.71 |            42 |          2 | 11. Simmering   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/ina---p%C3%A4rchenwohnung-mit-freifl%C3%A4che-n%C3%A4he-wasserspielplatz-leberberg-1904606435/)                        | Nov 24, 10:24      |
|       788.4  |            75 |          3 | 12. Meidling    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/zentrumsnahe-3-zimmerwohnung-1591435077/)                                                                               | Nov 24, 06:16      |
