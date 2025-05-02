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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                                                                             | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       647.25 |            48 |          2 | 09. Alsergrund           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/2-zimmer-wohnung-in-toplage-alser-stra%C3%9Fe---sanierter-altbau-zweitbezug-%7C-ab-1.-juni-2025-859816456/)                                                                                | May 02, 15:28      |
|       795.55 |            63 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/gut-geschnittene-eckwohnung-im-2.-liftstock---revitalisiertes-gr%C3%BCnderzeithaus-1946101800/)                                                                             | May 02, 14:27      |
|       460    |            39 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/provisionsfrei-f%C3%BCr-den-mieter%21-liebhartsgasse-hofgr%C3%BCnruhelage-altbaumiete-39m%C2%B2-1.-stock-in-separatem-hofgeb%C3%A4ude-gelegen-befristet-studenten-bevorzugt%21-2003802503/) | May 02, 13:37      |
|       669.52 |            34 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/exklusives-wohnen-in-der-residenz-montleart---modernes-ambiente-trifft-auf-altbauflair---top-wohnungen-unbefristet-zu-vermieten-2012117644/)                                                  | May 02, 13:08      |
|       770    |           nan |          3 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/mitten-im-10ten---zentral-und-ruhig-gelegen-1439997573/)                                                                                                                                    | May 02, 11:45      |
|       678    |            56 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/56-m2-wohnung-wien-16-ruhige-lage-2042061403/)                                                                                                                                              | May 02, 10:46      |
|       771.22 |            55 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/open-house-am-5.5.-17:50-18:10-1043938714/)                                                                                                                                                   | May 02, 10:19      |
|       775    |            40 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/erstbezug-nach-sanierung---top-2-zimmer-wohnung-nur-1-minute-zur-u-bahn%21-897014564/)                                                                                                      | May 02, 09:46      |
|       660    |            60 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeinde-2-zimmer-wohnung-mit-balkon-1707461575/)                                                                                                                                           | May 02, 07:56      |
|       579    |            54 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/gemeinde-wohnung-direktvergabe-931315084/)                                                                                                                                                    | May 01, 22:38      |
|       799    |            39 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/orea-%7C-sch%C3%B6ne-2-zimmer-wohnung-mit-guter-anbindung-%7C-smart-besichtigen-%C2%B7-online-anmieten-935252328/)                                                                          | May 01, 17:25      |
|       635    |            45 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/45m-wohnung-im-3-bezirk-1859732317/)                                                                                                                                                  | May 01, 16:35      |
|       645    |            40 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/charmante-2-zimmer-wohnung-nahe-u6-thaliastra%C3%9Fe---perfekt-f%C3%BCr-singles-oder-paare-1813305604/)                                                                                     | May 01, 15:48      |
