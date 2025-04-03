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
|       628.33 |            60 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/2-zimmer-gemeindewohnung-mit-balkon-ca-60m%C2%B2-%28vms-bis-28.2.2025%29-1321592714/)                                                                                          | Apr 03, 21:09      |
|       529.85 |            54 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-gemeindewohnung-mit-balkon-54m%C2%B2-%28vms-bis-31.03.2025%29-1162579671/)                                                                                            | Apr 03, 20:39      |
|       799    |            45 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/sonnwend---living%21-erstbezug---k%C3%BCche---klima---beschattung---u1-n%C3%A4he%21-1393569049/)                                                                               | Apr 03, 18:49      |
|       566    |            56 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/gemeindewohnung---direktvergabe-%28vms-bis-31.03.25%29-1377107609/)                                                                                                             | Apr 03, 17:56      |
|       583.58 |            44 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/generalsanierte-15-zimmerwohnung-nahe-u3-ottakring-1244723738/)                                                                                                                | Apr 03, 17:40      |
|       695    |            40 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/charmante-2-zimmer-wohnung-nahe-u6-thaliastra%C3%9Fe---perfekt-f%C3%BCr-singles-oder-paare-1813305604/)                                                                        | Apr 03, 15:48      |
|       598.39 |            40 |          2 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/topsanierte-unbefristete-altbauwohnung-in-der-balderichgasse-1963873568/)                                                                                                        | Apr 03, 14:26      |
|       554.57 |            39 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/n%C3%A4he-u3-station-ii-g%C3%BCnstige-singlewohnung-ii-zwischen-stadthalle-und-schmelz-ii-10min-in-die-wiener-innenstadt-1702291691/)                          | Apr 03, 13:47      |
|       704    |           nan |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/in-besonders-attraktiver-lage---mitten-in-hetzendorf-1291158926/)                                                                                                               | Apr 03, 13:27      |
|       799.98 |            41 |          2 | 09. Alsergrund           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/studentenhit:-2-zimmer-wohnung-mit-kfz-stellplatz-und-perfekter-infrastruktur---n%C3%A4he-spittelau-/-nu%C3%9Fdorferstra%C3%9Fe-u6-988402127/)                                | Apr 03, 11:22      |
|       780    |            58 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/%28reserviert%29-top-wg-geeignete-2-zimmer-wohnung-im-12.-bezirk-1379797406/)                                                                                                   | Apr 03, 08:41      |
|       680    |            43 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/erstbezug-n%C3%A4he-meidlinger-markt-und-u4/-u6-792770248/)                                                                                                                     | Apr 03, 08:22      |
|       787.05 |            65 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/2-zimmerwohnung-3.-stock-kein-lift-09.04.25-16.30-18.00-h-1631051185/)                                                                                                           | Apr 03, 02:56      |
|       588.86 |            56 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/gemeindewohnung-11.-bezirk-mit-balkon-5662m2-1649928707/)                                                                                                                      | Apr 02, 23:52      |
|       755    |            62 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/studenten-wg-f%C3%BCr-2-personen-1959319100/)                                                                                                                                   | Apr 02, 20:25      |
|       632.12 |            50 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/%2Akurzzeitmiete-m%C3%B6glich/-short-term-rent-possible%2A-nahe-westbahnhof:-ger%C3%A4umige-2-zimmer-wohnung-mit-ausgezeichneter-verkehrsanbindung-900306781/) | Apr 02, 20:00      |
