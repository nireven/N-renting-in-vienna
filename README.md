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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                                                                   | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       552.31 |            60 |          2 | 17. Hernals      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/sch%C3%B6ne-&-helle-2-zimmer-gemeindewohnung-n%C3%A4he-elterleinplatz-%21%21-wohnticket-g%C3%BCltig-ab-sp%C3%A4testens-31.01.25-%21%21-2088832958/) | Feb 06, 10:36      |
|       741.74 |            48 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/ol%C3%A9-ol%C3%A9---oh-la-laa-%21-1101051871/)                                                                                                    | Feb 06, 10:22      |
|       758.72 |            53 |          2 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/2-zimmer-altbauwohnung-mit-viel-potential-i-1.-stock-ohne-lift-i-n%C3%A4he-thaliastra%C3%9Fe-bezirksamt-1795632021/)                              | Feb 05, 20:44      |
|       763.01 |            47 |          2 | 05. Margareten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/studentenwohnung-klein-und-fein---ab-april-25-1258156655/)                                                                                       | Feb 05, 19:38      |
|       754.93 |            93 |          3 | 17. Hernals      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/stilvolle-2-zimmer-altbauwohnung-im-erkerzimmer-in-1170--ab-sofort-verf%C3%BCgbar-1032145674/)                                                      | Feb 05, 16:49      |
|       708    |            68 |          4 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/gemeindewohnung-zur-direktvergabe-936296652/)                                                                                                     | Feb 05, 15:48      |
|       678.38 |            57 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/sonnige-2-zimmerwohnung-mit-allen-nebenr%C3%A4umen--unbefristet-zu-mieten-1712788161/)                                                            | Feb 05, 15:27      |
|       595    |            32 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/provisionsfrei---sch%C3%B6ne-2-zimmer-wohnung-ideal-f%C3%BCr-p%C3%A4rchen-oder-singles-2109286336/)                                               | Feb 05, 14:03      |
|       470    |            65 |          3 | 06. Mariahilf    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1060-mariahilf/%28reserviert%29-gemeinde-wohnung-986407142/)                                                                                                     | Feb 05, 13:30      |
|       785.84 |            47 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/ina---p%C3%A4rchenwohnung-mit-perfektem-grundriss---n%C3%A4he-kaiserebersdorf-1590079860/)                                                        | Feb 05, 12:53      |
|       767.95 |            49 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/terrassentraum-f%C3%BCr-p%C3%A4rchen---wohnung-mit-perfektem-grundriss---n%C3%A4he-einkaufszentrum-huma-eleven-1338398862/)                       | Feb 05, 12:53      |
|       771.62 |            42 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/n%C3%A4he-schloss-neugeb%C3%A4ude---wohnung-perfekt-f%C3%BCr-singles-oder-p%C3%A4rchen-mit-freifl%C3%A4che-1759659165/)                           | Feb 05, 12:29      |
|       796.05 |            48 |          2 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/wundersch%C3%B6ne-48-m%C2%B2-wohnung-mit-2-zimmern-im-16.-bezirk---rosseggergasse-15-1974310578/)                                                 | Feb 05, 12:20      |
|       450    |            40 |          2 | 03. Landstraße   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/2-zimmer-gemeindewohnung-/-wiener-wohnen-vormerkschein-30.11.2024-2074624638/)                                                              | Feb 05, 10:36      |
|       623.58 |            63 |          3 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/gemeindewohnung-mit-direktvergabr-1927370518/)                                                                                                 | Feb 05, 10:00      |
