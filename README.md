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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                  | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       899.44 |            42 |          2 | 04. Wieden       | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1040-wieden/perfekt-aufgeteilte-2-zimmer-wohnung-inkl.-loggia%21-2097175072/)                                   | Jul 01, 10:36      |
|       890    |            62 |          2 | 07. Neubau       | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1070-neubau/2-zimmer%21-generalsaniert%21-stilaltbau%21-westbahnhofn%C3%A4he%21-unbefristet%21-1161970764/)     | Jul 01, 10:18      |
|       665.07 |            48 |          2 | 03. Landstraße   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/%2A%2A-garconniere-%2A%2A-f%C3%BCr-singles-im-fasanviertel-1273563877/)                    | Jul 01, 10:16      |
|       449.36 |            30 |          3 | 05. Margareten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/lager/atelier-zur-miete-in-1050-wien---ehemalige-wohnung-nahe-pilgramgasse-1798271816/)         | Jul 01, 09:57      |
|       458.79 |            47 |          2 | 05. Margareten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/gemeindebauwohnung-per-direktvergabe-1490919102/)                                               | Jun 30, 23:51      |
|       870    |            39 |          2 | 06. Mariahilf    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1060-mariahilf/zwischenmiete---vollm%C3%B6blierte-2-zimmer-neubauwohnung-im-6.-bezirk-824708999/)               | Jun 30, 20:51      |
|       803    |            90 |          3 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/3-zimmer-wohnung-im-2.-bezirk---m%C3%B6bliert---90-m%C2%B2---%E2%82%AC800-miete-1054702474/)  | Jun 30, 18:30      |
|       765.87 |            47 |          2 | 03. Landstraße   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/%28reserviert%29-nachmieter-gesucht-f%C3%BCr-wohnung-in-3er-bezirk---47m%C2%B2-948403138/) | Jun 30, 13:37      |
