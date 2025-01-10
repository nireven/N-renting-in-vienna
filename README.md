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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                                                              | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       799    |            39 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1-monat-mietfrei:-erstbezug-im-gr%C3%BCnen-nahe-der-u2---zwischen-badeteich-hirschstetten-und-seestadt-1704280680/)                                                         | Jan 10, 07:54      |
|       775    |            48 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/sch%C3%B6ne-2-zimmer-wohnung-in-guter-lage-990597111/)                                                                                                       | Jan 10, 07:37      |
|       750    |            47 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/%22kompakte-eleganz:-erstbezug-in-sanierter-wohnung%21%22-1010670731/)                                                                                                       | Jan 10, 07:12      |
|       678.83 |            49 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/gem%C3%BCtliche-2-zimmer-wohnung-im-3.-og-2009648704/)                                                                                                                       | Jan 10, 02:49      |
|       705    |            68 |          3 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/3-zimmer-gemeindewohnung-1459925097/)                                                                                                                                       | Jan 09, 21:59      |
|       766    |            65 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/altbauappartement-im-hetzendorfer-cottage-2001283882/)                                                                                                                        | Jan 09, 20:37      |
|       617    |            64 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/wohnung-zu-vermieten-1813785410/)                                                                                                                                            | Jan 09, 20:30      |
|       779    |            35 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/2-zimmer-wohnung-%7C-thaliastra%C3%9Fe-%7C-billa-im-haus-%7C-3.-liftstock-1753848084/)                                                                                       | Jan 09, 19:33      |
|       748    |            50 |          2 | 08. Josefstadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1080-josefstadt/provisionsfrei-f%C3%BCr-den-mieter%21-lange-gasse-sch%C3%B6nbornpark-hofruhelage-zentrumsnahe-50m%C2%B2-altbaumiete-1.-stock-unbefristet-studenten-bevorzugt%21-953152243/) | Jan 09, 19:18      |
|       602.5  |            43 |          2 | 18. Währing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1180-w%C3%A4hring/bitte-vorerst-keine-anfragen-%28-reserviert%29-super-zentrale-15-zimmer-wohnung-1895424573/)                                                                              | Jan 09, 19:17      |
|       799    |            39 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1-monat-mietfrei:-erstbezug-im-gr%C3%BCnen-nahe-der-u2---zwischen-badeteich-hirschstetten-und-seestadt-1121290609/)                                                         | Jan 09, 17:31      |
|       779    |            42 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/leopold-xxi---traumhafte-2-zimmerwohnung-mit-anbindung-ins-stadtinnere-1789730226/)                                                                                        | Jan 09, 16:45      |
|       700    |            70 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/gemeindewohnung-780339729/)                                                                                                                                                    | Jan 09, 16:13      |
|       734.12 |            47 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/generalsanierte-helle-2-zimmer-wohnung-nahe-meidlinger-hauptstra%C3%9Fe---provisionsfrei-1378114662/)                                                                         | Jan 09, 15:53      |
|       520.52 |            52 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/gemeindewohnung-vms.30.11.2024-831678220/)                                                                                                                                 | Jan 09, 14:03      |
|       750    |            49 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/2-zimmer-dachgeschosswohnung-%2A%2Awarmmiete%2A%2Aohne-provision%2A%2Abusstation-vor-der-haust%C3%BCre%2A%2A-909090098/)                                                   | Jan 09, 12:53      |
|       650    |            42 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/befristete-miete-1960545360/)                                                                                                                                                 | Jan 09, 12:05      |
|       538.33 |            51 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/gemeindewohnung-per-direktvergabe-1120-wien-1487952557/)                                                                                                                      | Jan 09, 12:02      |
|       799    |            55 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/ca.-55-m2-%282-zimmer%29-erstbezug-nach-sanierung-atelier-im-souterrain-f%C3%BCr-firma-oder-privat---all-inclusive-miete-warm-1832119767/)                   | Jan 09, 11:55      |
|       799.98 |            41 |          2 | 09. Alsergrund           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/studentenhit:-2-zimmer-wohnung-mit-kfz-stellplatz-und-perfekter-infrastruktur---n%C3%A4he-spittelau-/-nu%C3%9Fdorferstra%C3%9Fe-u6-988402127/)                              | Jan 09, 11:22      |
