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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District   | Link                                                                                                                                                                                                        | 📅 Published Date   |
|-------------:|--------------:|-----------:|:--------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       785    |            42 |          2 | 12. Meidling  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/wundervolle-2-zimmer-wohnung-in-toller-lage---einbauk%C3%BCche-inklusive---ab-01.08.2025-verf%C3%BCgbar%21-1879327887/) | Apr 09, 11:48      |
|       780    |            33 |          2 | 12. Meidling  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/privat-:-wundersch%C3%B6ne-ruhige-neubau-wohnung-mit-balkon-2-zimmer-1162038703/)                                       | Apr 09, 10:36      |
|       799.23 |            41 |          2 | 17. Hernals   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/modernes-wohnen-im-erstbezug---frisch-sanierte-wohnung-mit-hochwertiger-ausstattung.---wohntraum-2125011910/)            | Apr 09, 06:55      |
|       460    |            46 |          2 | 14. Penzing   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/abl%C3%B6se-nur-1k---gemeindewohnung-direktvergabe-vm-feb-2025-774170219/)                                               | Apr 08, 18:05      |
|       630.28 |            54 |          2 | 17. Hernals   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/supermiete-2-zimmerwohnung-mit-allen-nebenr%C3%A4umen-top-zustand-unbefristet-zu-mieten-1201998038/)                     | Apr 08, 17:06      |
|       778    |            56 |          2 | 10. Favoriten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/sch%C3%B6ne-2-zimmer-dachwohnung-am-belgradplatz%21-1986764950/)                                                       | Apr 08, 15:27      |
|       785.01 |            48 |          2 | 10. Favoriten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/viola-park---2-zimmer-balkonwohnung---ihr-zuhause-mit-direkter-u1-anbindung-%7Cam-laaer-berg-1139947170/)              | Apr 08, 11:59      |
|       644.01 |            61 |          2 | 14. Penzing   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/sehr-helle-2-zimmer-altbauwohnung---n%C3%A4he-sch%C3%B6nbrunn-810256197/)                                                | Apr 08, 10:36      |
