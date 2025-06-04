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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District    | Link                                                                                                                                                                                                          | 📅 Published Date   |
|-------------:|--------------:|-----------:|:---------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       520.25 |            47 |          2 | 05. Margareten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/gemeindewohnung-nahe-matzleinsdorfer-pl.-nur-mit-g%C3%BCltigem-wiener-wohn-ticket-1980287901/)                          | Jun 04, 15:44      |
|       795    |            54 |          2 | 03. Landstraße | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/3.erdbergstrasse---provisionsfreie-charmante-2-zimmer-neubaumiete-direkt-beim-kardinal-naglplatz-2105617351/)      | Jun 04, 15:32      |
|       816.93 |            54 |          2 | 05. Margareten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/wiedner-hauptstra%C3%9Fe---gro%C3%9Fz%C3%BCgige-2-zimmer-wohnung-zu-vermieten-1497036728/)                              | Jun 04, 11:58      |
|       622.22 |            39 |          2 | 09. Alsergrund | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/openhouse-am-6.6.-von-13:00---13:20-uhr%21-keine-anrufe-anfragen-nur-per-mail%21-1158485666/)                           | Jun 04, 11:42      |
|       601.07 |            55 |          2 | 04. Wieden     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1040-wieden/1040-sch%C3%B6ne-2-zimmer-wohnung-nahe-alois-drasche-park-1138123774/)                                                      | Jun 04, 10:28      |
|       899    |            61 |          2 | 03. Landstraße | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/openhouse---heute-04.06.-um-17:00-uhr-_-perfekte-stadtwohnung:-direkt-bei-der-urania-mit-donaublick%21-965817735/) | Jun 04, 07:34      |
|       760    |            40 |          2 | 06. Mariahilf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1060-mariahilf/wohnung-in-1060-wien-1675858195/)                                                                                        | Jun 03, 23:27      |
|       875.94 |            62 |          2 | 04. Wieden     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1040-wieden/tolles-zuhause-n%C3%A4he-hauptbahnhof%21-1615573530/)                                                                       | Jun 03, 17:16      |
