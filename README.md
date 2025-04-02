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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                  | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       761.64 |            64 |          2 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/provisionsfrei:-unbefristeter-64m%C2%B2-altbau-in-hofruhelage--1170-wien-2032330216/)                              | Apr 02, 14:29      |
|       789    |            39 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/orea-%7C-charmante-2-zimmer-wohnung-nahe-u6-%7C-smart-besichtigen-%C2%B7-online-anmieten-1765217068/)            | Apr 02, 13:26      |
|       745    |            42 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/%2Aprovisionsfrei%2A-sch%C3%B6negeflegte-2-zimmer-wohnung---ideal-f%C3%BCr-p%C3%A4rchen-oder-singles-871791214/) | Apr 02, 12:34      |
|       750    |            44 |          3 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/44m%C2%B2---citynah---singles-und-p%C3%A4rchen---n%C3%A4he-mariahilferstra%C3%9Fe-1642453213/)   | Apr 02, 10:47      |
|       792.03 |            52 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/topsanierte-5233-m%C2%B2---altbauhit-%2Amit-k%C3%BCche%2A-1654411305/)                                             | Apr 02, 07:04      |
|       799.23 |            41 |          2 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/modernes-wohnen-im-erstbezug---frisch-sanierte-wohnung-mit-hochwertiger-ausstattung.---wohntraum-2125011910/)      | Apr 02, 06:55      |
|       790    |            74 |          3 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/direktvergabe-gemeindewohnung-mit-vormerkschein-30.04.2024---hervorragende-lage-949980584/)                | Apr 01, 19:19      |
|       477    |            47 |          2 | 02. Leopoldstadt         | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/direktvergabe-ger%C3%A4umige-2-zimmer-wohnung-mit-wienerwohnticket:28.02.2025-1836074634/)                    | Apr 01, 17:37      |
|       759    |            58 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/%2B%2B-neu-%2B%2B-2-zimmer-wohnung-%2B%2B-thaliastra%C3%9Fe-%2B%2B-1738283935/)                                  | Apr 01, 17:20      |
