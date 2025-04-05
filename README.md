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
|       632.12 |            50 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/%2Akurzzeitmiete-m%C3%B6glich/-short-term-rent-possible%2A-nahe-westbahnhof:-ger%C3%A4umige-2-zimmer-wohnung-mit-ausgezeichneter-verkehrsanbindung-900306781/) | Apr 05, 10:46      |
|       790    |            50 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/altbau-wohnung-813543214/)                                                                                                                                               | Apr 05, 08:42      |
|       690    |            50 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/u6-meidling-bahnhof-%7C-unbefristet-%7C-2-zimmer-998264939/)                                                                                                                    | Apr 04, 21:32      |
|       794    |            50 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/zwei-zimmer---50m%C2%B2---hauptbahnhof-n%C3%A4he-962366678/)                                                                                                                   | Apr 04, 19:54      |
|       749.39 |            41 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/sch%C3%B6ne-neubauwohnung-mit-balkon-&-moderner-ausstattung-in-wien-simmering-1116540477/)                                                                                     | Apr 04, 19:34      |
|       530    |            48 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeindewohnung---direktvergabe-1838523143/)                                                                                                                                   | Apr 04, 17:40      |
|       540    |            48 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/gemeindewohnung/-%21-direktvergabe-vms-31.03.25%21-1812943628/)                                                                                                                 | Apr 04, 16:57      |
|       700    |            37 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/kleine-15-zimmer-wohnung-1834575149/)                                                                                                                                            | Apr 04, 16:01      |
|       451    |            41 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/direktvergabe-gemeindewohnung-%28mit-wiener-wohnticket%29-974559640/)                                                                                                          | Apr 04, 15:41      |
|       735    |            37 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-neubauwohnung-inkl-komplettk%C3%BCche-loggia-und-kellerabteil-/-hs28-top-216-1582882110/)                                                                             | Apr 04, 12:56      |
|       520    |            45 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/privat-ohne-abl%C3%B6se-und-provision-1972091205/)                                                                                                                             | Apr 04, 11:30      |
|       750    |            26 |          2 | 05. Margareten           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/%22hallo-sie-kommen-zum-studieren-oder-f%C3%BCr-die-...-1960645751/)                                                                                                          | Apr 04, 10:05      |
|       679.36 |            63 |          3 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/gemeindewohnung-wiener-wohnen-vergabedatum-28.-februar-2025-1521561024/)                                                                                                         | Apr 04, 09:47      |
