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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District   | Link                                                                                                                                                                                             | 📅 Published Date   |
|-------------:|--------------:|-----------:|:--------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       794    |            65 |          2 | 14. Penzing   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/sonnige-altbauwohnung-2099649851/)                                                                            | May 18, 12:22      |
|       698    |            54 |          2 | 10. Favoriten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/n%C3%A4he-u1-keplerplatz%21-2-zimmerwohnung%21-1810993031/)                                                 | May 18, 11:34      |
|       690    |            65 |          3 | 16. Ottakring | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/unbefristet---3-zimmerwohnung-1716098890/)                                                                  | May 18, 08:01      |
|       778.49 |            48 |          2 | 14. Penzing   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/provisionsfrei:-unbefristeter-48m%C2%B2-erstbezug-mit-2-zimmern-und-einbauk%C3%BCche---1140-wien-2075344855/) | May 17, 19:31      |
|       646.11 |            47 |          2 | 10. Favoriten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/tolle-zwei-zimmer-wohnung-im-2.-liftstock-1201734508/)                                                      | May 17, 18:53      |
|       483.48 |            46 |          2 | 10. Favoriten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/zwei-zimmer-wohnung-im-1.-liftstock-1027147283/)                                                            | May 17, 18:53      |
|       630.89 |            45 |          2 | 10. Favoriten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/sch%C3%B6ne-zwei-zimmer-wohnung-1023837630/)                                                                | May 17, 18:53      |
|       750    |            52 |          3 | 10. Favoriten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/helle-altbauwohnung-zum-wohlf%C3%BChlen-1859859425/)                                                        | May 17, 18:38      |
|       771.81 |            32 |          2 | 12. Meidling  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/erstbezug-mit-wohlf%C3%BChlfaktor---topmoderne-mietwohnung-nahe-u6-&-s-bahn-1215454318/)                     | May 17, 13:18      |
