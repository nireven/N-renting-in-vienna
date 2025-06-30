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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                                                                                   | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       803    |            90 |          3 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/3-zimmer-wohnung-im-2.-bezirk---m%C3%B6bliert---90-m%C2%B2---%E2%82%AC800-miete-1054702474/)                                                                   | Jun 30, 18:30      |
|       822.02 |            53 |          2 | 04. Wieden       | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1040-wieden/renovierte-wohnung-n%C3%A4he-naschmarkt-802244150/)                                                                                                                  | Jun 30, 14:18      |
|       765.87 |            47 |          2 | 03. Landstraße   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/nachmieter-gesucht-f%C3%BCr-wohnung-in-3er-bezirk---47m%C2%B2-948403138/)                                                                                   | Jun 30, 13:37      |
|       845    |            45 |          2 | 03. Landstraße   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/laendyard:-traumhafte-2-zimmer-gartenwohnung---zur-miete-in-1030-wien-1751748651/)                                                                          | Jun 30, 12:49      |
|       825    |            31 |          2 | 05. Margareten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/pauschalmiete-inklusive-warmwasser-&-heizung/k%C3%BChlung---moderne-2-zimmer-wohnung-mit-sch%C3%B6nem-balkon-in-hofruhelage---stilvolle-ausstattung-2001386578/) | Jun 30, 08:46      |
|       854.47 |            51 |          2 | 08. Josefstadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1080-josefstadt/in-toplage-2-zimmerwohnung-n%C3%A4he-bennoplatz%21-bennogasse-23/33-1164629880/)                                                                                 | Jun 30, 06:31      |
|       670    |            65 |          3 | 03. Landstraße   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/direktvergabe-wiener-wohnen-vormerkschein-vor-05/2024-912697125/)                                                                                           | Jun 29, 23:08      |
