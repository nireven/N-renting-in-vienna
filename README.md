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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                                    | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       750    |            44 |          2 | 06. Mariahilf            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1060-mariahilf/webgasse-1060-wien-%2A%2A%2Afein-und-zentral-wohnen-mit-terrassennutzung%2A%2A-1845468809/)                                                        | Mar 06, 12:47      |
|       675    |            72 |          2 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/privatvergabe-1170-wien-helle-2-zimmerwohnung-im-zweiten-lift-stock-mit-guter-verkehrsanbindung-1745963020/)                                         | Mar 06, 12:17      |
|       799.98 |            41 |          2 | 09. Alsergrund           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/studentenhit:-2-zimmer-wohnung-mit-kfz-stellplatz-und-perfekter-infrastruktur---n%C3%A4he-spittelau-/-nu%C3%9Fdorferstra%C3%9Fe-u6-988402127/)    | Mar 06, 11:22      |
|       729.01 |            43 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-neubauwohnung-mit-dachschr%C3%A4ge-inkl.-k%C3%BCche-dachterrasse-und-kellerabteil---mietbeginn-15.06.2025-/hs28-top-2-261-2045954207/)    | Mar 06, 10:19      |
|       690    |            37 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/%2Aneues-projekt%2A-urbanes-wohnen-im-wildgarten%21-1244532636/)                                                                                    | Mar 06, 10:18      |
|       690.01 |            37 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/erstbezug-ab-februar:-15-zimmer-wohnparadies-mit-eigenem-garten-2059191679/)                                                                        | Mar 06, 10:03      |
|       790    |            49 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/2-zimmer-mietwohnung-bei-u4-station-unter-st.-veit-1427215525/)                                                                                      | Mar 06, 09:25      |
|       661.63 |            54 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/simmeringer-hauptstra%C3%9Fe/enkplatz:-2-zimmer-loggiawohnung---innenhof-ruhelage---hervorragende-verkehrsanbindung-und-infrastruktur-1746428305/) | Mar 06, 09:25      |
|       670    |            62 |          3 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/gemeindewohnung-in-1110-wien-direktvergabe-weiterzugeben--wiener-wohnen-vormerkschein-1652350055/)                                                 | Mar 06, 09:16      |
|       745.57 |            48 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/%2A%2A2-zimmer-mit-separater-k%C3%BCche---ruhelage-i-innenhofseitig-i-troststrasse-i-jetzt-anfragen%2A%2A-883597894/)                              | Mar 06, 08:27      |
|       598.13 |            45 |          2 | 09. Alsergrund           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/sanierter-erstbezug-bei-u6-alsergrund-neben-meduni-&-akh---unbefristet-1030543842/)                                                               | Mar 06, 08:03      |
|       721.39 |            65 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/charmante-3-zimmer-wohnung-im-5.og.-1742650434/)                                                                                                   | Mar 06, 02:44      |
|       696.64 |            51 |          2 | 05. Margareten           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/top---stilaltbauwohnung%21---n%C3%A4he-matzleinsdorferplatz-gelegen%21-1409421198/)                                                               | Mar 05, 20:37      |
|       629.28 |            50 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/2-zimmer-altbau-wohnung-%2B-balkon-1857522706/)                                                                                    | Mar 05, 19:56      |
|       676    |            57 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/gemeinde-wohnung-1362623821/)                                                                                                                      | Mar 05, 17:29      |
|       598    |            56 |          3 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/%2Asonniger-altbau-nahe-elterleinplatz%2A-1737237926/)                                                                                               | Mar 05, 13:28      |
|       745    |            42 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/%2Aprovisionsfrei%2A-sch%C3%B6negeflegte-2-zimmer-wohnung---ideal-f%C3%BCr-p%C3%A4rchen-oder-singles-871791214/)                                   | Mar 05, 12:34      |
|       650    |            57 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/2-zimmer-wohnung-in-1030-wien---57-m%C2%B2-im-1.-liftstock-1385945099/)                                                                      | Mar 05, 12:22      |
|       442.62 |            43 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/%28reserviert%29-preisg%C3%BCnstige-2-zimmer-wohnung-%2A-landstra%C3%9Fer-g%C3%BCrtel-1517314984/)                                           | Mar 05, 11:58      |
