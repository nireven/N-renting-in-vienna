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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                                                            | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       750    |            45 |          2 | 05. Margareten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/student:-innen-zur-untermiete-gesucht-%28nur-1-person%29-779443963/)                                                                      | Mar 30, 18:09      |
|       750    |            38 |          2 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/ruhige-und-helle-2-zimmer-wohnung-mit-blick-in-den-innenhof-keine-provision-&-heizung-in-bk-inkludiert%21-1934789698/)                     | Mar 30, 17:12      |
|       432    |            42 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/%28reserviert%29-direktvergabe-wiener-wohnen-ticket-31.12.2024-1969505461/)                                                                | Mar 30, 16:20      |
|       600.07 |            44 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/44m2-wohnung---unbefristet-1043020343/)                                                                                                     | Mar 30, 14:33      |
|       610    |            55 |          3 | 14. Penzing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/gemeindewohnung-direktvergabe-1152453997/)                                                                                                   | Mar 30, 14:09      |
|       470    |            54 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/moderne-sch%C3%B6ne-2-zimmer-wohnung-in-wien-1100-%28oberlaa%29-gef%C3%B6rderte-wohnung-m%C3%B6bliert---sofort-verf%C3%BCgbar-1367589114/) | Mar 30, 12:46      |
|       676.34 |            43 |          2 | 14. Penzing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/erstbezug-nach-top-sanierung:-helle-2-zimmer-wohnung-nahe-hanusch-krankenhaus-1329993018/)                                                   | Mar 30, 12:16      |
|       469    |            38 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/moderne-kleinwohnung-2-zimmer-1277902762/)                                                                                                 | Mar 30, 06:40      |
|       750    |            41 |          2 | 04. Wieden       | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1040-wieden/wohnung-im-vierten-2019519176/)                                                                                                               | Mar 29, 19:36      |
|       765    |            41 |          2 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/helle-2-zimmer-wohnung-nahe-brunnenmarkt-1698974716/)                                                                                      | Mar 29, 17:55      |
|       480    |            32 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/g%C3%BCnstige-wohnung-direkt-bei-u---bahnstation-friedensbr%C3%BCcke-831129886/)                                                        | Mar 29, 17:34      |
