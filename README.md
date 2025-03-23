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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District    | Link                                                                                                                                                                                                         | 📅 Published Date   |
|-------------:|--------------:|-----------:|:---------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       432    |            42 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/%28reserviert%29-direktvergabe-wiener-wohnen-ticket-31.12.2024-1969505461/)                                             | Mar 23, 16:20      |
|       530    |            48 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/direktvergabe%2828.02.2025%29-2-zimmer-gemeindewohnung-in-favoriten---mit-abl%C3%B6se-1826919497/)                      | Mar 23, 15:24      |
|       735.54 |            56 |          2 | 14. Penzing    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/gem%C3%BCtliche-2-zimmer-wohnung-n%C3%A4he-h%C3%BCtteldorfer-stra%C3%9Fe---ohne-lift-%7C-zellmann-immobilien-2009128640/) | Mar 23, 12:54      |
|       700    |            37 |          2 | 14. Penzing    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/kleine-15-zimmer-wohnung-1834575149/)                                                                                     | Mar 23, 12:20      |
|       750    |            66 |          2 | 09. Alsergrund | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/zwischenmiete-26.3.--17.4.2025-750---885388329/)                                                                       | Mar 23, 11:46      |
|       468    |            44 |          2 | 11. Simmering  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/44m2-gemeinde-wohnung-nur-mit-vormerkschein-bis-31.12.2024-direktvergabe-n%C3%A4he-u3-enkplatz-1582661529/)             | Mar 23, 10:52      |
|       778.49 |            48 |          2 | 14. Penzing    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/provisionsfrei:-unbefristeter-48m%C2%B2-erstbezug-mit-2-zimmern-und-einbauk%C3%BCche---1140-wien-2075344855/)             | Mar 22, 19:31      |
