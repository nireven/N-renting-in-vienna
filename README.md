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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                                   | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       622    |            55 |          3 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/gemeinde-wohnung-direktvergabe-841840312/)                                                                                                        | Mar 07, 08:18      |
|       799    |            75 |          3 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/gro%C3%9Fz%C3%BCgige-wohnung-in-ruhiger-gasse-nahe-u4-und-u6%21-lift-k%C3%BCche-und-gepflegtes-geb%C3%A4ude%21-967895272/)        | Mar 07, 08:15      |
|       500    |            48 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/2-zimmer-gemeinde-wohnung-vms-31.10.2024-1466213463/)                                                                                       | Mar 06, 20:43      |
|       799.79 |            44 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/attraktive-und-sch%C3%B6ne-2-zimmer-wohnung-in-der-r%C3%B6mergasse%21-828621730/)                                                                 | Mar 06, 19:34      |
|       467    |            61 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeindewohnung--direktvergabe-vmd:-31.12.2024-1536003267/)                                                                                       | Mar 06, 19:29      |
|       750    |            56 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/2-zimmer-wohnung-792659043/)                                                                                                                      | Mar 06, 18:46      |
|       680    |            48 |          2 | 05. Margareten           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/provisionsfrei-f%C3%BCr-den-mieter%21-vogelsanggasse-hofruhelage-zentrumsnahe-48m%C2%B2-altbaumiete-3.-stock-studenten-bevorzugt%21-1507702647/) | Mar 06, 18:00      |
|       650    |            30 |          2 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/sch%C3%B6ne-neubauwohnung-f%C3%BCr-singles---1-minischlafzimmer-1-wohnk%C3%BCche-mit-balkon-994031042/)                                             | Mar 06, 16:53      |
|       753    |            52 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/wohnung-in-gepflegter-wohnhausanlage-2124302366/)                                                                                                   | Mar 06, 16:38      |
|       726    |            57 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/sonnig-und-helle-wohnung-1615221997/)                                                                                                               | Mar 06, 16:25      |
|       781.26 |            52 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/unbefristet%21-2-zimmer--wohnung-in-der-raaber-bahn-gasse.-1562285608/)                                                                           | Mar 06, 14:39      |
|       720    |            54 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/helle-altbauwohnung-zum-wohlf%C3%BChlen-1397772009/)                                                                                              | Mar 06, 14:33      |
|       790    |            55 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/helle-2-zimmer-wohnung-in-favoriten-1700079494/)                                                                                                  | Mar 06, 14:27      |
|       750    |            58 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/p%C3%A4rchen--oder-singlewohnung-privat-1110-1573552988/)                                                                                         | Mar 06, 14:08      |
|       628.76 |            45 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/helle-kleinwohnung-1347178753/)                                                                                                                   | Mar 06, 14:08      |
|       790    |            51 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-wohnung-mit-8-m%C2%B2-loggia-inkl.-garagenplatz-4.-liftstock-direkt-bei-u1-1647747406/)                                                  | Mar 06, 13:56      |
|       789    |            38 |          2 | 07. Neubau               | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1070-neubau/1070---wien---gepflegte-ruhige-hofseitige-balkonwohnung-mit-m%C3%B6blierter-k%C3%BCche-1413994831/)                                                  | Mar 06, 13:42      |
|       675    |            72 |          2 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/privatvergabe-1170-wien-helle-2-zimmerwohnung-im-zweiten-lift-stock-mit-guter-verkehrsanbindung-1745963020/)                                        | Mar 06, 12:17      |
|       799.98 |            41 |          2 | 09. Alsergrund           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/studentenhit:-2-zimmer-wohnung-mit-kfz-stellplatz-und-perfekter-infrastruktur---n%C3%A4he-spittelau-/-nu%C3%9Fdorferstra%C3%9Fe-u6-988402127/)   | Mar 06, 11:22      |
|       729.01 |            43 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-neubauwohnung-mit-dachschr%C3%A4ge-inkl.-k%C3%BCche-dachterrasse-und-kellerabteil---mietbeginn-15.06.2025-/hs28-top-2-261-2045954207/)   | Mar 06, 10:19      |
