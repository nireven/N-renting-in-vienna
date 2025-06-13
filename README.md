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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                              | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       868.07 |            58 |          2 | 05. Margareten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/helle-2-zimmer-wohnung-%2858-qm%29-im-5.-bezirk-mit-k%C3%BCche-und-terrasse-4.-stock-mit-aufzug-863528939/) | Jun 13, 10:52      |
|       879.91 |            49 |          2 | 06. Mariahilf    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1060-mariahilf/wohnung-im-1060-in-der-n%C3%A4he-von-mariahilferstra%C3%9Fe-und-westbahnhof-zu-vermieten-1065025210/)        | Jun 13, 09:59      |
|       739.15 |            53 |          2 | 05. Margareten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/perfekte-stadtwohnung-n%C3%A4he-pilgramgasse-u4%21-br%C3%A4uhausgasse-17-19/1/13-1260268768/)               | Jun 13, 07:00      |
|       544.69 |            50 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/gemeindewohnung-direktvergabe-vormerkschein28.02.2025-1358765607/)                                        | Jun 13, 06:44      |
|       856.62 |            54 |          2 | 09. Alsergrund   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/%2A%2Awird-aktuell-frisch-ausgemalt%2A%2A-%7C-traum-2-zimmer-wohnung-1316132113/)                           | Jun 12, 16:24      |
|       866    |            48 |          2 | 05. Margareten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/unbefristet%21-smarte-2-zimmer-wohnung-beim-siebenbrunnenplatz-1979449239/)                                 | Jun 12, 12:21      |
|       713.63 |            41 |          2 | 09. Alsergrund   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/liechtensteinstra%C3%9Fe-114:-2-zimmer-wohnung-mit-kfz-stellplatz-988402127/)                               | Jun 12, 11:22      |
