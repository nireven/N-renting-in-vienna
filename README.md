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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District     | Link                                                                                                                                                                                                                                                              | 📅 Published Date   |
|-------------:|--------------:|-----------:|:----------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       545    |            57 |          2 | 23. Liesing     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/gemeindewohnung-1230-5690-m%C2%B2-1409653118/)                                                                                                                                 | Nov 28, 12:55      |
|       485.72 |            37 |          2 | 10. Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/topzustand%21-1778683951/)                                                                                                                                                   | Nov 28, 12:27      |
|       790    |            48 |          2 | 10. Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-wohntraum-mit-balkon-im-viola-park-1011592335/)                                                                                                                     | Nov 28, 11:58      |
|       790    |            47 |          2 | 10. Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-wohnung-mit-balkon-im-viola-park-1566207186/)                                                                                                                       | Nov 28, 11:51      |
|       750    |            57 |          2 | 10. Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/modernisierte-2-zimmer-wohnung-in-direkter-u-bahn-und-fh-campus-n%C3%A4he-1740397186/)                                                                                       | Nov 28, 11:16      |
|       735    |            38 |          2 | 12. Meidling    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/%2Aneues-projekt%2A-urbanes-wohnen-im-wildgarten-ab-01.02.2025-1377855747/)                                                                                                   | Nov 28, 11:11      |
|       459    |            40 |          2 | 10. Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/entz%C3%BCckende-2-zimmer-nahe-keplerplatz-968481856/)                                                                                                                       | Nov 28, 10:50      |
|       760.41 |            42 |          2 | 11. Simmering   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/teilm%C3%B6beliert-und--renoviert-klein-und-funktional-1362776126/)                                                                                                          | Nov 28, 10:45      |
|       790    |            54 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/charmante-2-zimmer-dachgeschosswohnung-mit-zwei-terrassen-2069008596/)                                                                                                     | Nov 28, 10:39      |
|       799.99 |            43 |          2 | 10. Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-neubauwohnung-inkl.-komplettk%C3%BCche-loggia-und-kellerabteil-/hs17-top-b-30-1421079285/)                                                                          | Nov 28, 09:57      |
|       790    |            42 |          2 | 14. Penzing     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/entz%C3%BCckende-2-zimmer-miete-mit-garten-n%C3%A4he-auhof-center-1992259277/)                                                                                                 | Nov 28, 09:57      |
|       771.41 |            41 |          2 | 14. Penzing     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/tolle-2-zimmer-wohnung-im-herzen-von-breitensee%21-ab-dem-01.02.2025-verf%C3%BCgbar-1847703648/)                                                                               | Nov 28, 09:26      |
|       670    |            63 |          3 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/gemeindewohnung-63-m2-3-zimmer-und-balkon%21-miete-680%E2%82%AC-plus-strom-direktvergabe-wohnticket-vor-31.05.2024-mindestens-3-zimmer-%21-1079882752/)                    | Nov 28, 09:15      |
|       799    |            55 |          2 | 19. Döbling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1190-d%C3%B6bling/ruhige-helle-2-zimmer-wohnung-mit-balkon-2009630686/)                                                                                                                     | Nov 28, 09:14      |
|       749    |            39 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/leo-131---hochwertiger-neubau-zu-fairen-preisen---gut-angebunden-%28u1-leopoldau-%2B-u6-floridsdorf%29---mit-vollm%C3%B6blierter-k%C3%BCche-&-freifl%C3%A4che-1026345968/) | Nov 28, 08:57      |
|       508    |            58 |          2 | 16. Ottakring   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/sozialbau-genossenschaft-2-zimmer-1154953269/)                                                                                                                               | Nov 28, 08:18      |
|       705.19 |            41 |          2 | 19. Döbling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1190-d%C3%B6bling/sch%C3%B6ne-2-zimmer-wohnung-im-19.-bezirk-1140179140/)                                                                                                                   | Nov 28, 06:48      |
|       733.77 |            42 |          2 | 19. Döbling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1190-d%C3%B6bling/gem%C3%BCtliche-singlewohnung-im-19.-bezirk-1191172900/)                                                                                                                  | Nov 28, 06:48      |
|       706.83 |            36 |          2 | 10. Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/zentral-gelegenes-apartment-in-wien---f%C3%BCr-singles-oder-paare-918995592/)                                                                                                | Nov 28, 03:31      |
|       540    |            43 |          2 | 14. Penzing     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/matznerpark/helle-top-gepflegte-altbauwohnung-1005880698/)                                                                                                                     | Nov 27, 21:35      |
