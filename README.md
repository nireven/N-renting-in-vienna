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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District    | Link                                                                                                                                                                                    | 📅 Published Date   |
|-------------:|--------------:|-----------:|:---------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       466    |            46 |          2 | 06. Mariahilf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1060-mariahilf/direktvergabe-wiener-wohnen-2-zimmer-n%C3%A4he-mariahilferstrasse-988853902/)                      | Mar 24, 12:22      |
|       722.23 |            33 |          2 | 16. Ottakring  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/baujahr-2019%21%21%21-kompakte-2-zimmer-wohnung%21%21%21-top-infrastruktur%21%21%21-1628608950/)   | Mar 24, 11:40      |
|       477.98 |            47 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeindewohnung---direktvergabe-1527300546/)                                                       | Mar 24, 11:18      |
|       524.64 |            35 |          2 | 11. Simmering  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/moderne-2-zimmer-wohnung-auf-der-simmeringer-hauptstrasse%21-1992521228/)                          | Mar 24, 11:10      |
|       704.4  |            55 |          2 | 11. Simmering  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/erstbezug%21-wohnen-in-simmering---ekz-und-u-3-n%C3%A4he-2079105332/)                              | Mar 24, 11:09      |
|       719.88 |            47 |          2 | 11. Simmering  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/gepflegte-2-zimmerwohnung-mit-balkon-1612720188/)                                                  | Mar 24, 09:18      |
|       619    |            57 |          3 | 05. Margareten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/gemeindewohnung-direktvergabe-f%C3%BCr-3-zimmer-mit-vmd-vor-dem-28.2.2025-1511509870/)            | Mar 24, 05:53      |
|       420    |            41 |          2 | 03. Landstraße | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/gemeindewohnung-zur-vergabe-1140494205/)                                                     | Mar 23, 22:07      |
|       551.09 |            61 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/genossenschaftswohnung-2-zimmer-mit-balkon-920227885/)                                             | Mar 23, 22:01      |
|       432    |            42 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/%28reserviert%29-direktvergabe-wiener-wohnen-ticket-31.12.2024-1969505461/)                        | Mar 23, 16:20      |
|       530    |            48 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/direktvergabe%2828.02.2025%29-2-zimmer-gemeindewohnung-in-favoriten---mit-abl%C3%B6se-1826919497/) | Mar 23, 15:24      |
|       700    |            37 |          2 | 14. Penzing    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/kleine-15-zimmer-wohnung-1834575149/)                                                                | Mar 23, 12:20      |
|       750    |            66 |          2 | 09. Alsergrund | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/zwischenmiete-26.3.--17.4.2025-750---885388329/)                                                  | Mar 23, 11:46      |
