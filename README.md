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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                                                                | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       530    |            48 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeindewohnung---direktvergabe-1838523143/)                                                                                                                                   | Apr 11, 17:40      |
|       540    |            48 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/gemeindewohnung/-%21-direktvergabe-vms-31.03.25%21-1812943628/)                                                                                                                 | Apr 11, 16:57      |
|       735    |            37 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-neubauwohnung-inkl-komplettk%C3%BCche-loggia-und-kellerabteil-/-hs28-top-216-1582882110/)                                                                             | Apr 11, 12:56      |
|       673.58 |            40 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/helle-2-zimmer-wohnung-in-ruhiger-lage-%281120-wien%29---ab-1.6.2025-1322980441/)                                                                                               | Apr 11, 08:33      |
|       700    |            50 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/studentenhit---2-zimmer-wohnung-%2850m2%29-in-1120-wien-zu-vermieten.-300-m-zu-u4/-u6-1520455880/)                                                                              | Apr 11, 08:28      |
|       582.16 |            42 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/top-sanierte-2-zimmer-wohnung-im-dg%21-953181889/)                                                                                                                             | Apr 11, 06:49      |
|       614    |            62 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/1160-wien-paletzgasse/-st%C3%B6berpark:-gut-aufgeteilte-2-zimmer-altbauwohnung-ca.-62-m2-unbefristet-zu-vermieten-1307421665/)                                                 | Apr 10, 21:28      |
|       632.12 |            50 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/%2Akurzzeitmiete-m%C3%B6glich/-short-term-rent-possible%2A-nahe-westbahnhof:-ger%C3%A4umige-2-zimmer-wohnung-mit-ausgezeichneter-verkehrsanbindung-900306781/) | Apr 10, 19:46      |
|       750    |            38 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/ruhige-und-helle-2-zimmer-wohnung-mit-blick-in-den-innenhof-keine-provision-&-heizung-in-bk-inkludiert%21-1934789698/)                                                         | Apr 10, 19:35      |
|       543.84 |            37 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-wohnung-n%C3%A4he-troststrasse%21-1828723448/)                                                                                                                        | Apr 10, 19:34      |
|       680.2  |            51 |          3 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/3-zimmer-wohnung-im-16.-direkt-beim-brunnenmarkt%21-1942295835/)                                                                                                               | Apr 10, 19:32      |
|       789.57 |            60 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/reserviert---komfortable-2-zimmer-wohnung-2012590885/)                                                                                                                         | Apr 10, 18:19      |
