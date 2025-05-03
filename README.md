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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                                                                                                       | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       750    |            45 |          2 | 05. Margareten           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/student:-innen-zur-untermiete-gesucht-%28nur-1-person%29-2044871970/)                                                                                                                                                | May 03, 13:18      |
|       695.01 |            46 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/exklusive-hoflage%21-868058652/)                                                                                                                                                                                      | May 03, 12:14      |
|       575.89 |            54 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/supersch%C3%B6ne-helle-gut-angelegte-&-gepflegte-gemeindewohnung-mit-loggia/-terrasse-freier-sicht-&-blick-ins-gr%C3%BCne-in-guter-lage---wr.-wohnticket-vormerkdatum-bis/-vor-28.02.2025-erforderlich%21-819573369/) | May 03, 09:48      |
|       582.16 |            42 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/top-sanierte-2-zimmer-wohnung-im-dg%21-880507954/)                                                                                                                                                                    | May 03, 06:51      |
|       540    |            48 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/gemeindewohnung/-%21-direktvergabe-vms-31.03.25%21-1812943628/)                                                                                                                                                        | May 02, 16:57      |
|       622.27 |            45 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/sch%C3%B6ne-2-zimmer-wohnung-mit-loggia-n%C3%A4he-stadthalle-1432310788/)                                                                                                                             | May 02, 16:34      |
|       647.25 |            48 |          2 | 09. Alsergrund           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/%2Aanfragenstopp%2A-2-zimmer-wohnung-in-toplage-alser-stra%C3%9Fe---sanierter-altbau-zweitbezug-%7C-ab-1.-juni-2025-859816456/)                                                                                      | May 02, 15:28      |
|       795.55 |            63 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/gut-geschnittene-eckwohnung-im-2.-liftstock---revitalisiertes-gr%C3%BCnderzeithaus-1946101800/)                                                                                                       | May 02, 14:27      |
|       460    |            39 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/provisionsfrei-f%C3%BCr-den-mieter%21-liebhartsgasse-hofgr%C3%BCnruhelage-altbaumiete-39m%C2%B2-1.-stock-in-separatem-hofgeb%C3%A4ude-gelegen-befristet-studenten-bevorzugt%21-2003802503/)                           | May 02, 13:37      |
|       669.52 |            34 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/exklusives-wohnen-in-der-residenz-montleart---modernes-ambiente-trifft-auf-altbauflair---top-wohnungen-unbefristet-zu-vermieten-2012117644/)                                                                            | May 02, 13:08      |
