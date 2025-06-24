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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District    | Link                                                                                                                                                                                                                                                    | 📅 Published Date   |
|-------------:|--------------:|-----------:|:---------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       861.55 |            55 |          2 | 06. Mariahilf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1060-mariahilf/2-zimmerwohnung-n%C3%A4he-mariahilfer-strasse%21-gfrornergasse-13-top-14-2135258371/)                                                                              | Jun 24, 06:21      |
|       850    |            50 |          2 | 03. Landstraße | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/singelterrassenwohnung-n%C3%A4he-schloss-belvedere-2132774882/)                                                                                              | Jun 23, 11:15      |
|       780    |            51 |          2 | 09. Alsergrund | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/1090-saniertes-hofhaus-in-ruhelage-n%C3%A4he-akh-1006686555/)                                                                                                     | Jun 23, 09:47      |
|       890    |            40 |          2 | 09. Alsergrund | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/besichtigungen:-mittwoch-25.-juni-um-8:15-und-donnerstag-26.6-um-13.00%21-helle-westseitige-2-zimmer-wohnung---nahe-u6-nussdorferstrasse---1090-wien-1113510332/) | Jun 23, 09:22      |
|       854.47 |            51 |          2 | 08. Josefstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1080-josefstadt/in-toplage-2-zimmerwohnung-n%C3%A4he-bennoplatz%21-bennogasse-23/33-1164629880/)                                                                                  | Jun 23, 06:31      |
