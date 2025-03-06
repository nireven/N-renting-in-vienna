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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                                 | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       753    |            52 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/wohnung-in-gepflegter-wohnhausanlage-2124302366/)                                                                                                 | Mar 06, 16:38      |
|       726    |            57 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/sonnig-und-helle-wohnung-1615221997/)                                                                                                             | Mar 06, 16:25      |
|       781.26 |            52 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/unbefristet%21-2-zimmer--wohnung-in-der-raaber-bahn-gasse.-1562285608/)                                                                         | Mar 06, 14:39      |
|       720    |            54 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/helle-altbauwohnung-zum-wohlf%C3%BChlen-1397772009/)                                                                                            | Mar 06, 14:33      |
|       790    |            55 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/helle-2-zimmer-wohnung-in-favoriten-1700079494/)                                                                                                | Mar 06, 14:27      |
|       750    |            58 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/p%C3%A4rchen--oder-singlewohnung-privat-1110-1573552988/)                                                                                       | Mar 06, 14:08      |
|       628.76 |            45 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/helle-kleinwohnung-1347178753/)                                                                                                                 | Mar 06, 14:08      |
|       790    |            51 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-wohnung-mit-8-m%C2%B2-loggia-inkl.-garagenplatz-4.-liftstock-direkt-bei-u1-1647747406/)                                                | Mar 06, 13:56      |
|       789    |            38 |          2 | 07. Neubau               | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1070-neubau/1070---wien---gepflegte-ruhige-hofseitige-balkonwohnung-mit-m%C3%B6blierter-k%C3%BCche-1413994831/)                                                | Mar 06, 13:42      |
|       675    |            72 |          2 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/privatvergabe-1170-wien-helle-2-zimmerwohnung-im-zweiten-lift-stock-mit-guter-verkehrsanbindung-1745963020/)                                      | Mar 06, 12:17      |
|       799.98 |            41 |          2 | 09. Alsergrund           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/studentenhit:-2-zimmer-wohnung-mit-kfz-stellplatz-und-perfekter-infrastruktur---n%C3%A4he-spittelau-/-nu%C3%9Fdorferstra%C3%9Fe-u6-988402127/) | Mar 06, 11:22      |
|       729.01 |            43 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-neubauwohnung-mit-dachschr%C3%A4ge-inkl.-k%C3%BCche-dachterrasse-und-kellerabteil---mietbeginn-15.06.2025-/hs28-top-2-261-2045954207/) | Mar 06, 10:19      |
|       690    |            37 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/%2Aneues-projekt%2A-urbanes-wohnen-im-wildgarten%21-1244532636/)                                                                                 | Mar 06, 10:18      |
|       690.01 |            37 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/erstbezug-ab-februar:-15-zimmer-wohnparadies-mit-eigenem-garten-2059191679/)                                                                     | Mar 06, 10:03      |
|       790    |            49 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/2-zimmer-mietwohnung-bei-u4-station-unter-st.-veit-1427215525/)                                                                                   | Mar 06, 09:25      |
|       670    |            62 |          3 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/gemeindewohnung-in-1110-wien-direktvergabe-weiterzugeben--wiener-wohnen-vormerkschein-1652350055/)                                              | Mar 06, 09:16      |
|       745.57 |            48 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/%2A%2A2-zimmer-mit-separater-k%C3%BCche---ruhelage-i-innenhofseitig-i-troststrasse-i-jetzt-anfragen%2A%2A-883597894/)                           | Mar 06, 08:27      |
|       598.13 |            45 |          2 | 09. Alsergrund           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/%28reserviert%29-sanierter-erstbezug-bei-u6-alsergrund-neben-meduni-&-akh---unbefristet-1030543842/)                                           | Mar 06, 08:03      |
|       721.39 |            65 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/charmante-3-zimmer-wohnung-im-5.og.-1742650434/)                                                                                                | Mar 06, 02:44      |
|       629.28 |            50 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/%28reserviert%29-2-zimmer-altbau-wohnung-%2B-balkon-1857522706/)                                                                | Mar 05, 19:56      |
