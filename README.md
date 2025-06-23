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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                                                             | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       890    |            40 |          2 | 09. Alsergrund   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/besichtigungen:-mittwoch-25.-juni-um-8:15%21%21%21-helle-westseitige-2-zimmer-wohnung---nahe-u6-nussdorferstrasse---1090-wien-1113510332/) | Jun 23, 09:22      |
|       806.7  |            46 |          2 | 05. Margareten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/sofortbezug-mit-terrasse-eigengarten-und-garagenplatz-vollm%C3%B6blierte-spitzenneubauwohnung-1299144616/)                                 | Jun 23, 07:11      |
|       854.47 |            51 |          2 | 08. Josefstadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1080-josefstadt/in-toplage-2-zimmerwohnung-n%C3%A4he-bennoplatz%21-bennogasse-23/33-1164629880/)                                                           | Jun 23, 06:31      |
|       670    |            65 |          3 | 03. Landstraße   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/direktvergabe-wiener-wohnen-vormerkschein-vor-05/2024-912697125/)                                                                     | Jun 22, 23:08      |
|       795    |            36 |          2 | 05. Margareten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/zentralgelegen---kurzzeitmiete%28zwischenmiete%29-all-inklusive%21%21-1583737212/)                                                         | Jun 22, 20:40      |
|       750    |            35 |          2 | 03. Landstraße   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/15-zimmer-singelwohnung-am-rochusmarkt---all-inclusive-1847734592/)                                                                   | Jun 22, 16:24      |
|       804    |            50 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/helle-2-zimmer-wohnung-in-zentraler-lage-im-2.-bezirk---ab-september-1423523778/)                                                        | Jun 22, 11:16      |
