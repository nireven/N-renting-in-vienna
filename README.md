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
|       528    |            46 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/helle-gut-gelegene-sanierte-2-zimmer-wohnung-in-hofruhelage-1172267050/)                                                                                                                       | Feb 13, 13:50      |
|       771    |            75 |          3 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/helle-familienwohnung-neben-meidlinger-hauptstra%C3%9Fe-1815749009/)                                                                                                                            | Feb 13, 13:37      |
|       599    |            34 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/ca.-34-m2-erstbezug-nach-sanierung-atelier-im-souterrain-f%C3%BCr-firma-oder-privat---all-inclusive-miete-warm-1578533243/)                                                                      | Feb 13, 12:01      |
|       735.97 |            55 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/charmante-2-zimmer-wohnung-am-sechshauser-g%C3%BCrtel%21-1142683402/)                                                                                                          | Feb 13, 11:58      |
|       680.43 |            75 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/n%C3%A4he-u3-station-enkplatz---2-zimmer-mit-separater-k%C3%BCche---vollm%C3%B6bliert---an-der-simmeringer-hauptstra%C3%9Fe-1610991859/)                                                       | Feb 13, 11:27      |
|       799.98 |            41 |          2 | 09. Alsergrund           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/studentenhit:-2-zimmer-wohnung-mit-kfz-stellplatz-und-perfekter-infrastruktur---n%C3%A4he-spittelau-/-nu%C3%9Fdorferstra%C3%9Fe-u6-%28besichtigungen-erst-ab-23.1-m%C3%B6glich%29-988402127/) | Feb 13, 11:22      |
|       750    |            55 |          2 | 06. Mariahilf            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1060-mariahilf/mietwohnung-1507164133/)                                                                                                                                                                       | Feb 13, 10:34      |
|       786.06 |            49 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/traumhaftes-2-zimmer-apartment-mit-balkon---viola-park---ihre-wohlf%C3%BChloase-am-laaer-berg-1658526598/)                                                                                     | Feb 13, 10:31      |
|       786.06 |            49 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/traumhaftes-2-zimmer-apartment-mit-balkon---viola-park---ihre-wohlf%C3%BChloase-am-laaer-berg-1658526598/)                                                                                     | Feb 13, 10:31      |
|       710    |            70 |          3 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/direktvergabe-gemeindewohnung-2042732503/)                                                                                                                                                      | Feb 13, 09:14      |
|       775    |            38 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/charming-2-room-apartment-in-vienna%27s-15th-district-1850184102/)                                                                                                             | Feb 13, 02:47      |
|       690    |            32 |          2 | 09. Alsergrund           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/koffer-packen-und-einziehen--zwischenmiete-oder-langfristig-1521897382/)                                                                                                                      | Feb 12, 19:15      |
|       410    |            40 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeindewohnung-mit-2-zimmern-1619947070/)                                                                                                                                                     | Feb 12, 18:16      |
|       595    |            32 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/provisionsfrei---sch%C3%B6ne-2-zimmer-wohnung-ideal-f%C3%BCr-p%C3%A4rchen-oder-singles-2109286336/)                                                                                            | Feb 12, 14:03      |
