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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                                                      | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       699.6  |            44 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/goldschlagstra%C3%9Fe%21-helle-2-zimmer-traumwohnung%21-keine-anrufe---anfragen-nur-per-mail-1661433388/)                                            | Mar 07, 13:51      |
|       729.98 |            53 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/sehr-sch%C3%B6ne-2-zimmer-wohnung-mit-balkon%21-1194153677/)                                                                                                         | Mar 07, 13:49      |
|       721.55 |            49 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/sehr-helle-2-zimmer-wohnung-im-zentrum-von-favoriten-1623854276/)                                                                                                    | Mar 07, 13:28      |
|       460    |            43 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeinde-wohnung-zu-vergeben-1100-wien-1124502640/)                                                                                                                  | Mar 07, 13:22      |
|       650    |            38 |          2 | 05. Margareten           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/moderne-wohnung-in-margareten-1425533192/)                                                                                                                          | Mar 07, 12:42      |
|       796.05 |            48 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/wundersch%C3%B6ne-48-m%C2%B2-wohnung-mit-2-zimmern-im-16.-bezirk---rosseggergasse-15-1974310578/)                                                                    | Mar 07, 12:20      |
|       534.62 |            53 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/%28reserviert%29-sonnige-53m%C2%B2-gemeindewohnung-mit-balkon-prater--&-donaukanalblick---direktvergabe-vmd-vor-31.01.2025-ab-juli-verf%C3%BCgbar-1466171694/) | Mar 07, 10:55      |
|       720.88 |            78 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/721-eur-bruttomiete.-sehr-gut-eingeteilte-gepflegte-wohnung-977341521/)                                                                              | Mar 07, 10:49      |
|       622    |            55 |          3 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/gemeinde-wohnung-direktvergabe-841840312/)                                                                                                                           | Mar 07, 08:18      |
|       500    |            48 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/2-zimmer-gemeinde-wohnung-vms-31.10.2024-1466213463/)                                                                                                          | Mar 06, 20:43      |
|       799.79 |            44 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/attraktive-und-sch%C3%B6ne-2-zimmer-wohnung-in-der-r%C3%B6mergasse%21-828621730/)                                                                                    | Mar 06, 19:34      |
|       467    |            61 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeindewohnung--direktvergabe-vmd:-31.12.2024-1536003267/)                                                                                                          | Mar 06, 19:29      |
|       750    |            56 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/2-zimmer-wohnung-792659043/)                                                                                                                                         | Mar 06, 18:46      |
|       680    |            48 |          2 | 05. Margareten           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/provisionsfrei-f%C3%BCr-den-mieter%21-vogelsanggasse-hofruhelage-zentrumsnahe-48m%C2%B2-altbaumiete-3.-stock-studenten-bevorzugt%21-1507702647/)                    | Mar 06, 18:00      |
|       650    |            30 |          2 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/sch%C3%B6ne-neubauwohnung-f%C3%BCr-singles---1-minischlafzimmer-1-wohnk%C3%BCche-mit-balkon-994031042/)                                                                | Mar 06, 16:53      |
|       753    |            52 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/wohnung-in-gepflegter-wohnhausanlage-2124302366/)                                                                                                                      | Mar 06, 16:38      |
|       726    |            57 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/sonnig-und-helle-wohnung-1615221997/)                                                                                                                                  | Mar 06, 16:25      |
|       781.26 |            52 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/unbefristet%21-2-zimmer--wohnung-in-der-raaber-bahn-gasse.-1562285608/)                                                                                              | Mar 06, 14:39      |
|       720    |            54 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/helle-altbauwohnung-zum-wohlf%C3%BChlen-1397772009/)                                                                                                                 | Mar 06, 14:33      |
|       750    |            58 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/p%C3%A4rchen--oder-singlewohnung-privat-1110-1573552988/)                                                                                                            | Mar 06, 14:08      |
