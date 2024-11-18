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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                                                | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       740    |            45 |          2 | 03. Landstraße   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/2-zimmer-wohnung-mitten-im-dritten-2053489987/)                                                                          | Nov 18, 10:51      |
|       673.75 |            55 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/mietwohnung-1100-wien-1770718792/)                                                                                             | Nov 18, 10:46      |
|       799.1  |            52 |          2 | 23. Liesing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/%23%23-ubahn-n%C3%A4he---sch%C3%B6n-&-charmant---2-zimmer-%23%23-1602888048/)                                                    | Nov 18, 09:57      |
|       799.05 |            46 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/ina---wohnanlage-am-leberberg-:-top-a3-46-915431798/)                                                                          | Nov 18, 09:34      |
|       757.82 |            43 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/ina-%E2%97%8F-wohnanlage-am-leberberg:-b1-12-1773365340/)                                                                      | Nov 18, 09:34      |
|       600    |            59 |          2 | 23. Liesing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/moderne-gemeindewohnung-in-ruhiger-lage-%28vms-datum:-31.10.2024-f%C3%BCr-2-zimmer%29-2087845635/)                               | Nov 18, 09:26      |
|       790    |            46 |          2 | 21. Floridsdorf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/stammersdorfer-wohntr%C3%A4ume-erleben:-mietwohnungen-mit-option-auf-zuk%C3%BCnftigen-kauf-739383800/)                       | Nov 18, 08:56      |
|       790    |            70 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/erstbezug-nach-renovierung-2090760752/)                                                                                        | Nov 17, 23:05      |
|       470.52 |            44 |          2 | 14. Penzing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/direktvergabe-2-zimmer-gemeindewohnung-998500957/)                                                                               | Nov 17, 20:55      |
|       736.87 |            62 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/helle-2-zimmer-wohnung-am-rosenh%C3%BCgel/-hetzendorf-1400678622/)                                                              | Nov 17, 20:47      |
|       598.95 |            50 |          3 | 21. Floridsdorf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/3-zimmer-wohnung-mit-gemeinschaftsg%C3%A4rtchen-in-wien-floridsdorf-1724289823/)                                             | Nov 17, 19:30      |
|       650    |            43 |          2 | 22. Donaustadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/vollm%C3%B6blierte-apartments-mit-all-in-miete-in-n%C3%A4he-u2-donaustadtbr%C3%BCcke-1750064689/)                             | Nov 17, 18:41      |
|       782.62 |            55 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/bitte-nur-schriftliche-anfragen-keine-anrufe.-unbefristete-h%C3%BCbsche-2-zimmer-wohnung-in-der-pernerstorfergasse-824202117/) | Nov 17, 17:36      |
|       697.92 |            65 |          2 | 23. Liesing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/helle-sanierte-2-zimmer-wohnung-nur-5-gehminuten-vom-liesinger-bahnhof-entfernt-1944479031/)                                     | Nov 17, 17:21      |
|       551    |            84 |          3 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/%28reserviert%29-gemeinde-wohnung-direktvergabr-2093286640/)                                                                | Nov 17, 15:06      |
|       648    |            59 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/helle-gemeindewohnung-direktvergabe-wien-11.-1177927236/)                                                                      | Nov 17, 13:15      |
|       720    |            73 |          3 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/3-zimmer-gemeindewohnung-vormerkschein-nr.-31.01.2024-2083762439/)                                                             | Nov 17, 12:35      |
|       500    |            47 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/gemeindewohnung---direktvergabe-g%C3%BCltiger-vormerkschein-bis-31.07.2024-erforderlich%21%21-818489687/)                       | Nov 17, 12:01      |
|       749.71 |            42 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/ina---p%C3%A4rchenwohnung-mit-freifl%C3%A4che-n%C3%A4he-wasserspielplatz-leberberg-1904606435/)                                | Nov 17, 10:24      |
