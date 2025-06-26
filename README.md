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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       696.01 |            47 |          2 | 03. Landstraße   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/2-zimmerwohnung-1939156392/)                                             | Jun 26, 17:17      |
|       814    |            44 |          2 | 07. Neubau       | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1070-neubau/44-m%C2%B2-urbaner-wohnraum-in-der-neustiftgasse-1629717728/)                     | Jun 26, 16:53      |
|       850    |            70 |          3 | 07. Neubau       | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1070-neubau/altbau-unbefristet-%7C-zieglergasse-%7C-renovierungsbedarf-1247915410/)           | Jun 26, 15:47      |
|       713.63 |            41 |          2 | 09. Alsergrund   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/liechtensteinstra%C3%9Fe-114:-2-zimmer-wohnung-mit-kfz-stellplatz-988402127/) | Jun 26, 11:22      |
|       880    |            83 |          4 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/gemeinde-wohnung-direktvergabe-2048614917/)                                 | Jun 26, 06:55      |
