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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District    | Link                                                                                                                                                                     | 📅 Published Date   |
|-------------:|--------------:|-----------:|:---------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|          760 |            55 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/zwei-zimmer-wohnung-1601183165/)                                                    | May 10, 09:43      |
|          668 |            47 |          2 | 05. Margareten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/topsaniert%21-sonnige-2-zimmer-wohnung%21-n%C3%A4he-u4%21-1074421774/)             | May 10, 08:08      |
|          510 |            50 |          2 | 03. Landstraße | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/nachmieter-gesucht--nur-f%C3%BCr-sozialbau-genossenschaft-mieter-1539228419/) | May 10, 07:48      |
|          794 |            50 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/zwei-zimmer---50m%C2%B2---hauptbahnhof-n%C3%A4he-1816814362/)                       | May 09, 16:03      |
|          790 |            74 |          3 | 12. Meidling   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/helle-3-zimmer-wohnung-in-bahnhofs-n%C3%A4he---auch-wg-tauglich-1888755054/)         | May 09, 15:48      |
|          799 |            48 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/viola-park---moderne-2-zimmerwohnung-mit-balkon-885839769/)                         | May 09, 15:47      |
|          670 |            70 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/ruhige-altbauwohnung-1630794656/)                                                   | May 09, 15:07      |
|          678 |            56 |          2 | 16. Ottakring  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/56-m2-wohnung-wien-16-ruhige-lage-2042061403/)                                      | May 09, 10:46      |
