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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                                                                                | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       432    |            42 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/direktvergabe-wiener-wohnen-ticket-31.12.2024-1147334553/)                                                                                                                                     | Feb 07, 07:38      |
|       598.7  |            48 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/helle-2-zimmer-wohnung-n%C3%A4hethaliastra%C3%9Fe-1576037450/)                                                                                                                                 | Feb 06, 21:39      |
|       765.95 |            47 |          2 | 02. Leopoldstadt         | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/hofseitige-2-zimmer-stielalbauwohnung---n%C3%A4he-u1-vorgartenstra%C3%9Fe-778319933/)                                                                                                       | Feb 06, 19:32      |
|       548    |            36 |          2 | 02. Leopoldstadt         | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/provisionsfrei-f%C3%BCr-den-mieter%21-tandelmarktgasse-n%C3%A4chst-u1/u2-altbauhauptmiete-36m%C2%B2-hofruhelage-3.-stock-studenten-bevorzugt%21-1194444437/)                                | Feb 06, 19:29      |
|       479    |            50 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmerwohnung-bei-u-bahn-keplerplatz-1269054020/)                                                                                                                                            | Feb 06, 17:44      |
|       799.88 |            57 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/provisionsfrei:-unbefristeter-57m%C2%B2-altbau-mit-einbauk%C3%BCche---1140-wien-1432133190/)                                                                                                     | Feb 06, 17:17      |
|       739    |            50 |          2 | 06. Mariahilf            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1060-mariahilf/befristete-untermiete%21-m%C3%B6bliert-%21-ruhig%21-1948306609/)                                                                                                                               | Feb 06, 16:12      |
|       632.12 |            50 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/nahe-westbahnhof:-ger%C3%A4umige-wohnung-mit-ausgezeichneter-verkehrsanbindung-1782887214/)                                                                                    | Feb 06, 16:03      |
|       532.49 |            69 |          3 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/charmante-altbauwohnung-in-der-singrienergasse-meidling-stilvoll-wohnen-mit-charakter-1044229690/)                                                                                              | Feb 06, 15:48      |
|       595    |            41 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/%2Aprovisionsfrei%2A-gepflegte-2-zimmer-wohnung-ideal-f%C3%BCr-singles-oder-studenten-1412179388/)                                                                                              | Feb 06, 15:21      |
|       763.03 |            47 |          2 | 05. Margareten           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/video%21-studentenwohnung-klein-und-fein---ab-april-25-2046729124/)                                                                                                                           | Feb 06, 15:17      |
|       737    |           nan |          3 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/mitten-im-10ten---zentral-und-ruhig-gelegen-1213380153/)                                                                                                                                       | Feb 06, 12:58      |
|       599    |            34 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/ca.-34-m2-erstbezug-nach-sanierung-atelier-im-souterrain-f%C3%BCr-firma-oder-privat---all-inclusive-miete-warm-1578533243/)                                                                      | Feb 06, 12:01      |
|       680.43 |            75 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/n%C3%A4he-u3-station-enkplatz---2-zimmer-mit-separater-k%C3%BCche---vollm%C3%B6bliert---an-der-simmeringer-hauptstra%C3%9Fe-1610991859/)                                                       | Feb 06, 11:27      |
|       799.98 |            41 |          2 | 09. Alsergrund           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/studentenhit:-2-zimmer-wohnung-mit-kfz-stellplatz-und-perfekter-infrastruktur---n%C3%A4he-spittelau-/-nu%C3%9Fdorferstra%C3%9Fe-u6-%28besichtigungen-erst-ab-23.1-m%C3%B6glich%29-988402127/) | Feb 06, 11:22      |
|       552.31 |            60 |          2 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/sch%C3%B6ne-&-helle-2-zimmer-gemeindewohnung-n%C3%A4he-elterleinplatz-%21%21-wohnticket-g%C3%BCltig-ab-sp%C3%A4testens-31.01.25-%21%21-2088832958/)                                              | Feb 06, 10:36      |
|       741.74 |            48 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/ol%C3%A9-ol%C3%A9---oh-la-laa-%21-1101051871/)                                                                                                                                                 | Feb 06, 10:22      |
