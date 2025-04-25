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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                         | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       530    |            48 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeindewohnung---direktvergabe-%28wiener-wohnticket/-vormerkschein%29-1838523143/)                                     | Apr 25, 17:40      |
|       540    |            48 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/gemeindewohnung/-%21-direktvergabe-vms-31.03.25%21-1812943628/)                                                          | Apr 25, 16:57      |
|       734.4  |            36 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/wohlf%C3%BChl-wohnung-mit-loggia---barrierefrei-modern-&-perfekt-angebunden-%7C-zellmann-immobilien-786335691/)         | Apr 25, 16:16      |
|       699.06 |            39 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/neubau---singlewohnung-mit-loggia-zu-vermieten-1122111832/)                                                             | Apr 25, 15:23      |
|       790    |            62 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/privatvermietung---sonnendurchflutete-wohnung-u-bahn-westbahnhof-%28keine-provision%29-1738734345/)     | Apr 25, 15:10      |
|       785.01 |            48 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/moderne-2-zimmerwohnung-im-viola-park-mit-balkon-1866882694/)                                                           | Apr 25, 13:23      |
|       489    |            45 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-wohnung---zentrale-lage---ruhelage-1352972163/)                                                                | Apr 25, 12:37      |
|       485    |            50 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/direktvergabe-gemeindewohnung-50-m%C2%B2-1100-wien-1689668878/)                                                         | Apr 24, 22:33      |
|       490    |            42 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeindewohnung-direktvergabe-1998769728/)                                                                              | Apr 24, 20:53      |
|       609.64 |            42 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/zentral-gelegene-2-zimmer-wohnung-n%C3%A4he-reumannplatz%21-1458001703/)                                                | Apr 24, 18:48      |
|       799.74 |            49 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/orea-%7C-nahe-u1:-2-zimmer-wohnung-mit-balkon-in-den-innenhof-%7C-smart-besichtigen-%C2%B7-online-anmieten-1588699843/) | Apr 24, 17:26      |
|       799    |            39 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/orea-%7C-sch%C3%B6ne-2-zimmer-wohnung-mit-guter-anbindung-%7C-smart-besichtigen-%C2%B7-online-anmieten-935252328/)      | Apr 24, 17:25      |
|       684.3  |            42 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/provisionsfrei:-unbefristeter-42m%C2%B2-altbau-mit-einbauk%C3%BCche-und-2-zimmern---1140-wien-1988238833/)                | Apr 24, 16:47      |
|       792.61 |            50 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/sofortbezug-vollm%C3%B6blierte-spitzenneubauwohnung-n%C3%A4chst-u1---keplerplatz-1971622134/)                           | Apr 24, 16:09      |
