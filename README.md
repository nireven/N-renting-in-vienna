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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District    | Link                                                                                                                                                                                                 | 📅 Published Date   |
|-------------:|--------------:|-----------:|:---------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       540    |            40 |          2 | 03. Landstraße | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/sanierter-altbaucharme---2-zimmer-im-herzen-von-1030-wien-1443446871/)                                    | Apr 16, 04:35      |
|       732.87 |            82 |          3 | 11. Simmering  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/altbaujuwel-in-simmering---stilvolle-3-zimmer-wohnung-mit-flair-1342211474/)                                    | Apr 16, 03:44      |
|       699.06 |            39 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/neubau---singlewohnung-mit-loggia-zu-vermieten-892408464/)                                                      | Apr 15, 21:25      |
|       795    |            49 |          2 | 08. Josefstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1080-josefstadt/top---angebot-966731938/)                                                                                      | Apr 15, 18:19      |
|       638    |           nan |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/attraktives-wohnen-mitten-im-sonnwendviertel-1756684583/)                                                       | Apr 15, 15:27      |
|       799.86 |            41 |          2 | 17. Hernals    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/modernes-wohnen-im-erstbezug---frisch-sanierte-wohnung-mit-hochwertiger-ausstattung---jetzt-anfragen-1366664417/) | Apr 15, 13:48      |
|       769    |            45 |          2 | 11. Simmering  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/mietwohnungen-in-niedrigenergiehaus---provisionsfrei---zu-mieten-in-1110-wien-947223014/)                       | Apr 15, 13:45      |
|       726.14 |            38 |          2 | 11. Simmering  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/2-zimmer-wohnung-mit-balkon-im-2.-obergescho%C3%9F-in-niedrigenergiehaus---zu-mieten-in-1110-wien-1594327667/)  | Apr 15, 13:38      |
|       726.1  |            39 |          2 | 11. Simmering  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/2-zimmer-wohnung-mit-balkon-in-niedrigenergiehaus---zu-mieten-in-1110-wien-1646102503/)                         | Apr 15, 13:37      |
|       733.61 |            45 |          2 | 11. Simmering  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/mietwohnungen-in-niedrigenergiehaus---provisionsfrei---zu-mieten-in-1110-wien-1447076825/)                      | Apr 15, 12:50      |
|       785.01 |            48 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/viola-park---2-zimmer-balkonwohnung---ihr-zuhause-mit-direkter-u1-anbindung-%7Cam-laaer-berg-1139947170/)       | Apr 15, 11:59      |
