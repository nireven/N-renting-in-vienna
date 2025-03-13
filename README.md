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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                                                             | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       760    |            45 |          2 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/sch%C3%B6ne-helle-wohnung-sehr-gute-%C3%B6ffentliche-verkehrsanbindung-sehr-gute-infrastruktur-1300163401/)                                                                   | Mar 13, 21:25      |
|       614    |            61 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/%28reserviert%29-gemeindewohnung--direktvergabe-vmd:-31.12.2024-1536003267/)                                                                                                | Mar 13, 19:29      |
|       595    |            53 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/zentral-gelegene-gemeindewohnung---direktvergabe---sehr-guter-zustand--teilm%C3%B6biliert---vormerkschein-notwendig%21-verf%C3%BCgbar-ab-ende-juni/-anfang-juli-1549362117/) | Mar 13, 17:31      |
|       716.44 |            52 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/2-zimmerwohnung-n%C3%A4he-schloss-sch%C3%B6nbrunn-1507908607/)                                                                                                               | Mar 13, 17:16      |
|       694.79 |            50 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-erdgeschosswohnung-im-10.bezirk-n%C3%A4he-r%C3%A4umannplatz%21-1904442257/)                                                                                        | Mar 13, 17:15      |
|       799    |            61 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/1140-wien---gesamtmiete-inkl.-heizung/warmwasser---gepflegte-altbauwohnung---sofortbezug-890239375/)                                                                          | Mar 13, 16:41      |
|       545    |            54 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/gemeindewohnung-dringend-direktvergabe-1160-wien-ab-sofort%21-997187755/)                                                                                                   | Mar 13, 15:26      |
|       770    |            70 |          2 | 08. Josefstadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1080-josefstadt/top-lage-und-ausstattung-im-zentrum-rathausn%C3%A4he-2-zimmer-770.---brutto-1207957347/)                                                                                   | Mar 13, 15:24      |
|       700    |            86 |          3 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/3-zimmer-gemeindewohnung-zur-weitervergabe-1467675361/)                                                                                                     | Mar 13, 14:17      |
|       799.98 |            41 |          2 | 09. Alsergrund           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/studentenhit:-2-zimmer-wohnung-mit-kfz-stellplatz-und-perfekter-infrastruktur---n%C3%A4he-spittelau-/-nu%C3%9Fdorferstra%C3%9Fe-u6-988402127/)                             | Mar 13, 11:22      |
|       729.01 |            43 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-neubauwohnung-mit-dachschr%C3%A4ge-inkl.-k%C3%BCche-dachterrasse-und-kellerabteil---mietbeginn-15.06.2025-/hs28-top-2-261-2045954207/)                             | Mar 13, 10:19      |
|       446.34 |            45 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/tolle-2-zimmer-gemeindewohnung-mit-2-balkonen%21---vormerkticket:-28.02.2025%21-1582779541/)                                                                                  | Mar 13, 09:03      |
