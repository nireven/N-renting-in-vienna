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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                                                                 | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       559.41 |            50 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/2.-hofruhelage%21-15-zimmer%21-nette-startwohnung-f%C3%BCr-studenten%21-1802259048/)                                                         | Apr 24, 13:27      |
|       530    |            48 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-gemeindewohnung-zu-vergeben-%28nur-mit-wiener-wohn-ticket-vor-dem-28.2.2025%29-1877800390/)                                            | Apr 24, 12:34      |
|       490    |            44 |          2 | 14. Penzing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/gemeindewohnung-direktvergabe-vms-vor-dem-31.03.2025-1824670041/)                                                                                 | Apr 24, 12:28      |
|       748.88 |            57 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/generalsanierte-zwei-zimmer-wohnung-unbefristet-bei-der-u1-troststra%C3%9Fe-%21-2141885842/)                                                    | Apr 24, 12:13      |
|       663    |            63 |          2 | 17. Hernals      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/2-zimmer-gemeindewohnung-1707661184/)                                                                                                             | Apr 24, 12:01      |
|       550    |            39 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/sch%C3%B6ne-single-oder-p%C3%A4rchenwohnungen-n%C3%A4he-wienerberg-861915716/)                                                                  | Apr 24, 11:58      |
|       799.98 |            41 |          2 | 09. Alsergrund   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/studentenhit:-2-zimmer-wohnung-mit-kfz-stellplatz-und-perfekter-infrastruktur---n%C3%A4he-spittelau-/-nu%C3%9Fdorferstra%C3%9Fe-u6-988402127/) | Apr 24, 11:22      |
|       745.42 |            63 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/ger%C3%A4umige-2-zimmer-wohnung-provisionsfrei-922425112/)                                                                                      | Apr 24, 09:16      |
|       748    |            43 |          2 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/2-zimmerwohnung-im-2.og-mit-loggia-1457854191/)                                                                                                 | Apr 24, 07:39      |
|       689    |            66 |          3 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/3-zimmer-gemeinde-wohnung-830576584/)                                                                                                           | Apr 23, 20:12      |
|       720.51 |            56 |          2 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/neuwertig%21-1443592918/)                                                                                                                       | Apr 23, 13:57      |
|       789    |            39 |          2 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/orea-%7C-charmante-2-zimmer-wohnung-nahe-u6-%7C-smart-besichtigen-%C2%B7-online-anmieten-1765217068/)                                           | Apr 23, 13:26      |
|       750    |            26 |          2 | 05. Margareten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/%22hallo-sie-kommen-zum-studieren-oder-f%C3%BCr-die-...-1104762709/)                                                                           | Apr 23, 13:07      |
|       745    |            42 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/%2Aprovisionsfrei%2A-sch%C3%B6negeflegte-2-zimmer-wohnung---ideal-f%C3%BCr-p%C3%A4rchen-oder-singles-871791214/)                                | Apr 23, 12:34      |
|       770    |            48 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/%28reserviert%29-sch%C3%B6ne-2-zimmer-wohnung-mit-m%C3%B6beln-abzugeben---bezugsbereit-in-ca.-1-monat-%28nach-absprache%29-2037442014/)         | Apr 23, 12:24      |
|       785    |            42 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/wundervolle-2-zimmer-wohnung-in-toller-lage---einbauk%C3%BCche-inklusive---ab-01.08.2025-verf%C3%BCgbar%21-1879327887/)                          | Apr 23, 11:48      |
