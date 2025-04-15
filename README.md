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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District    | Link                                                                                                                                                                                   | 📅 Published Date   |
|-------------:|--------------:|-----------:|:---------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       798.66 |            46 |          2 | 16. Ottakring  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/sch%C3%B6n-aufgeteilte-2-zimmer-wohnung-mit-sonniger-freifl%C3%A4che%21-1355940294/)              | Apr 15, 09:15      |
|       788.5  |            54 |          2 | 16. Ottakring  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/gem%C3%BCtliche-2-zimmer-wohnung-inkl.-gemeinschaftsinnenhof%21-1315784558/)                      | Apr 15, 09:15      |
|       750    |            42 |          2 | 16. Ottakring  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/helle-2-zimmer-wohnung-%7Cprovisionsfrei-%7C-u3-kendlerstra%C3%9Fe-941679937/)                    | Apr 15, 06:03      |
|       799    |            45 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/sonnwend---living%21-erstbezug---k%C3%BCche---klima---beschattung---u1-n%C3%A4he%21-1661379415/)  | Apr 14, 20:38      |
|       627    |            60 |          3 | 12. Meidling   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/direktvergabe-%28gemeindewohnung%29-nur-mit-g%C3%BCltigen-vormerkschein-1520320301/)               | Apr 14, 19:20      |
|       785.8  |            49 |          2 | 12. Meidling   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/sonnige-2-zimmer-mit-balkon-zzgl.-kfz-stellplatz-1686858368/)                                      | Apr 14, 17:17      |
|       799    |            52 |          3 | 16. Ottakring  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/wohnung-zu-vermieten-abl%C3%B6se-voll-m%C3%B6bliert-16.-bezirk-3-zimmer-1755000410/)              | Apr 14, 12:54      |
|       731.81 |            55 |          2 | 17. Hernals    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/dg-wohnung-in-ruhiger-lage%21-1081205312/)                                                          | Apr 14, 11:37      |
|       797.55 |            59 |          2 | 17. Hernals    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/beautiful-2-room-apartment-with-separate-kitchen-871871071/)                                        | Apr 14, 10:25      |
|       689    |            43 |          2 | 16. Ottakring  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/entz%C3%BCckendes-dachgescho%C3%9F-am-brunnenmarkt-1963777278/)                                   | Apr 14, 09:26      |
|       750    |            53 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/wundersch%C3%B6ne-2-zimmerwohnung-im-10.-bezirk%21%21-360%C2%B0--3d-grad-besichtigung-877450305/) | Apr 14, 09:26      |
|       440    |            48 |          2 | 03. Landstraße | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/2-zimmer-gemeinde-wohnung-vms-20.02.2025-1739166108/)                                       | Apr 14, 07:26      |
