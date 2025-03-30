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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                    | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       469    |            38 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/moderne-kleinwohnung-2-zimmer-1277902762/)                                                         | Mar 30, 06:40      |
|       750    |            41 |          2 | 04. Wieden       | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1040-wieden/wohnung-im-vierten-2019519176/)                                                                       | Mar 29, 19:36      |
|       765    |            41 |          2 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/helle-2-zimmer-wohnung-nahe-brunnenmarkt-1698974716/)                                              | Mar 29, 17:55      |
|       480    |            32 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/g%C3%BCnstige-wohnung-direkt-bei-u---bahnstation-friedensbr%C3%BCcke-831129886/)                | Mar 29, 17:34      |
|       670    |            62 |          3 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/gemeindewohnung-in-1110-wien-direktvergabe-weiterzugeben--wiener-wohnen-vormerkschein-1652350055/) | Mar 29, 14:50      |
|       491.75 |            47 |          2 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/2-zimmer-gemeindewohnung-zu-vermieten-vormerkschein-28.02.2025-1346605518/)                        | Mar 29, 14:50      |
|       799    |            52 |          3 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/wohnung-zu-vermieten-abl%C3%B6se-voll-m%C3%B6bliert-16.-bezirk-3-zimmer-1755000410/)               | Mar 29, 11:39      |
|       457    |            53 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/neue-2-zimmer-gemeindewohnung-im-2.-bezirk-zu-vergeben-1057271336/)                             | Mar 29, 11:31      |
